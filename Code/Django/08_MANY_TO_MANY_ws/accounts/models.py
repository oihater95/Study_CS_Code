# accounts.models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth import get_user_model

class User(AbstractUser):
    # fans -> stars | stars -> fans : override
    # fans = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='stars')  => 추가 데이터 없을 때
    fans = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='stars', through='FanStar')
    # stars = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='fans', through='FanStar')  # stars를 부를 때 fans라 부름, through string으로 안쓰면 참조 안됨
    # profile_pic = models.ImageField()
    
    # friends를 부를 때 user_set으로 부름
    # 친구추가한다고 상대방 친구목록에 내가 추가되지 않음
    # friends = models.ManyToManyField('self', symmetrical=False)  # symmetrical=True: 무방향, False:방향성 있음 
    # symmetrical=True인 경우 게임 친추처럼 동시에 양쪽 친구로 등록

    def __str__(self):
        return f'{self.pk}: {self.username}'

'''
fans => 나를 따르는, stars => 내가 따르는
내 star가 추가됨 => follow

u1.stars.add(u2) 
-> 이것을 star 추가로 작성했다면 일관되게 사용할 것, u1이 u2를 follow
=> from이 누구고 to가 누구인지는 중요치 않음 처음 정한 로직을 지킬 것

중간에 u.fans.add() 섞어 쓰지 말 것


'''
# through X
# through 연결 안되어 있다면 FanStar.objects.filter(fan=u1, star=u2) 사용해야함(u1의 팔로워 찾기) => FanStar 객체 반환
# u1의 팔로잉 목록 조회 FanStar.objects.filter(fan=u1) => [<FanStar 객체 1>, <FanStar 객체 3>] 객체 리스트 => for문 돌려서 출력 => 2 tak, 3 john
# u1이 팔로잉 언제 했는지 => FanStar.objects.get(fan=u1, star=f2) => for문 돌려서 출력

# through O
# u1의 팔로잉 목록 조회 => u1.fans.all() => 2 tak, 3 john
# u1이 팔로잉 언제 했는지 => FanStar.objects.get(fan=u1, star=f2).created_at

# through를 사용하여 중개테이블 연결 => through로 연결하면 User 객체처럼 다룰 수 있음, 쿼리셋을 반환
class FanStar(models.Model):
    # 순서 필요! 자동으로 맞춰주는거 아님 위가 from_id, 아래가 to_id
    star = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='fan')
    fan = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='star')
    created_at = models.DateTimeField(auto_now_add=True)

# class Gallery(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     image = models.ImageField()

