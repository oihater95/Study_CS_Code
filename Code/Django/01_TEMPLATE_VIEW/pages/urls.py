from django.urls import path
from . import views

urlpatterns = [
    # intro > urls.py에서 path('lotto/')로 여기 도달
    # Domain/lotto/까지는 intro > urls.py에서 처리 그 뒤가 들어옴
    path('', views.lotto),
    # Domain/lotto/action
    # path('action/', views.action),
]
