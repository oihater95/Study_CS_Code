[TOC]

# 05. Django_Static

## Static files

> 웹 사이트의 구성 요소 중에서 image, css, js 파일과 같이 해당 내용이 고정되어 응답을 할 때 별도의 처리 없이 파일 내용을 그대로 보여주면 되는 파일
>
> https://docs.djangoproject.com/en/3.1/howto/static-files/#managing-static-files-e-g-images-javascript-css

<br>

### Static files 구성

1. django.contrib.staticfiles 앱이 `INSTALLED_APPS`에 있는지 확인
2. setting.py에 `STATIC_URL` 정의
3. 템플릿에서 static 템플릿 태그를 사용하여 static file이 있는 상대경로를 빌드
4. 앱에 static file 저장하기 (`my_app/static/my_app/sample.jpg`)

<br>

```django
<!-- articles/index.html -->

{% extends 'base.html' %}
{% load static %}

{% block content %}
  <img src="{% static 'articles/images/sample.png' %}" alt="sample">
  ...
{% endblock %}
```

- 이미지 파일 위치 - `articles/static/articles/images/`
- static file 기본 경로
  - `app_name/static/`

<br>

### The staticfiles app

> https://docs.djangoproject.com/en/3.1/ref/contrib/staticfiles/#module-django.contrib.staticfiles

**`STATIC_ROOT`**

- Django 프로젝트에서 사용하는 모든 정적 파일을 한 곳에 모아넣는 경로

- collectstatic이 배포를 위해 정적파일을 수집하는 절대 경로
- DEBUG=True(개발 단계)로 설정되어 있으면 작용하지 않음
- 개발단계에서는 경로를 작성하지 않아도 문제없이 동작
- 즉, 실제 서비스 배포 환경에서 필요한 경로

> [참고]
>
> **collectstatic**
>
> - 프로젝트 배포 시 흩어져있는 정적 파일들을 모아 특정 디렉토리로 옮기는 작업
>
> ```python
> # settings.py 예시
> 
> STATIC_ROOT = BASE_DIR / 'staticfiles'
> ```
>
> ```bash
> $ python manage.py collectstatic
> ```

<br>

**`STATIC_URL`**

- `STATIC_ROOT`에 있는 정적파일을 참조 할 때 사용할 URL
  - 실제 파일이나 디렉토리가 아니며, URL로만 존재
- 비어 있지 않은 값으로 설정 한다면 반드시 slash(/)로 끝나야 함

<br>

**`STATICFILES_DIRS`**

- app내의 static 디렉토리 경로를 사용하는 것(기본 경로) 외에 추가적인 정적 파일 경로 정의

  ```django
  <!-- base.html -->
  
  <head>
    {% block css %}{% endblock %}
  </head>
  ```

  ```python
  # settings.py
  
  STATICFILES_DIRS = [
      BASE_DIR / 'crud' / 'static',
  ]
  ```

  ```django
  <!-- articles/index.html -->
  
  {% extends 'base.html' %}
  {% load static %}
  
  {% block css %}
    <link rel="stylesheet" href="{% static 'stylesheets/style.css' %}">
  {% endblock %}
  ```

  ```css
  /* crud/static/stylesheets/style.css */
  
  h1 {
      color: crimson;
  }
  ```


<br>

**STATIC_URL 확인해보기**

![1](04_django_staticfiles.assets/1.jpg)



- 개발자도구 - 네트워크 - 이미지파일 선택 - Request URL 확인

<br>

---

<br>

## Media

> 사용자가 웹에서 업로드하는 정적 파일
>
> 즉, 유저가 업로드 한 모든 정적 파일

<br>

### 이미지 업로드

> https://docs.djangoproject.com/ko/3.1/ref/models/fields/#filefield

<br>

**`FileField` / `ImageField` 를 사용하기 위한 몇 가지 단계**

1. setting.py에 `MEDIA_ROOT`, `MEDIA_URL` 설정
2. `upload_to` 속성을 정의하여 업로드 된 파일에 사용할 `MEDIA_ROOT`의 하위 경로를 지정
   - upload_to는 optional argument
3. 업로드 된 파일의 상대 URL은 django가 제공하는 `url` 속성을 통해 얻을 수 있음

<br>

**`MEDIA_ROOT`**

