from django.urls import path
from . import views

# practice/...
urlpatterns = [
    # practice/'' => 목록 보여주기(전체 조회)
    path('', views.index, name='index'),

    # practice/1 => 1번 학생 정보 보여주기 (단일 조회)
    path('<int:pk>/', views.detail, name='detail'),

    # practice/new => 새로운 데이터 입력용 HTML(생성 준비 단계)
    path('new/', views.new, name='new'),

    # practice/create/ => 사용자 입력 데이터 처리
    path('create/', views.create, name='create'),
]
