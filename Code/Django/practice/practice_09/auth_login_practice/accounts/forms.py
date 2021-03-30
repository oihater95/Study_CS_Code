from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model  # from .models import User 대신에 이거 씀
from django import forms

User = get_user_model()  # models.py의 User 대신에 이거 씀, AUTH_USER_MODEL

'''
기존의 모델 폼
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
'''

class CustomUserCreationForm(UserCreationForm):  # UserCreationForm => ModelForm, save() => return user(본인을 반환) 
    class Meta:
        model = User
        fields = ('username', )


class CustomUserChangeForm(UserChangeForm):
    last_name = forms.CharField(min_length=2, max_length=100)
    first_name = forms.CharField(min_length=2, max_length=100)
    email = forms.EmailField(min_length=1)
    password = None  # password 안보이게 하기
    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'email',)