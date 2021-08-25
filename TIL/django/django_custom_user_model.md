# Custom User

1. **프로젝트 시작 전**에 accounts 앱을 만든다.

2. 커스텀 User 모델을 생성한다.

   ```python
   from django.db import models
   from django.contrib.auth.models import AbstractUser
   
   # Create your models here.
   class User(AbstractUser):
       pass 
   ```

3. settings.py에 AUTH_USER_MODEL을 변경한다.

   ```python
   # settings.py
   
   AUTH_USER_MODEL = 'accounts.User'
   ```

4. **프로젝트 시작.**





