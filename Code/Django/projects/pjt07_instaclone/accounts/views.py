from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# from django.contrib.auth import login as auth_login, logout as auth_logout
from django.views.decorators.http import require_POST, require_http_methods, require_safe
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash, get_user_model
from django.contrib.auth.forms import (
    AuthenticationForm, 
    UserCreationForm, 
    PasswordChangeForm,
)
from .forms import CustomUserChangeForm, CustomUserCreationForm

User = get_user_model()
# Create your views here.
@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('community:index')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('community:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'community:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


@require_POST
def logout(request):
    auth_logout(request)
    return redirect('community:index')


@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('articles:index')


@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method == 'POST':
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


@login_required
@require_http_methods(['GET', 'POST'])
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        # form = PasswordChangeForm(user=request.user, data=request.POST)
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


@require_safe
def profile(request, user_id):
    you = get_object_or_404(User, pk=user_id)
    context = {
        'you': you
    }
    return render(request, 'accounts/profile.html', context)


@require_http_methods(['GET', 'POST'])
def follow(request, user_id):
    you = get_object_or_404(User, pk=user_id)
    me = request.user

    if request.user.is_authenticated:
        if you != me:
            if you.followers.filter(pk=me.pk).exists():
                you.followers.remove(me)
                
            else:
                you.followers.add(me)
        return redirect('accounts:profile', user_id)
    return redirect('accounts:login')
