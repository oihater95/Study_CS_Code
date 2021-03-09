from django.urls import path, include
from . import views  # intro의 views와 intro의 urls는 같은 디렉토리(intro)에 위치 => .

urlpatterns = [  # forwarding
    path('test/', views.test),
    path('articles/', include('articles.urls')),
]
