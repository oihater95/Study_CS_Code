from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/update/', views.update, name='update'),
    path('<int:article_pk>/delete/', views.delete, name='delete'),
    path('<int:article_pk>/comment/', views.create_comment, name='create_comment'),
    path('<int:article_pk>/comment/<int:comment_pk>/update/', views.update_comment, name='update_comment'),
    path('<int:article_pk>/comment/<int:comment_pk>/delete/', views.delete_comment, name='delete_comment'),
]
