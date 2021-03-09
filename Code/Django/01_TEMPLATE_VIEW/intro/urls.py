from django.contrib import admin
from django.urls import path, include
from workshop0309 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lotto/', include('pages.urls')),  # pages의 urls.py로 보냄
    # /workshop0308/ => 'workshop0308.urls'
    path('workshop0308/', include('workshop0308.urls')),
    # /practice0309/ => 'practice0309.urls'
    # path('practice0309/', include('practice0309.urls')),
    
    # Domain/workshop0309/<menu>/몇명/
    path('workshop0309/dinner/<menu>/<int:people>/', views.dinner, name='dinner'),
]
