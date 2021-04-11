[TOC]

# 09. Django_Model_Relationship M:N

> https://docs.djangoproject.com/en/3.1/ref/models/fields/#module-django.db.models.fields

## User - Article

```python
# articles/models.py

from django.conf import settings


class Article(models.Model)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ...
```

```bash
$ python manage.py makemigrations
```

```bash
# 첫번째 상황(null 값이 허용되지 않는 user_id 가 아무 값도 없이 article 에 추가되려 하기 때문)
$ python manage.py makemigrations
You are trying to add a non-nullable field 'user' to article without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option: # 1 입력하고 enter

# 두번째 상황(그럼 기존 article 의 user_id 로 어떤 데이터를 넣을건지 물어봄)
Please enter the default value now, as valid Python
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
>>> # 1 입력하고 enter (그럼 현재 작성된 모든 글은 1번 user가 작성한 것으로 됨)
```

```bash
$ python manage.py migrate
```

<br>

- 게시글을 작성하려 하면 user 를 선택 해야하는 불필요한 field 가 노출된다. 

- 제목과 내용만 입력하도록 필드를 설정해야한다.

  ```python
  # articles/forms.py
  
  class ArticleForm(forms.ModelForm):
      
      class Meta:
          model = Article
          fields = ('title', 'content',)
  ```

  - 글을 작성해보면 create 시에 유저 정보가 저장되지 않기 때문에 다음과 같은 에러가 발생한다.
    - `NOT NULL constraint failed: articles_article.user_id`

<br>

### CREATE

- `request.user` 라는 현재 요청의 유저 객체를 추가로 저장한다.

  ```python
  # articles/views.py
  
  @login_required
  @require_http_methods(['GET', 'POST'])
  def create(request):
      if request.method == 'POST':
          form = ArticleForm(request.POST)
          if form.is_valid():
              article = form.save(commit=False)
              article.user = request.user
              article.save()
              return redirect('articles:detail', article.pk)
  ```

<br>

### READ

- 게시글을 작성한 user가 누구인지 보기 위해 `index.html` 수정

  ```django
  <!-- articles/index.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
    ...
    {% for article in articles %}
      <p><b>작성자 : {{ article.user }}</b></p>
      <p>글 번호 : {{ article.pk }}</p>
      <p>글 제목 : {{ article.title }}</p>
      <p>글 내용 : {{ article.content }}</p>
      <a href="{% url 'articles:detail' article.pk %}">DETAIL</a>
      <hr>
    {% endfor %}
  {% endblock %}
  ```

<br>

### UPDATE

- 사용자가 자신의 글만 수정 할 수 있도록 수정

  ```python
  # articles/views.py
  
  
  @login_required
  @require_http_methods(['GET', 'POST'])
  def update(request, pk):
      article = get_object_or_404(Article, pk=pk)
      if request.user == article.user:
          if request.method == 'POST':
              form = ArticleForm(request.POST, instance=article)
              if form.is_valid():
                  form.save()
                  return redirect('articles:detail', article.pk)
          else:
              form = ArticleForm(instance=article)
      else:
          return redirect('articles:index')
      context = {
          'form': form,
      }
      return render(request, 'articles/update.html', context)
  ```


<br>

### DELETE

- 사용자가 자신의 글만 삭제 할 수 있도록 수정

```python
# articles/views.py

@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user.is_authenticated:
        if request.user == article.user:
            article.delete()
            return redirect('articles:index')
    return redirect('articles:detail', article.pk)
```

- 해당 게시글의 작성가 아니라면, 수정/삭제 버튼을 출력하지 않도록 수정

```django
<!-- articles/detail.html -->

{% extends 'base.html' %}
{% block content %}
  ...
  {% if request.user == article.user %}
    <a href="{% url 'articles:update' article.pk %}" class="btn btn-primary">[UPDATE]</a>
    <form action="{% url 'articles:delete' article.pk %}" method="POST">
      {% csrf_token %}
      <button class="btn btn-danger">DELETE</button>
    </form>
  {% endif %}
...
```

<br>

---

<br>

## User - Comment

```python
# articles/models.py

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ...
```

```bash
$ python manage.py makemigrations

# 첫번째 상황(null 값이 허용되지 않는 user_id 가 아무 값도 없이 comment 에 추가되려 하기 때문)
You are trying to add a non-nullable field 'user' to comment without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option: # 1 입력하고 enter

# 두번째 상황 (그럼 기존 comment 의 user_id 로 뭘 넣을건지 물어봄)
Please enter the default value now, as valid Python
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
>>> # 1 입력하고 enter (모든 댓글의 작성자를 1번 user로 하게 됨)

Migrations for 'articles':
  articles\migrations\0003_comment_user.py
    - Add field user to comment
```

