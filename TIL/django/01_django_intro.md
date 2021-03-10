# 01. Django Intro

## Django

- Dynamic Web: 사용자 요청에 따라 동작 (Server-Side: JSP, SQL, PHP)
- Static Web: 미리 저장된 정적 파일 제공 (Client-Side: HTML, CSS, JS)

- Django는 Dynamic Web Frame Work



### MTV (Model-Template-View)

- Model: DB 관리
- Template: Layout(화면)
- View: 중심 컨트롤러(심장)
-  = MVC(Model-View-Controller)



#### 동작원리(Cycle)

- HTTP 요청 => URLS(urls.py): 요청을 알맞은 View로 전달(어디로 갈지 결정)
- View(views.py): 요청 동작을 하는 곳, 요청을 받아 처리 => Template(<filename>.html)을 불러와 표현
- Template은 데이터 표현을 제어하는 도구이자 표현 관련 로직
- View => HTTP 응답(HTML)
- 요청 => URLS => View => Template => View => 응답
- 데이터 흐름 순서: URLS => Views => Templates (데이터 흐름 순서 = 코딩 순서)

```python
# intro > urls.py
from django.urls import path, include
from . import views  # intro의 views와 intro의 urls는 같은 디렉토리(intro)에 위치 => .
# App(패키지처럼 불러옴)

urlpatterns = [  # forwarding
    path('test/', views.test),
    path('articles/', include('articles.urls')),
]  # include => 해당 주소로 넘겨줌
```

```python
# articles > urls.py
from django.urls import path
from . import views  # articles 디렉토리
# urlpatterns는 필수
urlpatterns = [
    path('index/', views.index),
    path('mail/', views.mail),
]
```

```python
# articles > views.py
from django.shortcuts import render
from django.http.response import HttpResponse

def index(resquest):
    return HttpResponse('This is articles/index')

def mail(request):
    return HttpResponse('MYmail: oihater95@gmail.com')

```



### 명령어 및 시작

- django-admin startproject 파일이름 (. 쓰면 하위 폴더 없이 생성)
- python manage.py runserver
- python manage.py startapp 앱 이름(생성)
- app 이름은 복수형
- app 생성(startapp) 후 등록
- startapp보다 settings에서 등록부터 하면 App 생성 안됨
- settings.py에서 INSTALLED_APPS에 추가

  - 순서: local apps > 3rd-party apps > django apps
 - end slash 필수
 - view함수에서 parameter request 필수

  

### Temlplate

#### DTL (Django Template Language)

- bulit-in template system
- 조건, 반복, 변수 치환 ,필터 등의 기능을 제공
- 프로그래밍적 로직X, 표현하기 위함
- Python과 유사하지만 Python 코드로 실행되는 것 아님

- DTL Syntax
  - Variable
  - Filters
  - Tags
  - Comments
  
  

#### Variable

`{{ variable }}`

- render()를 사용하여 views.py에서 정의한 변수를 template 파일로 넘겨 사용하는 것

- 변수명은 영어, 숫자와 밑줄의 조합, 밑줄로 시작할 수 없다.
- 공백이나 구두점 문자 사용 불가
- dot(.)을 사용하여 변수 속성에 접근할 수 있음
- render()의 세번째 인자로 {'key': value}와 같이 딕셔너리 형태로 넘겨주며 key가 template에서 사용 가능한 변수명이 됨

``` python
# intro > urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('pages/', include('pages.urls')),
]

# articles(APP) > urls.py
from django.urls import path
# 명시적 상대경로 표현
from . import views  # 현재 디렉토리가 view.py와 같은 위치인 article이라 .을 사용

urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('greeting/', views.greeting, name='greeting'),
    path('dinner/', views.dinner, name='dinner'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    # Variable routing, 동적라우팅: 주소 자체를 변수처럼 사용해서 동적으로 주소를 만드는 것
    path('hello/<str:name>/', views.hello),  # str은 기본값이라 생략가능, int는 생략불가  
]
```

