[TOC]

# 04. Django_Form

> Django 프로젝트의 주요 유효성 검사 도구들 중 하나이며, 공격 및 데이터 손상에 대한 중요한 방어 수단이다.

<br>

## Django's role in forms

Django는 forms에 관련된 작업의 세 부분을 처리한다.

1. 렌더링을 위한 데이터 준비 및 재구성
2. 데이터에 대한 HTML forms 생성
3. 클라이언트로 부터 받은 데이터 수신 및 처리

이 모든 작업을 수동으로 수행하는 코드를 작성할 수 있지만 Django가 모든 작업을 처리 할 수 있다.

<br>

## Form Class

> https://docs.djangoproject.com/ko/3.1/topics/forms/#working-with-forms

- Django form 관리 시스템의 핵심이다. 
- form내 field들, field 배치, 디스플레이 widget, label, 초기값, 유효한 값과 (유효성 체크이후에) 비유효 field에 관련된 에러메시지를 결정한다.

<br>

**Form 선언**

- view까지 작성해서 템플릿에서 출력까지 확인
```python
# articles/forms.py

from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField(widget=forms.Textarea)
```

```python
# articles/views.py
  
from .forms import ArticleForm
  
  
def new(request):
    form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
```

````django
<!-- articles/new.html -->
  
{% extends 'base.html' %}
  
{% block content %}
    <h1>NEW</h1>
    <form action="{% url 'articles:create' %}" method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit">
    </form>
    <hr>
    <a href="{% url 'articles:index' %}">[back]</a>
{% endblock %}
````

  - 개발자 도구로 만들어진 input 태그 확인해보자.

<br>

**Outputting forms as HTML**

> https://docs.djangoproject.com/ko/3.1/ref/forms/api/#outputting-forms-as-html

- `as_p()` : 각 필드가 단락(paragraph)으로 렌더링
- `as_ul()` : 각 필드가 목록항목(list item)으로 렌더링
- `as_table()` : 각 필드가 테이블 행으로 렌더링

<br>

**Django의 HTML input 요소 표현 2가지**

1. Form fields
   - 입력에 대한 유효성 검사 로직을 처리하며 템플릿에서 직접 사용됨
2. Widgets
   - 웹 페이지의 HTML 양식 입력 요소 렌더링 및 제출 된 원시 데이터 추출을 처리
   - 위젯은 반드시 form fields에 할당 됨

<br>

### Form fields

> https://docs.djangoproject.com/en/3.1/ref/forms/fields/#module-django.forms.fields
>
> https://docs.djangoproject.com/en/3.1/internals/contributing/writing-code/coding-style/#model-style

```python
class ArticleForm(forms.Form):
    REGION_A = 'sl'
    REGION_B = 'dj'
    REGION_C = 'gj'
    REGION_D = 'gm'
    REGIONS_CHOICES = [
        (REGION_A, '서울'),
        (REGION_B, '대전'),
        (REGION_C, '광주'),
        (REGION_D, '구미'),
    ]
    title = forms.CharField(max_length=10)
    content = forms.CharField(widget=forms.Textarea)
    region = forms.ChoiceField(choices=REGIONS_CHOICES, widget=forms.RadioSelect())
```

<br>

---

<br>

## ModelForm

> https://docs.djangoproject.com/en/3.1/topics/forms/modelforms/#creating-forms-from-models

- Django에서는 model을 통해 Form Class를 만들수 있는 Helper(도우미)를 제공한다.

  - ModelForm Helper 클래스를 사용하여 모델에서 form을 작성
  - ModelForm은 일반 Form과 완전히 같은 방식(객체생성)으로 view에서 사용할 수 있다.

  ```python
  # articles/forms.py
  
  from django import forms
  from .models import Article
  
  # class ArticleForm(forms.Form):
  #     title = forms.CharField(max_length=10)
  #     content = forms.CharField(widget=forms.Textarea)
  
  class ArticleForm(forms.ModelForm):
      
      class Meta:
          model = Article
          fields = '__all__'
          # exclude = ('title',)
  ```

  - `new.html` 변화 확인

<br>

### CREATE

```python
# articles/views.py

def create(request):
    form = ArticleForm(request.POST) 
    if form.is_valid():
        article = form.save()
        return redirect('articles:detail', article.pk)
    return redirect('articles:new')
```

<br>

**The `save()` method**

> https://docs.djangoproject.com/ko/3.1/topics/forms/modelforms/#the-save-method

<br>

