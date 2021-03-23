from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # ORM은 models.py 내부의 class에서, class var만 확인하여 DB의 Column으로 만든다.
    # def __str__의 경우 중간에 추가해도 makemigrations에 잡히지 않음
    def __str__(self):
        return f'{self.id} => {self.title}'