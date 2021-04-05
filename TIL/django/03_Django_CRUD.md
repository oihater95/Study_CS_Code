[TOC]

# 03. Django_CRUD

**템플릿 폴더 구조 및 url 분리**

- `articles/urls.py` 파일 생성

- 프로젝트 폴더 url 설정


<br>

**`base.html` 설정**

```django
<!-- crud/templates/base.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <!-- Bootstrap CDN -->
</head>
<body>
  <div class="container">
    {% block content %}
    {% endblock %}
  </div>
  <!-- Bootstrap CDN -->
</body>
</html>
```

```python
# crud/settings.py

'DIRS': [BASE_DIR / 'crud' / 'templates'],
```

<br>

**기본 페이지 설정**

```python
# articles/urls.py

from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
]


# articles/views.py

def index(request):
    return render(request, 'articles/index.html')
```

```django
<!-- templates/articles/index.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>Articles</h1>
{% endblock %}
```

<br>

---

<br>

## READ

- 게시글 전체 조회

```python
# articles/views.py

from .models import Article

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)
```

```django
<!--templates/articles/index.html-->

{% extends 'base.html' %}

{% block content %}
  <h1>Articles</h1>
  <hr>
  {% for article in articles %}
    <p>글 번호: {{ article.pk }}</p>
    <p>글 제목: {{ article.title }}</p>
    <p>글 내용: {{ article.content }}</p>
    <hr>
  {% endfor %}
{% endblock %}
```

<br>

---

<br>

## CREATE

### New

```python
# articles/urls.py

path('new/', views.new, name='new'),
```

```python
# articles/views.py

def new(request):
    return render(request, 'articles/new.html')
```

```django
<!-- templates/articles/new.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>NEW</h1>
  <form action="#" method="GET">
    <label for="title">Title: </label>
    <input type="text" name="title"><br>
    <label for="content">Content: </label>
    <textarea name="content" cols="30" rows="5"></textarea><br>
    <input type="submit">
  </form>
  <hr>
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock %}
```

```django
<!-- templates/articles/index.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>Articles</h1>
  <a href="{% url 'articles:new' %}">[new]</a>
  <hr>
{% endblock  %}
```

<br>

### Create

```python
# article/urls.py

path('create/', views.create, name='create'),
```

```python
def create(request):
    title = request.GET.get('title') 
    content = request.GET.get('content')
    
    article = Article(title=title, content=content)
    article.save()
    
    return render(request, 'articles/create.html')
```

```django
<!-- templates/articles/create.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>성공적으로 글이 작성되었습니다.</h1>
{% endblock %}
```

```django
<!-- templates/articles/index.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>NEW</h1>
  <form action="{% url 'articles:create' %}" method="GET">
    <label for="title">Title: </label>
    <input type="text" name="title"><br>
    <label for="content">Content: </label>
    <textarea name="content" cols="30" rows="5"></textarea><br>
    <input type="submit">
  </form>
  <hr>
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock %}
```

<br>

**게시글 정렬 순서 변경**

- `#1` - DB로 부터 받은 쿼리셋을 이후에 파이썬이 변경 (Python이 조작)
- `#2`-  처음부터 내림차순 쿼리셋으로 받음 (DB가 조작)

```python
# articles/views.py

def index(request):
    # 1. articles = Article.objects.all()[::-1]
    # 2. articles = Artile.objects.order_by('-pk')  
```

<br>

---

<br>

### Http Method - POST

> https://developer.mozilla.org/ko/docs/Web/HTTP/Methods/POST

- **3가지 이유에서 우리는 글을 작성할 때 GET 요청이 아닌 POST 요청을 해야 한다.**
1. 사용자는 Django에게 '**HTML 파일 줘(GET)**' 가 아니라 '**~한 레코드(글)을 생성해(POST)**' 이기 때문에 GET보다는 POST 요청이 맞다.
  
2. 데이터는 URL에 직접 노출되면 안된다. (우리가 주소창으로 접근하는 방식은 모두 GET 요청) query의 형태를 통해 DB schema를 유추할 수 있다.
  
3. 모델(DB)을 건드리는 친구는 GET이 아닌 POST 요청! 왜? 중요하니까 **최소한의 신원 확인**이 필요하다!


<br>

**POST**

- 서버로 데이터를 전송할 때 사용
- 서버에 변경사항을 만듦
  - 때문에 요청자에 대한 최소한의 검증을 하지 않으면 부작용을 일으킬 수 있음
  - `csrf_token`을 통해서 요청자의 최소한의 신원확인
