from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', )


class CustomUserChangeForm(UserChangeForm):
    first_name = forms.CharField(min_length=1, max_length=30)
    last_name = forms.CharField(min_length=1, max_length=30)
    email = forms.EmailField(min_length=1)
    
    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'email',)