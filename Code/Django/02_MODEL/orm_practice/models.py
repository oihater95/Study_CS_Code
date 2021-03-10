from django.db import models

# Naming Convention => 단일 레코드의 이름(단수형)
class Student(models.Model):  # models.Model => 객체와 DB 연결
    name = models.CharField(max_length=100)  # CharField는 글자 수 제한 필요
    age = models.IntegerField()
    major = models.CharField(max_length=100)
    intro =  models.TextField()  # TextField는 글자 수 제한 없음
