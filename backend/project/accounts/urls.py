from os import stat
from django.urls import path
from accounts.views import *

app_name = 'accounts'
urlpatterns = [
    path('regist', user_regist, name='regist'),
    path('login', user_login, name='login'),
    path('user_login_check', user_login_check, name='user_login_check'),
    path('myprofile', myprofile, name='myprofile'),
    path('profile_update', profile_update, name='profile_update'),
    path('club_regist/<int:club_pk>', club_regist, name='club_regist')
]