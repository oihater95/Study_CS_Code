from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)

class CustomUserChangeForm(UserChangeForm):
    last_name = forms.CharField(min_length=2, max_length=100)
    first_name = forms.CharField(min_length=2, max_length=100)
    email = forms.EmailField(min_length=1)
    password = None  

    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'email',)