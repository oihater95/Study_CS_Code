[TOC]

# 06. Django_Auth

<br>

## Accounts

> app 이름이 반드시 accounts 일 필요는 없지만, 
> **auth 관련 기본 설정들이 accounts로 내부적으로 사용되고** 있기 때문에 되도록 accounts로 명명 권장

```bash
$ python manage.py startapp accounts
```

```python
# settings.py

INSTALLED_APPS = [
    'articles',
    'accounts',
...
```

```python
# myform/urls.py

urlpatterns = [
    path('accounts/', include('accounts.urls')),
]
```

```python
# accounts/urls.py

from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    
]
```

<br>

---

<br>

**Authentication(인증)**

- 신원 확인
- 자신이 누구라고 **주장하는 사람의 신원을 확인**하는 것

<br>

**Authorization(권한, 허가)**

- 권한 부여
- 가고 싶은 곳으로 가도록 혹은 **원하는 정보를 얻도록 허용**하는 과정

<br>

---

<br>

## Authentication in Web requests

### Login

- 로그인은 **`Session을 create 하는 것`**이다.

<br>

**AuthenticationForm**

> user 로그인을 위한 form
>
> https://docs.djangoproject.com/en/3.1/topics/auth/default/#django.contrib.auth.forms.AuthenticationForm
>
> https://github.com/django/django/blob/master/django/contrib/auth/forms.py#L173
>

<br>

**login()**

> https://docs.djangoproject.com/en/3.1/topics/auth/default/#authentication-in-web-requests

- 현재 세션에 연결하려는 인증 된 사용자가 있는 경우 `login()` 함수가 필요하다.

- django 의 session framework 를 통해 user 의 ID 를 세션에 저장한다.

- 즉, 로그인을 한다.

  ```python
  # accounts/urls.py
  
  path('login/', views.login, name='login'),
  ```

  > `AuthenticationForm` 은 왜 첫번째 인자가 request 인가? 
> ModelForm이 아닌 Form 이기 때문.

  ```python
  # accounts/views.py
  
  from django.shortcuts import render, redirect
  from django.contrib.auth import login as auth_login
  from django.contrib.auth.forms import AuthenticationForm
  
  
  def login(request):
      if request.method == 'POST':
          form = AuthenticationForm(request, request.POST)
          if form.is_valid():
              auth_login(request, form.get_user())
              return redirect('articles:index')
      else:
          form = AuthenticationForm()
      context = {
          'form': form,
      }
      return render(request, 'accounts/login.html', context)
  ```

- login 함수 이름을 `auth_login` 으로 변경해서 사용하는 이유는 view 함수인 login 과의 충돌을 방지하기 위함이다.
  
  ```django
  <!-- accounts/login.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
  <h1>로그인</h1>
  <form action="" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
  {% endblock %}
  ```
```
  
  - 로그인 후 브라우저와 DB에서 세션 확인

<br>

- 로그인을 진행하면 현재 로그인이 되어 있는지 확인할 수가 없기 때문에, 템플릿에서 현재 로그인 유저 이름을 출력 해보자.

  ```django
  <!-- base.html -->
  
  <body>
    <div class="container">
      <h3>Hello, {{ request.user }}</h3>
      <a href="{% url 'accounts:login' %}">Login</a>
      {% block content %}
      {% endblock %}
    </div>
    ...
  </body>
  </html>
