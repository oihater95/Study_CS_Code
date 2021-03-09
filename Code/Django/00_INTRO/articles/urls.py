from django.urls import path
from . import views  # articles 디렉토리
# urlpatterns는 필수
urlpatterns = [
    path('index/', views.index),
    path('mail/', views.mail),
]
