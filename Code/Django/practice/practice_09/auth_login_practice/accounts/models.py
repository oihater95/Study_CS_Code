from django.db import models
from django.contrib.auth.models import AbstractUser

# 사용자 관리 모델 (AbstractUser를 상속 받아야함)
class User(AbstractUser):
    pass  # pass를 권장