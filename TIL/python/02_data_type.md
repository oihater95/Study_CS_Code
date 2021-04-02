# Data Type - 자료형

## 숫자형

### int, 정수

- 정수를 뜻하는 자료형
- 양의 정수, 음의 정수, 0
- 4 byte

```python
number = 123
print(number, type(number))
```



### float, 실수

- 소수점이 포함된 숫자
- 파이썬은 float만 취급, 다른 언어에서는 float와 double로 나누어짐
- float =  4 byte, double = 8 byte
- 표기

```python
number_1 = 1.2
number_2 = 4.24e10
print(number_1, type(number_1), number_2, type(number_2))
```



## String, 문자열

- `f-string`

```python
name = 'Moon'
greeting = '반갑습니다.'
print(name + '입니다. '+ greeting)
>>> Moon입니다. 반갑습니다.

print(name,'입니다.', greeting)
>>> Moon 입니다. 반갑습니다.

# String Interpolation (f-string)
print(f'{name}님, {greeting}') 
>>> Moon님, 반갑습니다.
```



- `인덱싱, 슬라이싱`
  - 리스트와 마찬가지로 0부터 시작

```python
name = 'Moon'
print(name[0])
>>> M

print(name[-1])
>>> n
```



- `PEP`
  - `""` 대신 `''` 쓰기, `''`안에 `'` 추가적으로 들어갈 때에는 바깥 쪽을 `""` 쓰거나 안 쪽 `'`를 `\'`으로 쓰기

## List

- `생성`
  - `[]`로 정의, 불러올 때도 `[]`

```python
foods = ['치킨', '삼겹살', '피자'] 
print(foods)
>>> ['치킨', '삼겹살', '피자']
```



- `인덱싱`
  - 0부터 시작

```python
foods = ['치킨', '삼겹살', '피자'] 
print(foods[0])
>>> 치킨
print(foods[-1])
>>> 피자
```



- `PEP`
  - `""` 대신 `''` 쓰기 
  - `,` 다음에 띄어쓰기 필수
  - List는 항상 복수형 이름으로, 변수이름 list로 쓰지 않기, 변수이름_list도 마찬가지



## Dictionary

- { Key : Value }
- Dictionary = Table

| 지역 | 미세먼지 | 습도 |
| ---- | -------- | ---- |
| 서울 | 50       | 70   |

```python
weather_info = {
    '지역' : '서울',
    '미세먼지' : 50
    '습도' : 70
}
# Key = '지역', '미세먼지', '습도'
# Value = '서울', 50, 70
```



| 지역 | 미세먼지 | 습도 |
| ---- | -------- | ---- |
| 서울 | 50       | 70   |
| 부산 | 30       | 80   |

```python
weather_infos = [
    {
        '지역' : '서울'
        '미세먼지' : 50
        '습도' : 70
    },
    {
        '지역' : '대구'
        '미세먼지' : 30
        '습도' : 80
    }
]
```



- `생성`
  - `{}`로 정의, 불러올 때 `[]`

```python
my_home = {
    'location' : '분당',
    'pm' : 10,
    'temp' : 3
}
print(my_home['pm'])
>>> 10
```



- 예제 1
  - Dictionary의 경우 항목을 접은 후 해당 항목을 펼치면서 접근하면 쉽다. 항목의 요소가 Dictionary인지 List인지 확인

```python
coin = {
    "BTC": {
        "opening_price": "44405000",
        "closing_price": "38806000",
        "min_price": "36640000",
        "max_price": "44999000",
        "prev_closing_price": "44404000",
        "fluctate_24H": "-7463000",
        "fluctate_rate_24H": "-16.13"
    },
    "ETH": {
        "opening_price": "1458000",
        "closing_price": "1229000",
        "min_price": "1100000",
        "max_price": "1490000",
        "prev_closing_price": "1458000",
        "fluctate_24H": "-275000",
        "fluctate_rate_24H": "-18.28"
    },
    "XRP": {
        "opening_price": "364.5",
        "closing_price": "311.9",
        "min_price": "284.2",
        "max_price": "372.7",
        "prev_closing_price": "364.2",
        "fluctate_24H": "-90.6",
        "fluctate_rate_24H": "-22.51"
    }
}

# 2-1. 코인의 정보에서 BTC의 최대 가격을 출력하시오.
print(coin['BTC']['max_price'])
>>> 44999000

# 2-2. BTC의 시가와(opening price) XRP의 시가를 더한 결과를 출력하시오.
# string -> int or float 형변환 필요
print(int(coin['BTC']['opening_price']) + float(coin['XRP']['opening_price']))
>>> 44405364.5
```



- 예제 2

```python
movie = {
    'movieInfo': {
        'movieNm': '광해, 왕이 된 남자',
        'movieNmEn': 'Masquerade',
        'showTm': '131',
        'prdtYear': '2012',
        'openDt': '20120913',
        'typeNm': '장편',
        'nations': [
            {
                'nationNm': '한국'
            }
        ],
        'genres': [
            {
                'genreNm': '사극'
            },
            {
                'genreNm': '드라마'
            }
        ],
        'directors': [
            {
                'peopleNm': '추창민',
                'peopleNmEn': 'CHOO Chang-min'
            }
        ],
        'actors': [
            {
                'peopleNm': '이병헌',
                'peopleNmEn': 'LEE Byung-hun',
                'cast': '광해/하선'
            },
            {
                'peopleNm': '류승룡',
                'peopleNmEn': 'RYU Seung-ryong',
                'cast': '허균'
            },
            {
                'peopleNm': '한효주',
                'peopleNmEn': 'HAN Hyo-joo',
                'cast': '중전'
            }
        ]
    }
}
# Dictionary는 항목 접어서 접근하면 쉬움, value가 Dictionary인지 List인지 확인
# 1. 영화의 제목을 출력하시오.(하)
print(movie['movieInfo']['movieNm'])
>>> 광해, 왕이 된 남자

# 2. 영화 감독의 영어 이름을 출력하시오.(중)
print(movie['movieInfo']['directors'][0]['peopleNmEn'])
>>> CHOO Chang-min

# 3. 영화 배우의 인원을 출력하시오. (상)
print(len(movie['movieInfo']['actors']))
>>> 3
```



## JSON (Java Script Object Notation)

```python
import requests  

url = 'https://api.agify.io?name=moon'
response = requests.get(url).json()

# 출력결과 : 내 이름은 ~~~, 나이는 ~~~,
print('내 이름은 {}, 나이는 {}'.format(response['name'], response['age']))
print(f"내 이름은 {response['name']}, 나이는 {response['age']}")
# ''안에 ''있으면 에러날 가능성 있으니 바깥쪽에는 ""로 씀
```