```bash
$ python manage.py migrate
```

<br>

### CREATE

- 해당 view 함수를 요청한 유저의 정보를 넣고나서 저장한다. (로그인 사용자만 작성하도록)

  ```python
  # articles/views.py
  
  @require_POST
  def comments_create(request, pk):
      if request.user.is_authenticated:
          article = get_object_or_404(Article, pk=pk)
          comment_form = CommentForm(request.POST)
          if comment_form.is_valid():
              comment = comment_form.save(commit=False)
              comment.article = article
              comment.user = request.user
              comment.save()
              return redirect('articles:detail', article.pk)
          ...
  ```

<br>

### READ

- 비로그인 유저는 댓글 작성 form 을 볼 수 없도록 한다.

  ```django
  <!-- articles/detail.html -->
  
  {% extends 'base.html' %}
  {% block content %}
    ...
  <hr>
    {% if request.user.is_authenticated %}
      <form action="{% url 'articles:comments_create' article.pk %}" method="POST">
        {% csrf_token %}
        {{ comment_form }}
        <input type="submit">
      </form>
    {% else %}
      <a href="{% url 'accounts:login' %}">[댓글을 작성하려면 로그인하세요.]</a>
    {% endif %}
  {% endblock  %}
  ```
  
```python
  # articles/forms.py
  
  class CommentForm(forms.ModelForm):
  
      class Meta:
          model = Comment
          exclude = ('article', 'user',)
```

- 댓글 작성자 출력

  ```django
  <!-- articles/detail.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
    ...
    <h4>댓글 목록</h4>
    ...
    <ul>
      {% for comment in comments %}
        <li>
          {{ comment.user }} - {{ comment.content }}
          <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST" class="d-inline">
            {% csrf_token %}
            <input type="submit" value="DELETE">
          </form>
        </li>
      {% empty %}
        <p>아직 댓글이 없네요...</p>
      {% endfor %}
    </ul>
    <hr>
    ...
  {% endblock %}
  ```

<br>

### DELETE

- 본인이 작성한 댓글만 삭제할 수 있도록 수정한다.

  ```python
  # articles/views.py
  
  @require_POST
  def comments_delete(request, article_pk, comment_pk):
      if request.user.is_authenticated:
          comment = get_object_or_404(Comment, pk=comment_pk)
          if request.user == comment.user:
              comment.delete()
      return redirect('articles:detail', article_pk)
  ```

  ```django
  <!-- articles/detail.html -->
  
  {% extends 'articles/base.html' %}
  {% block content %}
    ...
    <h4>댓글 목록</h4>
    ...
    <ul>
      {% for comment in comments %}
        <li>
          {{ comment.user }} - {{ comment.content }}
          {% if request.user == comment.user %}
            <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST" class="d-inline">
              {% csrf_token %}
              <input type="submit" value="DELETE">
            </form>
          {% endif %}
        </li>
      {% empty %}
        <p>아직 댓글이 없네요...</p>
      {% endfor %}
    </ul>
    <hr>
    ...
  {% endblock %}
  ```

  - 본인 댓글에 대한 삭제 버튼을 볼 수 있도록 수정한다.



# 

## ManyToManyField

> https://docs.djangoproject.com/en/3.1/ref/models/fields/#manytomanyfield

- M:N(이하 다대다) 관계를 나타내기 위해 사용하는 필드

- 하나의 필수 위치인자(다대다 관계로 설정할 모델 클래스)가 필요하다.

<br>

**Arguments**

- `related_name`

  - ForeignKey의 related_name과 동일

- `through`

  - django는 다대다 관계를 관리하는 중개 테이블을 자동으로 생성한다.
  - 하지만, 중간 테이블을 직접 지정하려면 through 옵션을 사용하여 중개 테이블을 나타내는 Django 모델을 지정할 수 있다.
  - 일반적으로 추가 데이터를 다 대다 관계와 연결하려는 경우(extra data with a many-to-many relationship)에 사용

