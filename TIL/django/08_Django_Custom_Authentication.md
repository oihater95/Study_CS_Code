[TOC]

# 08. Django_Custom_Authentication

<br>

## User model 대체하기

> https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#auth-custom-user

- 일부 프로젝트에서는 Django의 내장 유저 모델이 제공하는 인증 요구사항이 적절하지 않을 수 있다.
- django는 custom model을 참조하는 `AUTH_USER_MODEL` 설정을 제공하여 default user model을 재정의(override)할 수 있도록 한다.
- django는 새 프로젝트를 시작하는 경우 기본 사용자 모델이 충분하더라도 커스텀 유저 모델을 설정하는 것을 강력하게 권장(highly recommended)
  - 커스텀 유저 모델은 기본 사용자 모델과 동일하게 작동하지만 필요한 경우 나중에 맞춤 설정할 수 있기 때문이다.
- **단, 프로젝트의 모든 migrations 혹은 첫 migrate를 실행하기 전에 이 작업을 마쳐야 한다.**

<br>

```python
# settings.py

AUTH_USER_MODEL = 'accounts.User' 
```

```python
# accounts/models.py

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
```

```python
# accounts/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


admin.site.register(User, UserAdmin)
```

<br>

**AUTH_USER_MODEL**

> https://docs.djangoproject.com/en/3.1/ref/settings/#auth-user-model

- User를 나타내는데 사용하는 모델
- 주의 사항
  - 프로젝트를 진행하는 동안 (즉, 프로젝트에 의존하는 모델을 만들고 마이그레이션 한 후) 설정은 변경할 수 없다. (변경하려면 큰 노력이 필요)
  - 프로젝트 시작 시 설정하기 위한 것이며, 참조하는 모델은 첫번째 마이그레이션에서 사용할 수 있어야 함

<br>

**데이터베이스 초기화 후 마이그레이션 (프로젝트 중간이라면)**

1. migrations 파일 삭제
2. db.sqlite3 삭제
3. migrations 진행

<br>

**`AbstractUser` vs `AbstractBaseUser`**

> https://github.com/django/django/blob/main/django/contrib/auth/base_user.py#L47
>  https://github.com/django/django/blob/main/django/contrib/auth/models.py#L321

<img width="250" alt="Picture1" src="https://user-images.githubusercontent.com/18046097/93996761-98afc300-fdcd-11ea-9ae7-3d8f90f102a8.png">

- `AbstractBaseUser`
  - password 와 last_login 만 기본적으로 제공
  - 자유도가 높지만 필요한 필드는 모두 작성해야 함
- `AbstractUser`
  - 관리자 권한과 함께 완전한 기능을 갖춘 사용자 모델을 구현하는 기본 클래스

<br>

## Custom user and built-in auth forms

> https://docs.djangoproject.com/ko/3.1/topics/auth/customizing/#custom-users-and-the-built-in-auth-forms

- 유저모델 대체 후 회원가입 시 에러 발생
- AbstractBaseUser의 모든 subclass와 호환되는 forms
  - AuthenticationForm, SetPasswordForm, PasswordChangeForm, AdminPasswordChangeForm
- User와 연결되어 있어서 커스텀 유저 모델을 사용하려면 다시 작성하거나 확장해야 하는 forms
  - UserCreationForm, UserChangeForm


<br>

`UserCreataionForm()` 재정의

```python
# accounts/forms.py

from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('email',)
```

```python
# accounts/views.py

from .forms import CustomUserChangeForm, CustomUserCreationForm


def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)
```

<br>

---

<br>

## Referencing the User model

> [https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#referencing-the-user-model](https://docs.djangoproject.com/en/3.1/topics/auth/customizing/)

`settings.AUTH_USER_MODEL`

- 유저 모델에 대한 외래 키 또는 다대다 관계를 정의 할 때 사용
- models.py에서 유저 모델을 참조할 때 사용

<br>

`get_user_model()`

- django는 User를 직접 참조하는 대신 django.contrib.auth.get_user_model()을 사용하여 사용자 모델을 참조해야 한다고 권장
- 현재 활성화(active)된 user model을 반환
  - 커스텀한 유저 모델이 있을 경우는 커스텀 유저 모델, 그렇지 않으면 User를 반환
  - 이것이 User를 직접 참조하지 않는 이유
- models.py가 아닌 다른 모든 곳에서 유저 모델을 참조할 때 사용

<br>

**참조 예시**

```python
# articles/models.py

from django.conf import settings


class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```