### Change view structure

> https://docs.djangoproject.com/en/3.1/topics/forms/#the-view

```python
# articles/forms.py

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST) 
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
```

>  new.html → `create.html` 이름변경

```django
<!-- articles/create.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>CREATE</h1>
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
  <hr>
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock %}
```

- input 태그에 공백 데이터를 넣어보고 제출 후 에러 메세지 확인

<br>

### Widgets

> https://docs.djangoproject.com/en/3.1/ref/forms/widgets/#module-django.forms.widgets

```python
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title', 
                'placeholder': 'Enter the title',
                'maxlength': 10,
            }
        ),
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,
            }
        ),
        error_messages={
            'required': 'Please enter your content'
        }
    )
    
    class Meta:
        model = Article
        fields = '__all__'
```

<br>

**Form과 ModelForm의 핵심 차이점**

- Form
  - 어떤 모델에 저장해야 하는지 알 수 없기 때문에 유효성 검사를 하고 실제로 DB에 저장할 때는  `cleaned_data` 와 `article = Article(title=title, content=content)` 를 사용해서 따로 `.save()` 를 해야 한다.
  - Form Class가 `cleaned_data` 로 딕셔너리로 만들어서 제공해 주고, 우리는 `.get` 으로 가져와서 Article 을 만드는데 사용한다.
- ModelForm
  - django 가 해당 모델에서 양식에 필요한 대부분의 정보를 이미 정의한다.
  - `forms.py` 에 Meta 정보로 `models.py` 에 이미 정의한  Article 을 넘겼기 때문에 어떤 모델에 레코드를 만들어야 할지 알고 있어서 바로 `.save()` 가 가능하다.

<br>

### Update

> https://docs.djangoproject.com/ko/3.1/topics/forms/modelforms/#the-save-method

- 인자 `instance`는 **수정 대상이 되는 객체를 지정**한다.

- create 로직과 다른 점은 기존의 데이터를 가져와 수정을 한다는 점이다. 

  - `request.POST` : 사용자가 form을 통해 전송한 데이터
- `instance` : 수정이 되는 대상

```python
# articles/urls.py

path('<int:pk>/update/', views.update, name='update'),
```

```python
# articles/views.py

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        # Create a form to edit an existing Article,
        # but use POST data to populate the form.
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        # Creating a form to change an existing article.
        form = ArticleForm(instance=article)
    context = {
        'form': form,
    }
    return render(request, 'articles/update.html', context)
```

```django
<!-- articles/update.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>UPDATE</h1>
  <form action="{% url 'articles:update' article.pk %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
  <hr>
  <a href="{% url 'articles:detail' aritlce.pk %}">[back]</a>
{% endblock %}
```

```django
<!-- articles/detail.html -->

<a href="{% url 'articles:update' article.pk %}">UPDATE</a><br>
```

```python
# articles/views.py

def update(request, pk):
    ...
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)
```

<br>

### Delete

```python
# articles/urls.py

path('<int:pk>/delete/', views.delete, name='delete'),
```

```python
# articles/views.py

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    return redirect('articles:detail', article.pk)
```

```django
<!-- articles/detail.html -->

<form action="{% url 'articles:delete' article.pk %}" method="POST">
  {% csrf_token %}
  <input type="submit" value="DELETE">
</form>
```

<br>

**`forms.py`  위치**

- Form class는 `forms.py` 뿐만 아니라 다른 위치 어느 곳에 두어도 상관없다.
- 하지만 되도록 app 폴더에 두며, Form class는 `forms.py` 에 작성하는 것이 일반적이다.

<br>

------

<br>

## Rendering fields manually

> 다양한 방법으로 form 커스터마이징
>
> https://docs.djangoproject.com/ko/3.1/topics/forms/#rendering-fields-manually

<br>

### 수동으로 Form 작성

1. Rendering fields manually

   ```django
   <!-- articles/create.html --> 
   
   <h1>CREATE</h1>
   ...
   <hr>
   
   <form action="" method="POST">
     {% csrf_token %}
     <div>
       {{ form.title.errors }}
       {{ form.title.label_tag }}
       {{ form.title }}
     </div>
     <div>
       {{ form.content.errors }}
       {{ form.content.label_tag }}
       {{ form.content }}
     </div>
     <button class="btn btn-primary">작성</button>
   </form>
   ```

