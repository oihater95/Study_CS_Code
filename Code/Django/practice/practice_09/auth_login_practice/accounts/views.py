from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
User = get_user_model()

def index(request):
    return render(request, 'accounts/index.html')

# User table Create
@require_http_methods(['GET', 'POST'])
def signup(request): 
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # UserCreationForm은 user를 반환
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()

    context = { 'form': form }
    return render(request, 'accounts/signup.html', context)

# User table Read
@login_required
def profile(request, username):  # detail
    user = get_object_or_404(User, username=username)
    context = { 'user': user }
    return render(request, 'accounts/profile.html', context)


######################################################################

# Session table Create
# AuthenticationForm은 save없음
def login(request):
    
    if request.method == "POST":
        # AuthForm은 id/pw가 올바른지(User DB에 있는지) 검증
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():  # 검증이 올바르게 끝나면, id/pw에 매칭하는 사용자 추출 가능
            user = form.get_user()  # id/pw 매칭하는 사용자
            auth_login(request, user)  # form.save() X => auth_login() O, Session Table에 추가(입장권)
            return redirect('accounts:profile', user.username)
    else:
        form = AuthenticationForm()
    context = { 'form': form }

    return render(request, 'accounts/login.html', context)

# Session table Delete
@login_required
def logout(request):
    auth_logout(request)
    return redirect('accounts:index')


@login_required
def update(request, username):
    user = request.user
    context = { 'user_profile': user }

    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            return redirect('accounts:profile', username=user.username)

    else:
        form = CustomUserChangeForm(instance=user)
    context['form'] = form
    return render(request, 'accounts/update.html', context)

    
@login_required
@require_POST
def withdraw(request):
    # 삭제 후 로그아웃
    user = request.user
    user.delete()
    auth_logout(request)
    return redirect('accounts:index')