- 리소스를 생성/변경하기 위해 데이터를 HTTP body에 담아 전송
- CRUD에서 C/U/D 역할을 담당

<br>

**`GET`**

- 특정 리소스를 가져오도록 요청할 때 사용
- 반드시 데이터를 가져올 때만 사용해야 함
- DB에 변화를 주지 않음
- CRUD에서 R 역할을 담당

<br>

**DB 조작(GET/POST)**

- GET 요청은 DB에서 데이터를 꺼내서 가져온다. 즉, DB에 변화를 주는 게 아니다.
  - 즉, **GET**은 누가 요청해도 어차피 정보를 조회(HTML 파일을 얻는 것)하기 때문에 문제가 되지 않음.
- POST 요청은 DB에 조작(생성/수정/삭제)를 하는 것(디비에 변화를 준다)
  - **POST**는 DB에 조작이 가해지기 때문에 요청자에 대한 최소한의 검증을 하지 않으면 아무나 DB에 접근해서 데이터에 조작을 가할 수 있다.
  - `csrf_token`을 통해서 요청자의 최소한의 신원확인을 한다.

<br>

**`new.html` 수정**

```django
<!-- templates/articles/new.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>NEW</h1>
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    <label for="title">Title: </label>
    <input type="text" name="title"><br>
    <label for="content">Content: </label>
    <textarea name="content" cols="30" rows="5"></textarea><br>
    <input type="submit">
  </form>
  <hr>
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock %}
```

```python
# articles/views.py

def create(request):
    title = request.POST.get('title') 
    content = request.POST.get('content') 

    article = Article(title=title, content=content)
    article.save()
    return render(request, 'articles/index.html')
```

<br>

**CSRF Token**

