from datetime import datetime, date
from django.db import models
# from django.contrib.auth.models import User
from django.utils import timezone
from accounts.models import User


club_category = (
    ('hobby','취미/교양'),
    ('study','스터디'),
    ('daily','일상'),
    ('exercise','운동'),
    ('etc','기타'),
)


class Club(models.Model):
    name = models.CharField(max_length=50, null=False)
    introduce = models.TextField(null=False)
    content = models.TextField(null=False)
    image = models.ImageField(upload_to='club', null=False)
    category = models.CharField(max_length=10, choices=club_category, default='카테고리1', null=False)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    howto = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(User, related_name='users', blank=True)

class ClubPost(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    post = models.ImageField(upload_to='club/post', null=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

class Todo(models.Model):
    id = models.AutoField(primary_key = True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 50)
    todo_date = models.DateField(null=False)
    box = models.BooleanField(default=False) #투두리스트 앞에 있는 체크박스 괄호안에 blank = false 넣어줘야하나?