```

<br>

------

<br>

### Logout

> 로그아웃은 **Session을 Delete** 하는 로직과 같다.

**logout()**

> https://docs.djangoproject.com/ko/3.1/topics/auth/default/#how-to-log-a-user-out

- logout 함수는 HttpRequest 객체를 인자로 받고 return 값은 없다.

- logout 함수를 호출하면 현재 request에 대한 db의 session data를 완전히 정리하고, 클라이언트 쿠키에서도 sessionid가 삭제된다.

- 이는 다른 사람이 동일한 웹 브라우저를 사용하여 로그인하고, 이전 사용자의 세션 데이터에 액세스하는 것을 방지하기 위한 것이다.

- 사용자가 로그인하지 않은 경우 오류를 발생시키지 않는다.

  ```python
  # accounts/urls.py
  
  path('logout/', views.logout, name='logout'),
  ```

  ```python
  # accounts/views.py
  
  from django.contrib.auth import logout as auth_logout
  # from django.contrib.auth import login as auth_login, logout as auth_logout 처럼 작성 가능
  from django.views.decorators.http import require_POST
  
  
  @require_POST
  def logout(request):
      auth_logout(request)
      return redirect('articles:index')
  ```

  ```django
  <!-- base.html -->
  
  <body>
    <div class="container">
      <h3>Hello, {{ user.username }}</h3>
      <a href="{% url 'accounts:login' %}">Login</a>
      <form action="{% url 'accounts:logout' %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="Logout">
      </form>
      {% block content %}
      {% endblock %}
    </div>
  ```

<br>

---

<br>

## 로그인 사용자에 대한 접근 제한

> https://docs.djangoproject.com/ko/3.1/topics/auth/default/#limiting-access-to-logged-in-users
>

<br>

1. `is_authenticated` attribute
   - The raw way
2. `login_required` decorator
   - As a shortcut

<br>

### is_authenticated

> **주의!** 
> 이것은 권한(permission)과는 관련이 없으며 사용자가 활성화 상태(active)이거나 유효한 세션(valid session)을 가지고 있는지도 확인하지 않는다.

> https://docs.djangoproject.com/en/3.1/ref/contrib/auth/#attributes
>
> https://github.com/django/django/blob/master/django/contrib/auth/base_user.py#L90

- 사용자가 인증 되었는지 알 수 있는 방법

- User model 의 `속성(attributes)` 들 중 하나.

- User에 항상 `True`이며, AnonymousUser에 대해서만 항상 `False`이다.

  ```django
  <!-- base.html -->
  
  {% if user.is_authenticated %}
    <h3>Hello, {{ user.username }}</h3>
    <form action="{% url 'accounts:logout' %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="Logout">
    </form>
  {% else %}
    <a href="{% url 'accounts:login' %}">Login</a>
  {% endif %}
  ```


<br>

**로그인 후 로그인 페이지 접근 제한**

```python
# accounts/views.py

def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
```

<br>

**비 로그인시 게시글 작성 링크 가리기**

```django
<!-- articles/index.html -->

{% extends 'base.html' %}

{% block content %}
  <h1 class="text-center">Articles</h1>
  {% if user.is_authenticated %}
    <a href="{% url 'articles:create' %}">CREATE</a>
  {% else %}
    <a href="{% url 'accounts:login' %}">[새 글을 작성하려면 로그인하세요]</a>
  {% endif %}
  ...
{% endblock %}
```

- 하지만 비 로그인 상태로도 url 에 직접 입력하면 작성 페이지로 갈 수 있다.

<br>

### login_required decorator

> https://docs.djangoproject.com/en/3.1/topics/auth/default/#limiting-access-to-logged-in-users
>
> https://github.com/django/django/blob/master/django/contrib/auth/decorators.py#L38

- 로그인 하지 않은 사용자의 경우 `settings.LOGIN_URL`에 설정된 문자열 기반 절대 경로로 리다이렉트 된다.
  - ex) 이후 인증 성공시 사용자가 redirect 되어야하는 경로는 `next`라는 쿼리 문자열 매개 변수에 저장
- LOGIN_URL 의 기본 값은 `'/accounts/login/'`, 우리가 두번째 app 이름을 accounts 로 했던 이유 중 하나
- 로그인 된 사용자의 경우 정상적으로 해당 view 를 실행한다.

<br>

```python
# articles/views.py

from django.contrib.auth.decorators import login_required


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):