- `symmetrical`

  - ManyToManyField가 동일한 모델을 가리키는 정의에서만 사용

  ```python
  from django.db import models
  
  class Person(models.Model):
      friends = models.ManyToManyField('self')
  ```

  - 예시처럼 동일한 모델을 가리키는 정의의 경우 django는 Person 클래스에 person_set 매니저를 추가 하지 않는다.
  - 대신 대칭적(`symmetrical`)이라고 간주하며, source 인스턴스가 target 인스턴스를 참조하면 target 인스턴스도 source 인스턴스를 참조하게 된다.
  - 즉, 내가 당신의 친구라면 당신도 내 친구가 된다.
  - self와의 관계에서 대칭을 원하지 않는 경우 `symmetrical=False`로 설정한다.

<br>

**Related manager**

- 1:N 또는 M:N 관련 컨텍스트에서 사용되는 매니저
- 같은 이름의 메서드여도 각 관계(1:N, M:N)에 따라 다르게 사용 및 동작
  - 1:N에서는 target 모델 객체만 사용 가능
  - M:N 관계에서는 관련된 두 객체에서 모두 사용 가능

<br>

**methods**

- `add()`
  - "지정된 객체를 관련 객체 집합에 추가"
  - 이미 존재하는 관계에 add()를 사용하면 관계가 복제되지 않음
- `remove()`
  - "관련 객체 집합에서 지정된 모델 개체를 제거"
  - QuerySet.delete()를 사용하여 관계가 삭제됨
- clear(), set(), create()

<br>

**데이터베이스에서의 표현**

- django는 다대다 관계를 나타내는 중개 테이블(intermediary join table)을 만든다.
- 테이블 이름은 앱이름 및 ManyToManyField의 이름과 이를 포함하는 모델의 이름을 조합하여 생성한다.

<br>

**중개 테이블 필드 생성 규칙**

1. 소스(source model) 및 대상(target model) 모델이 다른 경우
   - id
   - `<containing_model>_id`
   - `<other_model>_id`
2. ManyToManyField가 동일한 모델을 가리키는 경우
   - id
   - `from_<model>_id`
   - `to_<model>_id`

<br>

------

<br>

### LIKE

**model 설정**

```python
# articles/models.py

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    ...
```

```bash
$ python manage.py makemigrations
```

<br>

- **현 상황에서는 `related_name` 작성이 필수**
  - M:N 관계 설정 시에 `related_name` 이 없다면 자동으로 `.article_set` 매니저를 사용할 수 있도록 하는 데 이 매니저는 이미 이전 1:N(User:Article) 관계에서 사용 중인 매니저이다.
  - user가 작성한 글들(`user.article_set`)과 user가 좋아요를 누른 글(`user.article_set`)을 django는 구분할 수 없게 된다.
  - user와 관계된 ForeignKey 혹은 ManyToManyField 중 하나에 `related_name` 추가 작성이 필요하다.

<br>

- **이제 사용 가능한 manager는 다음과 같다.**
  - `article.user` : 게시글을 작성한 유저 - 1:N
  - `article.like_users` : 게시글을 좋아요한 유저 - M:N
  - `user.article_set`: 유저가 작성한 게시글들 → 역참조 - 1:N
  - `user.like_articles`: 유저가 좋아요한 게시글들 → 역참조 - M:N

<br>

**좋아요 구현**

> https://docs.djangoproject.com/en/3.1/ref/models/querysets/#filter
>
> https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.exists

- `exists()`
  - 최소한 하나의 레코드가 존재하는지 여부를 확인하여 알려 준다. 
- 쿼리셋 cache를 만들지 않으면서 특정 레코드가 존재하는지 검사한다.
  - 결과 전체가 필요하지 않은 경우 유용하다.
  

```python
# articles/urls.py

urlpatterns = [
    ...,
    path('<int:article_pk>/likes/', views.likes, name='likes'),
]
```

```python
# articles/views.py

@require_POST
def likes(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)

        if article.like_users.filter(pk=request.user.pk).exists():
        # if request.user in article.like_users.all():
            article.like_users.remove(request.user)
        else:
            article.like_users.add(request.user)
        return redirect('articles:index')
    return redirect('accounts:login')
```