2. Looping over the form’s fields (`{% for %}`)

   ```django
   <!-- articles/create.html --> 
   
   ...
   
   <hr>
   
   <form action="" method="POST">
     {% csrf_token %}
     {% for field in form %}
       {{ field.errors }}
       {{ field.label_tag }}
       {{ field }}
     {% endfor %}
     <button class="btn btn-primary">작성</button>
   </form>
   ```

<br>

### Bootstrap Form

> https://getbootstrap.com/docs/5.0/forms/overview/

- `form-control` 

  ```django
  <!-- articles/create.html -->
  
  ...
  
  <hr>
  
  <h2>Bootstrap Form</h2>
  <form action="" method="POST">
    {% csrf_token %}
    {% for field in form %}
      <div class="mb-3">
        {{ field.errors }}
        {{ field.label_tag }} 
        {{ field }}
      </div>
    {% endfor %}
    <button class="btn btn-primary">작성</button>
  </form>
  ```

  ```python
  # articles/forms.py
  
  class ArticleForm(forms.ModelForm):
      title = forms.CharField(
          label='제목',
          widget=forms.TextInput(
              attrs={
                  'class': 'my-title form-control', 
                  'placeholder': 'Enter the title',
          }),
      )
      content = forms.CharField(
          label='내용',
          widget=forms.Textarea(
              attrs={
                  'class': 'my-content form-control',
                  'placeholder': 'Enter the content',
                  'rows': 5,
                  'cols': 50,
          }),
          error_messages={
              'required': '내용 넣어라...',
          }
      )
  ```

<br>

### Error message with Bootstrap

```django
<!-- articles/create.html -->

<form action="" method="POST">
  {% csrf_token %}
  {% for field in form %}
    {% if field.errors %}
      {% for error in field.errors %}
        <div class="alert alert-warning" role="alert">{{ error|escape }}</div>
      {% endfor %}
    {% endif %}
    <div class="form-group">
      {{ field.label_tag }} 
      {{ field }}
    </div>
  {% endfor %}
  <button class="btn btn-primary">작성</button>
</form>
```

<br>

---

<br>

## Django Bootstrap Library

### django-bootstrap5

> https://django-bootstrap-v5.readthedocs.io/en/latest/installation.html

```bash
$ pip install django-bootstrap-v5
```

```python
# settings.py

INSTALLED_APPS = [
  ...
  'bootstrap5',
   ...
]
```

```bash
$ pip freeze > requirements.txt
```

```django
<!-- articles/base.html -->

{% load bootstrap5 %}

<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  {% bootstrap_css %}
  <title>Document</title>
</head>
<body>
  <div class="container">
    {% block content %}
    {% endblock %}
  </div>
  {% bootstrap_javascript %}
</body>
</html>
```

```django
<!-- articles/update.html -->

{% extends 'base.html' %}
{% load bootstrap5 %}

{% block content %}
  ...
  <form action="" method="POST">
    {% csrf_token %}
    {% bootstrap_form form layout='horizontal' %}
    {% buttons submit="Submit" reset="Cancel" %}{% endbuttons %}
  </form>
  ...
  {% endif %}
{% endblock %}
```

<br>

---

<br>

## View decorators

> https://docs.djangoproject.com/en/3.1/topics/http/decorators/#module-django.views.decorators.http

<br>

**데코레이터(decorator)**

- 어떤 함수에 기능을 추가하고 싶을 때, 해당 함수를 수정하지 않고 기능을 `연장`하게 해주는 `함수`

- Django는 다양한 HTTP 기능을 지원하기 위해 뷰에 적용 할 수있는 여러 데코레이터를 제공

<br>

### Allowed HTTP methods

> 일치하지 않는 메서드 요청이라면 `405 Method Not Allowed` 에러를 발생

<br>

**`require_http_methods()`**

- view가 특정한 요청 method만 허용하도록하는 데코레이터

  ```python
  from django.views.decorators.http import require_http_methods, require_POST
  
  
  @require_http_methods(['GET', 'POST'])
  def create(request):
      pass
  
    
  @require_http_methods(['GET', 'POST'])
  def update(request, pk):
      pass
  ```

<br>

**`require_POST()`**

- view가 POST 메서드만 요청만 승인하도록 하는 데코레이터

  ```python
  from django.views.decorators.http import require_http_methods, require_POST
  
  
  @require_POST
  def delete(request, pk):
      article = Article.objects.get(pk=pk)
      article.delete()
      return redirect('articles:index')
  ```

  - url 로 delete 시도 후 405 에러페이지 & terminal 로그 확인하기
