# API 활용

## URL 활용

- requests 라이브러리 이용

```python
import requests
url = f'https://...'

# json 형식으로 받을 때
response = requests.get(url).json()

# 요청 보낼 때
res = requests.get(url)
```



## 날씨 API

- 모듈화하여 구현
- location을 사용자 입력으로 받아 해당 지역의 최고, 최저, 현재기온을 섭씨와 화씨 온도로 출력
- `weather_api.py`
  - fetch_weather_infos 함수: 지역을 인풋으로 넣으면 날씨 데이터를 리스트 형식으로 리턴하는 함수
  - get_fahrenheit 함수: 섭씨 온도를 인풋으로 넣어 화씨 온도를 리턴하는 함수

```python
# 1. (브라우저 대신) 요청을 보내 모듈을 가져온다.
import requests  # 요청 보내는 라이브러리(브라우저처럼)

# 2. 브라우저에서 먼저 원하는 데이터 받아오기, location은 사용자 입력으로 받기 -> main.py
# 4. 가져온 모듈로 URL에 요청 보내기

def fetch_weather_infos(location):
    # location 으로 woeid 가져와 url완성
    # 3. 2에서 사용한 URL을 변수로 저장 
    locationInfo_url = f'https://www.metaweather.com/api/location/search/?query={location}'
    get_locationInfo = requests.get(locationInfo_url).json()
    woeid = get_locationInfo[0]['woeid']
    url = f'https://www.metaweather.com/api/location/{woeid}/'
    response = requests.get(url).json()
    weather_infos = response['consolidated_weather']
    return weather_infos

# 5. 응답으로 가져온 데이터에 접근
# 6. 내가 원하는 도시의 현재 온도를 섭씨와 화씨로 출력하기
'''
celsius = round(response['consolidated_weather'][0]['the_temp'],3)
fahrenheit = (celsius * 9 / 5) + 32
print(f"현재 섭씨 온도는 {celsius}°C, 현재 화씨 온도는 {fahrenheit}°F")
print('현재 섭씨 온도는 {}°C, 현재 화씨 온도는 {}°F'.format(celsius, fahrenheit))
'''

def get_fahrenheit(temperature):
    return round(temperature * 1.8 + 32, 3)



```



- `main.py`

```python
from weather_api import fetch_weather_infos, get_fahrenheit
# 모듈 이용

location = input('지역을 입력하세요: ')

for weather_info in fetch_weather_infos(location):
    min_fahrenheit = get_fahrenheit(weather_info['min_temp'])
    max_fahrenheit = get_fahrenheit(weather_info['max_temp'])
    the_fahrenheit = get_fahrenheit(weather_info['the_temp'])
    date = weather_info['applicable_date']
    print(f"{date} 날짜의 최고 온도는 {round(weather_info['max_temp'], 3)}°C, {max_fahrenheit}°F 최저 온도는 {round(weather_info['min_temp'], 3)}°C, {min_fahrenheit}°F 현재 온도는 {round(weather_info['the_temp'], 3)}°C, {the_fahrenheit}°F")

```



## Chat_Bot

- 요청 보내는 방법은 두가지
  - 첫번째는 웹에서 url을 연다. (토큰 인증 불가)
  - 두번째는 requests.get(url)을 이용하여 요청을 보낸다. (토큰 인증 가능)

- `telegram_bot_test.py`

```python
import requests
# 필요한 Data
# bot에 대한 데이터

bot_token = '############' # my_bot 정보

# '나'에 대한 데이터 => URL로 접속 시 나오는 id
# update_URL = f'https://api.telegram.org/bot{bot_token}/getUpdates' 
my_id = '1588053897'

# message
message = 'Hello SSAFY'

# message 보낼 때 URL (? => 내가 넘길 추가 요청 사항(option), parameter)
message_URL = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={my_id}&text={message}'
response = requests.get(message_URL)
```



- `my_telegram_bot.py`

```python
import requests
from weather_api import fetch_weather_infos
import random

# 필요한 Data
# bot에 대한 데이터

bot_token = '####' # my_bot 정보

# '나'에 대한 데이터 => URL로 접속 시 나오는 id
update_URL = f'https://api.telegram.org/bot{bot_token}/getUpdates' 
my_id = '##'
res = requests.get(update_URL).json()

weather_infos = fetch_weather_infos('seoul')
min_celsius = round(weather_infos[0]['min_temp'], 3)
max_celsius = round(weather_infos[0]['max_temp'], 3)
the_celsius = round(weather_infos[0]['the_temp'], 3)
date = weather_infos[0]['applicable_date']
weather_ans = f"{date} 날짜의 최고 온도는 {max_celsius}°C, 최저 온도는 {min_celsius}°C, 현재 온도는 {the_celsius}°C 입니다."

#######################################
# message
user_msg = res['result'][-1]['message']['text']

def bot_msg(user_msg):
    if user_msg == '안녕':
        return 'Hello'
    elif user_msg == '안녕하세요':
        return 'Hello'
    elif user_msg == '날씨':
        return weather_ans
    elif user_msg == '날씨알려줘':
        return weather_ans
        
message = bot_msg(user_msg)
#######################################

# message 보낼 때 URL (? => 내가 넘길 추가 요청 사항, parameter)
message_URL = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={my_id}&text={message}'
response = requests.get(message_URL)

#########################
'''
질문: bot_msg함수를
def bot_msg(user_msg):
    if user_msg == '안녕' or '안녕하세요'::
        return 'Hello'
    elif user_msg == '날씨' or '날씨알려줘':
        return weather_ans
로 만들면 
user_msg가 '날씨'여도 return 값은 Hello가 나타남. Why?
'''
```



## 최저가 검색

- 네이버 쇼핑에서 'ps5' 검색결과에 대한 최저가 검색 후 출력 

```python
import requests

bot_token = '####' # my_bot 정보
my_id = '###'

#########################
client_ID = '####'
client_secret = '####'

headers = { 
    'X-Naver-Client-Id': client_ID,
    'X-Naver-Client-Secret': client_secret
}

query = 'ps5'
naver_url = f'https://openapi.naver.com/v1/search/shop.json?query={query}'
res = requests.get(naver_url, headers=headers).json()
item = res['items'][0]

message = f"{item['title']}\n {item['lprice']}원 \n {item['link']}"

#########################

message_URL = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={my_id}&text={message}'
response = requests.get(message_URL)

```

