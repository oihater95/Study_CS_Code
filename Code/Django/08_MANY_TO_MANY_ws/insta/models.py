from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(User, related_name='like_articles', through='Like')  # User는 like_users를 부를 때 like_articles로 부른다.
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Like(models.Model):
    # 직접 FK 연결
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # 추가할 데이터, 추가 필드 정의
    created_at = models.DateTimeField(auto_now_add=True)  # 좋아요 누른 시간



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200) 