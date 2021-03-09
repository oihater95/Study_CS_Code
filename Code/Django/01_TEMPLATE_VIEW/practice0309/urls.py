from django.urls import path
from . import views

app_name = 'practice0309'  # name space, 다른 앱에서 path name 겹치는 것 방지

# practice0309/...
urlpatterns = [
    # practice0309/lotto/ => practice0309 > views.py
    # practice0309/var_route/뭐든지들어옴/
    # views.var_route(request, value='asdf')
    path('var_route/<value>/', views.var_route),  # default는 str, <int:value> => value는 int형으로 받음
    path('lotto/<value>', views.lotto),  # value는 str형, value = 회차
    path('lotto_sol/', views.lotto),
    # variable routing 변수 라우팅 => url을 변수처럼, 동적 주소
    # path('<int:movie_id>/', views.find_movie),

    # /practice0309/ping/ => <form> 으로 사용자 입력 받기
    path('ping/', views.ping, name='ping'),

    # /practice0309/pong/ => 처리 결과 보여주기
    path('pong/', views.pong, name='pong'),
]