```python
# articles > views.py
from django.shortcuts import render
import random

# Create your views here.
def index(request):  # view 함수 첫번째 인자는 반드시 request, main page이름은 index(관습)
    # render 함수의 첫번째 인자는 반드시 request
    return render(request, 'index.html')  # templates까지 django가 읽고 있기 때문에 'index.html'만 씀

# 템플릿의 경로들은 반드시 templates 폴더 안에 존재해야함


def greeting(request):
    foods = ['apple', 'banana', 'coconut',]
    info = {
        'name': 'Harry'
    }
    context = {
        'info': info,
        'foods': foods,
    }

    return render(request, 'greeting.html', context)


def hello(request, name):  # url의 동적변수 name(urls.py의 동적변수와 같아야함)이 들어감
    context = {
        'name': name,
    }
    return render(request, 'hello.html', context)
```

```django
{# articles > greeting.html #}
{% extends 'base.html' %}  {# 부모 template 주소 #}
{% block content %}
  <h1>안녕하세요, 저는 {{ info.name }} 입니다</h1>  {# 변수는 key로 접근 #}
  <p>제가 좋아하는 음식은 {{ foods }} </p>
  <p>{{ foods.0 }}을 가장 좋아합니다.</p>
{% endblock %}
```



##### Variable Routing

- url을 변수처럼, 동적 주소를 가짐

```python
# practice0309/var_route/뭐든지들어옴/
    # views.var_route(request, value='asdf')
    path('var_route/<value>/', views.var_route),  # default는 str, <int:value> => value는 int형으로 받음
    path('lotto/<value>', views.lotto),  # value는 str형, value = 회차
    path('lotto_sol/', views.lotto),
    # variable routing 변수 라우팅 => url을 변수처럼, 동적 주소
    # path('<int:movie_id>/', views.find_movie),
    
# domain/practice/lotto/953
```







#### Filters

`` {{ variable|filter }}``

- 표시할 변수를 수정할 때 사용
- 예시: `` {{ name|lower }}``  =  name 변수를 모두 소문자로 출력

```django
{% extends 'base.html' %}  {# 부모 template 주소 #}
{% block content %}
  <h1>오늘 저녁은 {{ pick }}!</h1>
  <p> {{ pick }}은 {{ pick|length }} </p> {# pick의 길이 filter#}
  <p>메뉴판</p>
  {% comment %} 
    여러줄 주석은 이걸로 쓰는데 코드 옆에 쓰면 에러
  {% endcomment %}
  <ul>
    {% for food in foods %} {# tag #}
      <li>{{ food }}</li>  {# 변수 #}
    {% endfor %}
  </ul>
{% endblock %}
```



 #### Tag & Comments

`` {% tag %}``

- 출력 텍스트를 만들거나 반복, 논리 수행하여 제어 흐름 만듦
- 일부 태그는 종료 태그 필요

```django
{% extends 'base.html' %}  {# 부모 template 주소 #}
{% block content %}  {# 블록 태그 #}
  <h1>오늘 저녁은 {{ pick }}!</h1>
  <p> {{ pick }}은 {{ pick|length }} </p>
  <p>메뉴판</p>
  {% comment %} 
    여러줄 주석은 이걸로 쓰는데 코드 옆에 쓰면 에러
  {% endcomment %}
  <ul>
    {% for food in foods %} {# tag 반복문 #}
      <li>{{ food }}</li>  {# 변수 #}
    {% endfor %}
  </ul>
  {# 아래는 여러줄 주석 #}
  {% comment %}
    <p>1</p>
    <p>2</p>
    <p>3</p>
  {% endcomment %}
{% endblock %}
```



#### 상속

- 표현(template)과 로직(view)분리
- 중복 배제
- base.html 사용 시 settings.py에서 TEMLPLATES DIRS 수정
- 'DIRS': [BASE_DIR / 'templates'],

`{% extends %}`

- 자식 템플릿이 부모 템플릿을 확장한다는 것을 알림
- 반드시 **템플릿 최상단**에 작성

`{% block %}`

- 하위 템플릿에서 재지정(override)할 수 있는 블록을 정의
- 하위 템플릿이 채울 공간

```django
{# intro > base.html(skelton) #}
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
  <title>Document</title>
</head>
<body>
  <nav class="navbar navbar-light bg-light">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Navbar</a>
    </div>
  </nav>
  <div class="container">
    {% block content %}  {# 자식 tag에 공간 내주기, 자식 templates에서 작성한 내용은 여기 작성됨, content는 블럭이름 #}
    {% endblock  %}
  </div>

  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>
</body>
</html>
```

