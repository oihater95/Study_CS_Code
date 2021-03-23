from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm  # ModelForm X, Form O
from django.contrib.auth import login as auth_login  # def login과 겹치므로 as를 써서 다른 이름으로 바꿔줌, 입장 팔찌 같은 거
from django.contrib.auth import logout as auth_logout  # def logout과 겹치므로 as를 써서 다른 이름으로 바꿔줌
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm  # 모델 폼
# from .models import User 

User = get_user_model()

def index(request):
    users = User.objects.all()
    context = { 'users': users }
    return render(request, 'accounts/index.html', context)


def login(request):  # create와 거의 비슷
    # login 검증 / HTML 만드는 forms.FORM을 써서 완료
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)  # AuthenticationForm 첫번째 인자는 무조건 request
        if form.is_valid():  # 유효성 검사 => DB에 있는지 없는지 확인 (모델폼 유효성 검사와는 다름)
            # 로그인
            user_found_in_db = form.get_user()  # user객체
            auth_login(request, user_found_in_db)  # == auth_login(request, form.get_user() )
            return redirect('accounts:index')

    else:
        form = AuthenticationForm()
    context = { 'form': form, }
    return render(request, 'accounts/login.html', context)


def signup(request):  # create와 같다
    # 로그인 한 사용자라면 회원가입 없이 인덱스로 보냄
    if request.user.is_authenticated:
        return redirect('accounts:index')

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('accounts:index')
    else:
        form = CustomUserCreationForm()
    context = { 'form': form, }

    return render(request, 'accounts/signup.html', context)


def logout(request):
    auth_logout(request)
    return redirect('accounts:index')