@login_required
@require_POST
def delete(request, pk):
```

- 이제 `articles/create/` 로 강제 접속 시 로그인 페이지로 리다이렉트 된다.
- 그런데 `/accounts/login/?next=/articles/create/` 와 같은 주소가 생성된다.

<br>

**`"next"` query string parameter**

- `@login_required` 은 기본적으로 인증 성공 후 사용자를 리다이렉트 할 경로를 **next 라는 문자열 매개 변수에 저장**한다.

- 우리가 url 로 접근하려고 했던 그 주소가 로그인이 되어있지 않으면 볼 수 없는 곳이라서, django 가 로그인 페이지로 강제로 돌려 보냈는데, 로그인을 다시 정상적으로 하면 원래 요청했던 주소로 보내 주기 위해 **keep 해주는 것**이다.

- 따로 처리 해주지 않으면 우리가 view에 설정한 redirect 경로로 이동하지만, next 에 저장된 주소로 이동되도록 만들기 위해 작업을 해보자.

  ```python
  # accounts/views.py
  
  def login(request):
      if request.user.is_authenticated:
          return redirect('articles:index')
  
      if request.method == 'POST':
          form = AuthenticationForm(request, request.POST)
          if form.is_valid():
              auth_login(request, form.get_user())
              return redirect(request.GET.get('next') or 'articles:index')
  
  ...
  ```

  > [주의]
  >
  > - 만약 `login.html`에서 form action이 작성되어 있다면 동작하지 않는다.
  >
  > - 해당 action 주소 자체가 next 파라미터가 붙어있는 현재 url이 아닌 `/accounts/login/` 으로 요청을 보내기 때문이다.

<br>

**두 데코레이터로 인해 로직상 문제 발생**

- 비로그인 상태로 detail 페이지에서 글 삭제 시도해보자.

- 만약 `@require_POST` 가 있는 함수에 `@login_required` 가 설정 된다면 로그인 이후 `"next"` 매개변수를 따라 해당 함수로 다시 redirect 되면서 `@require_POST` 때문에 405 에러가 발생하게 될 것이다.

- 이 경우 두가지 문제가 발생하게 되는데 첫째로는 **redirect 중 POST 데이터의 손실**이 일어나며 둘째로는 애초에 **redirect 는 POST Request 가 불가능**하여 GET Request 로 요청이 보내진다.

- 비로그인 상태 POST로 요청 -> 로그인 검증(@login_required) -> 로그인 페이지 (?next='articles/1/delete/') -> 로그인 성공 -> next로 redirect (GET Request) -> POST인지 검증(@require_POST) -> 405 Method Not Allowed

> `login_required` 는 GET 요청을 처리할 수 있는 View에서만 사용하자.

- 때문에 POST 요청만 허용하는 `delete` 와 같은 함수는 아래와 같이 함수 내부에서 처리하도록 한다.

  ```python
  # articles/views.py
  
  @require_POST
  def delete(request, pk):
      if request.user.is_authenticated:
          article = Article.objects.get(pk=pk)
          article.delete()
      return redirect('articles:index')
  ```

<br>

------

<br>

## 회원 가입

**UserCreationForm**

- 주어진 username과 password로 권한이 없는 user를 create하는 Modelform

```python
# accounts/urls.py

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
]
```

```python
# accounts/views.py

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)
```

```django
<!-- accounts/signup.html -->

{% extends 'base.html' %}

{% block content %}
<h1>회원가입</h1>
<form action="" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit">
</form>
{% endblock %}
```

<br>

**회원가입 후 자동으로 로그인 상태 전환**

```python
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {'form': form,}
    return render(request, 'accounts/signup.html', context)
```

<br>

## 회원 탈퇴

> 유저를 탈퇴하는 것은 DB에서 유저를 삭제하는 것과 같음

```python
# accounts/urls.py

path('delete/', views.delete, name='delete'),
```

```python
# accounts/views.py

from django.views.decorators.http import require_POST


@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
    return redirect('articles:index')
```

- sqlite 확장프로그램이나 admin 페이지에서 유저가 삭제 되었는지 확인해 본다.

<br>

------

<br>

## 회원 수정

**UserChangeForm**

> user의 정보 및 권한을 변경하기 위해 admin 인터페이스에서 사용되는 modelform
>
> https://docs.djangoproject.com/en/3.1/topics/auth/default/#django.contrib.auth.forms.UserChangeForm
>
> https://github.com/django/django/blob/master/django/contrib/auth/forms.py#L142

```python
# accounts/urls.py

path('update/', views.update, name='update'),
```

```python
# accounts/forms.py

from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)
```

```python
# accounts/views.py

from .forms import CustomUserChangeForm


@login_required
def update(request):
    if request.method == 'POST':
        # form = CustomUserChangeForm(data=request.POST, instance=request.user)
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)
```

```django
<!-- accounts/update.html -->

{% extends 'base.html' %}

{% block content %}
<h1>회원정보수정</h1>
<form action="" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit">
</form>
{% endblock  %}
```

```html
<!-- articles/base.html -->

