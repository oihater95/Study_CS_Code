from django.urls import path
from . import views

urlpatterns = [
    # intro > urls.py에서 path('workshop0308/')로 여기 도달
    # Domain/workshop0308/까지는 intro > urls.py에서 처리 그 뒤가 들어옴
    path('lotto/', views.lotto),
]