```django
{% extends 'base.html' %}  {# 부모 template 주소 #}
{% block content %}
  <h1>오늘 저녁은 {{ pick }}!</h1>
  <p> {{ pick }}은 {{ pick|length }} </p>
  <p>메뉴판</p>
  {% comment %} 
    여러줄 주석은 이걸로 쓰는데 코드 옆에 쓰면 에러
  {% endcomment %}
  <ul>
    {% for food in foods %} {# tag #}
      <li>{{ food }}</li>  {# 변수 #}
    {% endfor %}
  </ul>
  {# 이것은 주석 #}
  {% comment %}
    <p>1</p>
    <p>2</p>
    <p>3</p>
  {% endcomment %}
{% endblock %}
```

```python
# intro > settings.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'firstpjt' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```



### HTML Form

```django
{% extends 'base.html' %}
{% block title %}
  ping
{% endblock title %}

{% block content %}
  <h1>ping</h1>

  {% comment %} 
    action => 수신인(목적지), url
    method => 공개 / 비공개 여부 => GET, POST, ...
    GET: 모든 데이터가 (URL)에 공개되어 전송, URL making, default
    POST: 데이터가 URL에 공개되지 않음

    input은 항상 form 안에 쓰기, label 꼭 붙이기 (label은 사람용)
  {% endcomment %}

  {# (현재도메인)/practice0309/pong/ => 상대경로 #}
  {# 위에는 하드코딩, urls.py의 name을 활용하기, {% url 'name' %} #}
  {# 요청과 form에 있는 데이터가 urls.py의 pong으로 감 => views.pong => pong.html #}
  <form action="{% url 'practice0309:pong' %}" method="GET">  
    <label for="kr-name">한글이름</label>  {# label과 input을 for와 id로 연결 #}
    <input type="text" name="kr-name" id='kr-name'>  {# name = key, url에 담겨서 전송됨, name없어도 브라우저에는 남아있지만 데이터가 넘어가지 않음 #}

    <label for="en-name">English name</label>  
    <input type="text" name="en-name" id='en-name'>

    <input type="submit" value="전송">  {# value default는 제출, name없어도 됨 #}
  </form>
{% endblock content %}
```



#### HTML form element

- 웹에서 사용자 정보를입력하는 여러방식(button, text, password 등)을 제공

- 사용자로부터 할당된 데이터를 서버로 전송하는 역할을 담당

- 핵심 속성

  - action: 입력 데이터가 전송될 URL 지정, 목적지
  - method: 입력 데이터 전달 방식 지정, GET, POST,...
  
  

#### HTML input element

- **name = key**, url에 담겨서 전송됨
- name 없으면 key가 없어 데이터 넘어가지 않음

- 사용자로부터 데이터를 입력 받기 위해 사용
- type 속성에 따라 동작 방식 달라짐
- 핵심 속성
  - name
  - 중복가능, 제출 시 name에 설정된 값 넘겨서 값을 가져올 수 있음
  - GET/POST 방식으로 서버에 전달하는 파라미터(name = key, value = value)로 `?key=value&key=value`형태로 전달

```python
# articles > urls.py
from django.urls import path
# 명시적 상대경로 표현
from . import views  # 현재 디렉토리가 view.py와 같은 위치인 article이라 .을 사용

urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('greeting/', views.greeting, name='greeting'),
    path('dinner/', views.dinner, name='dinner'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    # Variable routing, 동적라우팅: 주소 자체를 변수처럼 사용해서 동적으로 주소를 만드는 것
    path('hello/<str:name>/', views.hello),  # str은 기본값이라 생략가능, int는 생략불가  
]
```

