from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from django.contrib.auth.decorators import login_required
User = get_user_model()

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    context = { 'form': form }
    return render(request, 'accounts/signup.html', context)


def profile(request, username):
    user = get_object_or_404(User, username=username)
    context = {'user_profile': user}
    if request.user == user:
        if request.method == "POST":
            form = CustomUserChangeForm(request.POST, instance=user)  
            if form.is_valid():
                user = form.save()
                return redirect('accounts:profile', username=user.username)
    else:
        form = CustomUserChangeForm(instance=user)    
    
    context['form'] = form

return render(request, 'accounts/profile.html', context)



def login(requset):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('accounts:profile', user.username)
    else:
        form = AuthenticationForm()
    context = { 'form': form }
    return render(request, 'accounts/login.html', context)


def logout(request):


def update(request, username):


def change_password(request):

def withdraw(request):