- 사용자가 업로드 한 파일(미디어 파일)들을 보관할 디렉토리의 절대 경로
- django는 성능을 위해 업로드 파일은 데이터베이스에 저장하지 않음
  - **데이터베이스에 저장되는 것은 파일 경로**
- `MEDIA_ROOT`는 `STATIC_ROOT`와 다른 경로로 지정을 해야 함

```python
# settings.py

MEDIA_ROOT = BASE_DIR / 'media'
```

<br>

**`MEDIA_URL `**

- 업로드 된 파일의 주소(URL)를 만들어 주는 역할

  - 웹 서버 사용자가 사용하는 public URL

- 비어 있지 않은 값으로 설정 한다면 반드시 slash(/)로 끝나야 함

- `MEDIA_URL`도 `STATIC_URL`과 경로가 달라야 함

  ```python
  # settings.py
  
  MEDIA_URL = '/media/' 
  ```

<br>

**개발 단계에서 사용자가 업로드한 미디어 파일 제공하기**

> https://docs.djangoproject.com/en/3.1/howto/static-files/#serving-files-uploaded-by-a-user-during-development

```python
# crud/urls.py

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 업로드 된 파일의 URL == settings.MEDIA_URL
# 위 URL을 통해 참조하는 파일의 실제 위치 == settings.MEDIA_ROOT
```

<br>

### CREATE

**ImageField**

```python
# views.py

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

> 기존 컬럼 코드 사이에 작성해도 실제 테이블에 추가 될 때는 가장 우측(뒤)에 추가됨

```bash
$ pip install Pillow
```

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br>

**`blank` - model field option**

> https://docs.djangoproject.com/en/3.1/ref/models/fields/#blank

- True일 경우 해당 field는 blank(빈 값)를 허용
- 데이터베이스에는 `''` (빈 문자열)이 저장됨
- 유효성 검사와 관련이 있음

<br>

```django
<!-- create.html -->

<form action="" method="POST" enctype="multipart/form-data">
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit">
</form>
```

```python
# views.py

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        # form = ArticleForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            article.save()
            return redirect('articles:detail', article.pk)
    else: 
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
```

<br>

form 태그 - `enctype(인코딩)` **속성**

1. `apllication/x-www-form-urlencoded`
   - (기본값) 모든 문자 인코딩
2. `multipart/form-data`
   - 파일/이미지 업로드 시에 반드시 사용해야 함 (전송되는 데이터의 형식을 지정)
   - `<input type="file">`을 사용할 경우 사용
3. `text/plain`

<br>

input 태그 - `accept` 속성

- 입력 허용할 파일 유형을 나타내는 문자열
- 이 문자열은 쉼표로 구분된 고유 파일 유형 지정자(unique file type specifiers)
- 하지만 파일 검증은 하지 못함 (이미지만 accept 해 놓더라도 비디오나 오디오 파일을 제출할 수 있음)

<br>

### READ

```django
<!-- detail.html -->

{% extends 'base.html' %}

{% block content %}
  <h2 class='text-center'>DETAIL</h2>
  <h3>{{ article.pk }} 번 글</h3>
  <img src="{{ article.image.url }}" alt="{{ article.image }}">
  <hr>
  ...
{% endblock %}
```

- `article.image.url`
  - 업로드 파일의 상대 URL
- `article.image`
  - 업로드 파일의 파일 이름

<br>

**MEDIA_URL 확인해보기**

![2](04_django_staticfiles.assets/2.jpg)

<br>

### UPDATE

- 이미지는 바이너리 데이터(하나의 덩어리)이기 때문에 텍스트처럼 일부만 수정 하는 것은 불가능
- 때문에 새로운 사진으로 덮어 씌우는 방식을 사용

```django
<!-- update.html -->

{% block content %}
  <h1 class="text-center">UPDATE</h1>
  <form action="" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
  <hr>
  <a href="{% url 'articles:detail' article.pk %}">[back]</a>
{% endblock %}
```

```python
# views.py

@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)
```

<br>

- 이미지 필드 설정 이전에 작성되었던 과거 게시물들 + 새로운 게시글 작성시 이미지 없이 작성하는 게시물의 detail 페이지를 출력하지 못하는 문제 해결 (image 필드 값이 없기 때문)

```django
<!-- detail.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>DETAIL</h1>
  <h2>{{ article.pk }} 번 글</h2>
  {% if article.image %}
    <img src="{{ article.image.url }}" alt="{{ article.image }}">
  {% endif %}
...
```

