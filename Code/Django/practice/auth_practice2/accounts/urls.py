from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    # profile => password 다음에 username 순으로 작성!
    # UserChangeForm에서 password 변경은 ../password/ == profile/password/
    path('profile/password/', views.change_password, name='change_password'),
    path('profile/<str:username>/', views.profile, name='profile'),  # username은 unique
    # view에서 login_required와 profile.html에서 로그인 할 때만 버튼 생성하기 때문에 변수 라우팅 안함
    path('withdraw/', views.withdraw, name='withdraw'),  

]
