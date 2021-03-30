from django.db import models

# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length=10)  # 제한을 써주기는 하나 적용은 안됨
    number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    