> [https://ko.wikipedia.org/wiki/%EC%82%AC%EC%9D%B4%ED%8A%B8_%EA%B0%84_%EC%9A%94%EC%B2%AD_%EC%9C%84%EC%A1%B0](https://ko.wikipedia.org/wiki/사이트_간_요청_위조)

- 사이트 간 요청 위조(Cross-Site-Request-Fogery)

  - 웹 애플리케이션 취약점 중 하나로 **사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹페이지를 보안에 취약하게 한다거나 수정, 삭제 등의 작업을 하게 만드는 공격 방법**을 의미한다.
  - `{% csrf_token %}` 을 설정하면 input type hidden 으로 특정한 hash 값이 들어있다.

- `{% csrf_token %}` 이 없다면?
- `403 forbidden` 에러: 서버에 요청은 도달했으나 서버가 접근을 거부할 때 반환하는 HTTP 응답 코드 / 오류 코드. 서버 자체 또는 서버에 있는 파일에 접근할 권한이 없을 경우에 발생
  - 이러한 접근을 할 수 있도록 하는 것이 `{% csrf_token %}` → 사내 인트라넷 서버를 사내가 아닌 밖에서 접속하려고 할 때도 해당 HTTP 응답 코드가 뜬다.
  

<br>

**게시글 작성 후 index로 되돌리기**

```python
# articles/views.py

def create(request):
    ...
    return render(request, 'articles/index.html')
```

- 문제점 발생
  1. 글을 작성 후 index 페이지가 출력되지만 게시글이 조회되지 않음
  2. URL은 여전이 create에 머물러 있음
     - 단순히 index 페이지만 render 되었을 뿐이고 url이 돌아가지 못했기 때문

<br>

---

<br>

### Redirect

> Django shortcut function 중 하나이며 model, view name, absolute or relate URL을 인자로 받음
>
> 여기서 인자 view name은 URL pattern name으로 작성 될 수 있음

- POST 요청은 HTML 문서를 렌더링 하는 것이 아니라 **'~~ 좀 처리해줘(요청)'의 의미이기 때문에 요청을 처리하고 나서의 요청의 결과를 보기 위한 페이지로 바로 넘겨주는 것이 일반적**이다.

  ```python
  # articles/views.py
  
  from django.shortcuts import render, redirect
  
  
  def create(request):
      title = request.POST.get('title') 
      content = request.POST.get('content')
      
      article = Article(title=title, content=content)
      article.save()
      
      return redirect('articles:index')
  ```

<br>

**POST 요청으로 변경 후 변화하는 것**

- POST 요청을 하게 되면 form을 통해 전송한 데이터를 받을 때도 `request.POST.get()` 로 받아야 함
- 글이 작성되면 실제로 주소 창에 내가 넘긴 데이터가 나타나지 않는다. (POST 요청은 HTTP body에 데이터를 전송함)
- POST는 html을 요청하는 것이 아니기 때문에 html 파일을 받아볼 수 있는 곳으로 다시 redirect 한다.

<br>

---

<br>

## DETAIL

**urls 설정**

- 개별 게시글 상세 페이지
- 글의 번호(pk)를 활용해서 각각의 페이지를 따로 구현해야 함
- 무엇을 활용할 수 있을까? → Variable Routing

```python
# articles/urls.py

path('<int:pk>/', views.detail, name='detail'),
```

<br>

**views 설정**

```python
# articles/views.py

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)
```

<br>

**templates 설정**

```django
<!-- templates/articles/detail.html -->

{% extends 'base.html' %}

{% block content %}
  <h2>DETAIL</h2>
  <h3>{{ article.pk }} 번째 글</h3>
  <hr>
  <p>제목: {{ article.title }}</p>
  <p>내용: {{ article.content }}</p>
  <p>작성 시각: {{ article.created_at }}</p>
  <p>수정 시각: {{ article.updated_at }}</p>
  <hr>
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock  %}
```

-  index 페이지에 게시글별 detail 링크작성

  ```django
  <!-- templates/articles/index.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
  <h1 class="text-center">Articles</h1>
  <a href="{% url 'articles:new' %}">[new]</a>
  <hr>
  {% for article in articles %}
    <p>글 번호: {{ article.pk }}</p>
    <p>글 제목: {{ article.title }}</p>
    <p>글 내용: {{ article.content }}</p>
    **<a href="{% url 'articles:detail' article.pk %}">[detail]</a>**
    <hr>
  {% endfor %}
  {% endblock  %}
  ```

<br>

**create 후 detail로 이동**

```python
# articles/views.py

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article(title=title, content=content)
    article.save()
    
    return redirect('articles:detail', article.pk)
```

<br>

------

<br>

## DELETE

**urls 설정**

```python
# articles/urls.py

path('<int:pk>/delete/', views.delete, name='delete'),
```

<br>

**views 설정**

```python
# articles/views.py

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')
```

<br>

**templates 설정**

```django
<!-- articles/detail.html -->

{% extends 'base.html' %}

{% block content %}
  ...
  <form action="{% url 'articles:delete' article.pk %}" method="POST">
    {% csrf_token %}
    <button class="btn btn-danger">DELETE</button>
  </form><br>
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock %}
```

- 그래서 POST 로 요청을 받기 위해 다음과 같이 조건을 만든다.

  ```python
  # articles/views.py
  
  def delete(request, pk):
      article = Article.objects.get(pk=pk)
      if request.method == 'POST':
          article.delete()
          return redirect('articles:index')
      else:
          return redirect('articles:detail', article.pk)
  ```

<br>

---

<br>

## UPDATE

### Edit

**urls 설정**

```python
# articles/urls.py

path('<int:pk>/edit/', views.delete, name='edit'),
```

<br>

**views 설정**

```python
# articles/views.py

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)
```

<br>

**templates 설정**

- 수정은 기존에 입력 되어 있던 데이터를 보여주는 것이 좋기 때문에 html 태그의 `value` 속성을 사용

```django
<!-- articles/edit.html -->

{% extends 'base.html' %}

{% block content %}
  <h1 class="text-center">EDIT</h1>
  <form action="#" method="POST">
    {% csrf_token %}
    <label for="title">Title: </label>
    <input type="text" name="title" value="{{ article.title }}"><br>
    <label for="content">Content: </label>
    <textarea name="content" cols="30" rows="5">{{ article.content }}</textarea><br>
    <input type="submit">
  </form>
  <hr>
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock %}
```

- `detail.html` 에 edit 으로 가는 링크 작성

  ```django
  <!-- articles/detail.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
    ...
    <a href="{% url 'articles:edit' article.pk %}" class="btn btn-primary">EDIT</a><br>
    <form action="{% url 'articles:delete' article.pk %}" method="POST">
      {% csrf_token %}
      <button class="btn btn-danger">DELETE</button>
    </form><br>
    <a href="{% url 'articles:detail' article.pk %}">[back]</a>
  {% endblock  %}
  ```

<br>

### Update

**urls 설정**

```python
# articles/urls.py

path('<int:pk>/update/', views.update, name='update'),
```

<br>

**views 설정**

```python
# articles/views.py

def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)
```

```django
<!-- articles/edit.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>EDIT</h1>
  <form action="{% url 'articles:update' article.pk %}" method="POST">
    {% csrf_token %}
    ...
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock %}
```
