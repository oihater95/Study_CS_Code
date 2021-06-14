from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('<int:movie_pk>/create/', views.create_rate, name='create_rate'),
    path('<int:movie_pk>/<int:rate_pk>/update/', views.update_rate, name='update_rate'),
    path('<int:movie_pk>/<int:rate_pk>/delete/', views.delete_rate, name='delete_rate'),
    path('<int:movie_pk>/like_detail/', views.like_from_detail, name='like_from_detail'),
    path('<int:movie_pk>/like_index/', views.like_from_index, name='like_from_index'),
    path('recommend2/', views.recommend2, name='recommend2'),
    path('genres/', views.genre_index, name='genre_index'),
    path('genres/<int:genre_pk>', views.genre_detail, name='genre_detail'),
    path('genres/<int:genre_pk>/<int:movie_pk>', views.like_from_genre_detail, name='like_from_genre_detail'),
]
