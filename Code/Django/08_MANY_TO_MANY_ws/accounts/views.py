from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model

User = get_user_model()

def profile(request, username):
    me = request.user  # 보려는 사람
    you = get_object_or_404(User, username=username)  # 보고자하는 대상

    


def follow(request, username):
    fan = request.user  # follow 요청 보낸 사람
    star = get_object_or_404(User, username=username)  # 팔로우 요청 받는 사람

    if user.is_authenticated:
        # 인증된 사용자가 이미 팔로우 중이라면
        if fan.stars.filter(pk=star.pk).exists():
            fan.stars.remove(star)
        else:
            fan.stars.add(star)

    return redirect('accounts:profile', star.pk)