```python
# articles > views.py
from django.shortcuts import render
import random

# Create your views here.
def index(request):  # view 함수 첫번째 인자는 반드시 request, main page이름은 index(관습)
    # render 함수의 첫번째 인자는 반드시 request
    return render(request, 'index.html')  # templates까지 django가 읽고 있기 때문에 'index.html'만 씀

# 템플릿의 경로들은 반드시 templates 폴더 안에 존재해야함


def greeting(request):
    foods = ['apple', 'banana', 'coconut',]
    info = {
        'name': 'Harry'
    }
    context = {
        'info': info,
        'foods': foods,
    }

    return render(request, 'greeting.html', context)


def dinner(request):
    foods = ['족발', '피자', '햄버거', '초밥',]
    pick = random.choice(foods)
    context = {
        'pick': pick,
        'foods': foods
    }
    return render(request, 'dinner.html', context)


def throw(request):  # 데이터 받을 템플릿 출력
    return render(request, 'throw.html')


def catch(request):  # throw로 보낸 데이터 출력
    message = request.GET.get('message')  # QueryDict, key로 접근
    context = {
        'message': message,
    }
    return render(request, 'catch.html', context)


def hello(request, name):  # url의 동적변수 name(urls.py의 동적변수와 같아야함)이 들어감
    context = {
        'name': name,
    }
    return render(request, 'hello.html', context)
```



#### HTTP

- 웹에서 이루어지는 모든 데이터 교환의 기초
- 주어진 리소스가 수행할 원하는 작업을 나타내는 request methods 정의
- 종류
  - GET, POST, PUT, DELETE...
  - GET: 정보를 조회하는 데 사용, 데이터를 서버로 전송할 때 body가 아닌 Query String Parameters를 통해 전송



### URL

- 웹 어플리케이션은 URL을 통한 클라이언트의 요청에서부터 시작
- app이 늘어날수록 path()도 늘어나기 때문에 master project의 urls.py에서 모두 관리하는 것은 유지보수에 좋지 않음
- 각 app에 urls.py를 작성

```python
# intro > urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('pages/', include('pages.urls')),
]
```

```python
# articles > urls.py
urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('greeting/', views.greeting, name='greeting'),
    path('dinner/', views.dinner, name='dinner'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    # Variable routing, 동적라우팅: 주소 자체를 변수처럼 사용해서 동적으로 주소를 만드는 것
    path('hello/<str:name>/', views.hello),  # str은 기본값이라 생략가능, int는 생략불가  
]
```

```python
# pages > urls.py
from django.urls import path

urlpatterns = [  # 비어있더라도 urlpatterns = []는 있어야함

]
```



#### Naming URL patterns

- 링크에 url을 직접 적성하지 않고 path() 함수의 name 인자를 정의
- url Tag (`{% url '' %}`) 를 사용해 path()에서 작성한 name 사용

```python
# articles > urls.py
urlpatterns = [
    path('index/', views.index, name = 'index'),
]
```

``` python
# articles > index.html
{% extends 'base.html' %}  {# 부모 template 주소 #}
{% block content %}
  <h1>만나서 반가워요!</h1>
  <a href={% url 'greeting' %}>greeting</a>
  <a href={% url 'dinner' %}>dinner</a>
  <a href={% url 'throw' %}>throw</a>
{% endblock %}
```



### Namespace

- 이름공간은 객체를 구분할 수 있는 범위를 뜻함
- 하나의 이름 공간에서는 하나의 이름이 단 하나의 객체만 가리킴

- 서로 다른 app의 같은 이름을 가진 url name은 이름공간을 설정해서 구분
- templates, static 등 django는 정해진 경로 하나로 모아서 보기 때문에 중간에 폴더를 임의로 만들어 줌으로써 이름공간을 설정

#### URL namespace

- url에 이름공간을 설정해 어떤 app에 작성된 url name인지 알수 있음

``` python
app_name = 'articles'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index name='index'),
]
```

``` django
<a href="{% url 'articles:index' %}">메인 페이지</a>
```



#### Template namespace

- Django는 기본적으로 `app_name/templates/`경로에 있는 templates 파일들만 찾을 수 있음
- INSTALLED_APPS에 작성한 app 순서로 template 검색 후 렌더링
- 임의로 templates 폴더 구조를 `app_name/templates/app_name`형태로 변경해 임의로 이름 공간 생성 후 변경된 추가 경로로 수정

```python
def index(request):
    return render(request, 'articles/index.html')
```






### 1. urls.py

### 2. views.py

### 3. models.py