```django
<!-- articles/index.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>Articles</h1>
  {% if request.user.is_authenticated %}
    <a href="{% url 'articles:create' %}">[CREATE]</a>
  {% else %}
    <a href="{% url 'accounts:login' %}">[새 글을 작성하려면 로그인하세요.]</a>
  {% endif %}
  <hr>
  {% for article in articles %}
    <p><b>작성자 : {{ article.user }}</b></p>
    <p>글 번호 : {{ article.pk }}</p>
    <p>글 제목 : {{ article.title }}</p>
    <p>글 내용 : {{ article.content }}</p>
    <div>
      <form action="{% url 'articles:likes' article.pk %}" method="POST">
        {% csrf_token %}
        {% if request.user in article.like_users.all %}
          <button>좋아요 취소</button>
        {% else %}
          <button>좋아요</button>
        {% endif %}
      </form>
    </div>
    <p>{{ article.like_users.all|length }} 명이 이 글을 좋아합니다.</p>
    <a href="{% url 'articles:detail' article.pk %}">[DETAIL]</a>
    <hr>
  {% endfor %}
{% endblock %}
```

- 좋아요 버튼 누른 후 데이터베이스 확인

<br>

---

<br>

### Profile

- 자연스러운 follow 흐름을 위한 프로필 페이지 작성

```python
# accounts/urls.py

path('<username>/', views.profile, name='profile'),
```

```python
# accounts/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model


def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)
```

```django
<!-- accounts/profile.html -->

{% extends 'base.html' %}

{% block content %}
<h1>{{ person.username }}님의 프로필</h1>

<hr>

<h2>{{ person.username }}'s 게시글</h2>
{% for article in person.article_set.all %}
  <div>{{ article.title }}</div>
{% endfor %}

<hr>

<h2>{{ person.username }}'s 댓글</h2>
{% for comment in person.comment_set.all %}
  <div>{{ comment.content }}</div>
{% endfor %}

<hr>

<h2>{{ person.username }}'s likes</h2>
{% for article in person.like_articles.all %}
  <div>{{ article.title }}</div>
{% endfor %}

<hr>

<a href="{% url 'articles:index' %}">back</a>
{% endblock  %}
```

```django
<!-- base.html -->

<body>
  <div class="container">
    <h3>Hello, {{ request.user }}</h3>
    {% if request.user.is_authenticated %}
      <a href="{% url 'accounts:profile' request.user.username %}">내 프로필</a>
      <a href="{% url 'accounts:update' %}">[회원정보수정]</a>
      ...
    {% else %}
```

```django
<!-- articles/index.html -->

<p>
  <b>작성자 : <a href="{% url 'accounts:profile' article.user.username %}">{{ article.user }}</a></b>
</p>
```

<br>

---

<br>

### FOLLOW

**models 작성**

```python
# accounts/models.py

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
```

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

- `accounts_user_followings` 중개 테이블 생성 확인

<br>

**Follow 구현**

> 자기자신은 follow 하면 안된다.

```python
# accounts/urls.py

urlpatterns = [
    ...,
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]
```

```python
# accounts/views.py

@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(), pk=user_pk)
        if person != request.user:
            if person.followers.filter(pk=request.user.pk).exists():
            # if request.user in person.followers.all():
                person.followers.remove(request.user)
            else:
                person.followers.add(request.user)
        return redirect('accounts:profile', person.username)
    return redirect('accounts:login')
```

<br>

**templates**

```django
<!-- accounts/profile.html -->

<div> 
  <div>
    팔로잉 : {{ person.followings.all|length }} / 팔로워 : {{ person.followers.all|length }}
  </div>
  {% if request.user != person %}
    <div>
      <form action="{% url 'accounts:follow' person.pk %}" method="POST">
        {% csrf_token %}
        {% if request.user in person.followers.all %}
          <button>Unfollow</button>
        {% else %}
          <button>Follow</button>
        {% endif %}
      </form>
    </div>
  {% endif %}
</div>
```

<br>

**`with` template tag**

>  https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#with

- 더 간단한 이름으로 복잡한 변수를 저장한다.
- 주로 데이터베이스에 중복으로 여러번 엑세스 할 때 유용하게 사용한다.
- 변수는 `{% with %}` and `{% endwith %}` 사이에서만 사용 가능하다.

```django
<!-- accounts/profile.html -->

{% with followings=person.followings.all followers=person.followers.all %}
  <div> 
    <div>
      팔로잉 : {{ followings|length }} / 팔로워 : {{ followers|length }}
    </div>
    {% if request.user != person %}
      <div>
        <form action="{% url 'accounts:follow' person.pk %}" method="POST">
          {% csrf_token %}
          {% if request.user in followers %}
            <button>Unfollow</button>
          {% else %}
            <button>Follow</button>
          {% endif %}
        </form>
      </div>
    {% endif %}
  </div>
{% endwith %}
```

------