{% if request.user.is_authenticated %}
  <h3>Hello, {{ user.username }}</h3>
  <a href="{% url 'accounts:update' %}">정보수정</a>
  ...
{% else %}
  <a href="{% url 'accounts:login' %}">Login</a>
  <a href="{% url 'accounts:signup' %}">Signup</a>
{% endif %}
```

- 정보수정 페이지를 확인해보자.

<br>

**get_user_model()**

> https://docs.djangoproject.com/ko/3.1/topics/auth/customizing/#referencing-the-user-model

- `User`를 직접 참조하는 대신`django.contrib.auth.get_user_model()` 을 사용하여 User model 을 참조해야 한다.
- **이 함수는 현재 활성화(active)된 user model을 리턴**한다.
- 커스텀한 유저 모델이 있을 경우는 커스텀 유저 모델, 그렇지 않으면 User를 참조
  - 단순 User를 직접 참조하지 않는 이유

<br>

**AbstractUser**

> User model을 구현하는 완전한 기능을 갖춘 기본 클래스 

- django github 으로 가서 직접 `UserChangeForm` 을 확인해보자. 

  - https://github.com/django/django/blob/master/django/contrib/auth/forms.py#L132

- Meta 정보를 보면 User 라는 model 을 참조하는 ModelForm 이라는 것을 확인할 수 있다.

- 이번엔 User 클래스를 찾아가보자. 

  - https://github.com/django/django/blob/master/django/contrib/auth/models.py#L384

- 그런데 User 클래스는 비어있고 `AbstractUser` 를 상속받고 있다. AbstractUser 를 다시 따라가보자. 

  - https://github.com/django/django/blob/master/django/contrib/auth/models.py#L316

- `AbstractUser` 의 클래스 변수명들을 확인해보면 우리가 회원수정 페이지에서 봤던 필드들과 일치한다는 것을 할 수 있다.

- 이제 공식문서에서 User 모델의 Fields 를 자세히 확인해보자.

  - https://docs.djangoproject.com/en/3.1/ref/contrib/auth/#user-model


<br>

---

<br>

## 비밀번호 변경

**PasswordChangeForm**

> 이전 비밀번호를 입력하여 비밀번호를 변경할 수 있도록 하는 Form
>
> https://docs.djangoproject.com/en/3.1/topics/auth/default/#django.contrib.auth.forms.PasswordChangeForm

- 회원정보 수정을 위한 `UserChangeForm` 에도 password 필드는 있지만 막상 필드를 보면 수정할 수 없다.

- 대신, 가장 하단에 '**다만 이 양식으로 비밀번호를 변경할 수 없습니다.**' 라는 문구가 있는데, 이 링크를 클릭하면 `accounts/password/` 라는 주소로 이동한다. django가 기본적으로 설정하고 있는 주소이다. 

  ```python
  # accounts/urls.py
  
  path('password/', views.change_password, name='change_password'),
  ```

  ```python
  # accounts/views.py
  
  from django.contrib.auth.forms import (
      UserCreationForm,
      AuthenticationForm,
      PasswordChangeForm,
  )
  from django.contrib.auth import update_session_auth_hash
  
  
  @login_required
  def change_password(request):
      if request.method == 'POST':
          form = PasswordChangeForm(request.user, request.POST)
          if form.is_valid():
              form.save()
              update_session_auth_hash(request, form.user)
              return redirect('articles:index')
      else:
          form = PasswordChangeForm(request.user)
      context = {
          'form': form,
      }
    return render(request, 'accounts/change_password.html', context)
  ```

  - [SetPasswordForm](https://github.com/django/django/blob/05bbff82638731a6abfed2fe0ae06a4d429cb32f/django/contrib/auth/forms.py#L316)의 init 함수를 살펴보면 첫번째 인자로 반드시 user가 위치

  ```django
  <!-- accounts/change_password.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
  <h1>비밀번호 변경</h1>
  <form action="" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
  {% endblock %}
  ```


<br>

**update_session_auth_hash()**

> "암호 변경 시 세션 무효화 방지"
>
> - 비밀번호는 잘 변경되었으나 비밀번호가 변경 되면서 기존 세션과의 회원 인증 정보가 일치하지 않기 때문
> - 비밀번호는 잘 변경되었으나 비밀번호가 변경 되면서 기존 세션과의 회원 인증 정보가 일치하지 않기 때문
> - 현재 요청(current request)과 새 session hash가 파생 될 업데이트 된 사용자 객체를 가져와서 session hash를 적절하게 업데이트해 로그아웃을 막는다.
>
> https://docs.djangoproject.com/en/3.1/topics/auth/default/#session-invalidation-on-password-change

<br>

---


