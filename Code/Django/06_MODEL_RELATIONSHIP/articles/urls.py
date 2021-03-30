from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:article_pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/update/', views.update, name='update'),
    path('<int:article_pk>/delete/', views.delete, name='delete'),

    # /articles/<article_pk>/...
    # /articles/<article_pk>/ => Comment Read (Article Detail Page)
    # /articles/<article_pk>/comments/<comment_pk>/update/ => Comment Update
    # /articles/<article_pk>/comments/<comment_pk>/delete/ => Comment Delete
    path('<int:article_pk>/comments/create', views.comment_create, name='comment_create'),
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
    # path('<int:article_pk>/comments/<int:comment_pk>/update/', views.comment_update, name='comment_update'),

]
