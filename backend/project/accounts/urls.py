from os import stat
from django.urls import path
from accounts.views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'accounts'
urlpatterns = [
    path('regist', user_regist, name='regist'),
    path('login', user_login, name='login'),
    path('user_login_check', user_login_check, name='user_login_check'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)