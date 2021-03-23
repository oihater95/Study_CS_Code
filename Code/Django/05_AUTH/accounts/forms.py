from django.contrib.auth.forms import UserCreationForm
# from .models import User
from django.contrib.auth import get_user_model  # 클래스 반환

# get_user_model() => settings.py의 AUTH_USER_MODEL을 반환
'''
 .models User 직접 참조 X
 직접 참조하면 UserCreationForm을 상속 받기 때문에 
 models.py의 User가 아닌 UserCreationForm의 User class를 받아온다.
'''
class CustomUserCreationForm(UserCreationForm):  # UserCreationForm => ModelForm
    # little customize
    class Meta:
        # model = User
        model = get_user_model()
        '''
        fields 없으면 에러
        fields = '__all__' 쓰면 모든 권한이 주어지기 때문에 X
        fields는 튜플 형태로 쓰기 ('~~',) 무조건 , 쓰기
        username 필드는 password와 password confirmation 자동으로 받게 함(암호화O)
        password 필드를 추가로 쓰지 않는다 => 추가로 작성한 password 필드는 암호화되지 않음
        '''
        
        fields = ('username',)
