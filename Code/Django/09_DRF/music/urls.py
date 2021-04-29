from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('v1/artists/', views.artist_list_or_create),
    path('v1/artists/<int:artist_pk>/', views.artist_detail),
    path('v1/artists/<int:artist_pk>/musics/', views.create_music),
    path('v1/musics/', views.music_list),
    path('v1/musics/<int:music_pk>/', views.music_detail_or_update_or_delete),
]
