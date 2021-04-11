from django.db import models
from faker import Faker

# Server Side => Modeling, Query
class Person(models.Model):
    name = models.CharField(max_length=100)

    # 더미 데이터 생성
    @classmethod
    def dummy(cls, n):
        f = Faker()
        for _ in range(n):
            cls.objects.create(name=f.name())


    @classmethod
    def dummy_bulk(cls, n):  # 쿼리처리속도 높음
        f = Faker()
        clss = []
        for _ in range(n):
            clss.append(cls(name=f.name()))
            objects: BaseManager
        cls.objects.bulk_create(clss)


    def __str__(self):
        return f'{self.pk}: {self.name}'


# 사람:게시글 = M:N
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # likes = models.ManyToManyField(Person)  => p1.article_set.all()  => p1이 좋아요 누른 게시글 쿼리셋
    likers = models.ManyToManyField(Person, related_name='likes')  # p1.likes.all() p1이 좋아요 누른 게시글 쿼리셋
    scrapers = models.ManyToManyField(Person, related_name='scraps')  # p1.scraps.all()
    # related_name => Person이 Article의 likes, scraps 부를 때 쓸 변수명
    author = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='my_articles')
    # a1.author => Person id / p1.article_set.all() == p1.my_articles.all()
    # author와 Person pk로 같지만 다르게 읽는다.
    editor = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='edit_articles')

    # 더미 데이터 생성
    @classmethod
    def dummy(cls, n):
        f = Faker()
        for _ in range(n):
            cls.objects.create(title=f.address(), content='hello')

    def __str__(self):
        return self.title
