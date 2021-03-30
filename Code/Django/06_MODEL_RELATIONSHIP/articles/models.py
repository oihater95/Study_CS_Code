from django.db import models

class Article(models.Model):  # Article:Comment = 1:N
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    # article_id = IntegerField()  X
    article = models.ForeignKey(Article, on_delete=models.CASCADE)  # article_id
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
