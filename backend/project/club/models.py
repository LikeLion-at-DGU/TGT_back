from email.policy import default
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

club_category = (
    ('hobby','취미/교양'),
    ('study','스터디'),
    ('daliy','일상'),
    ('exercise','운동'),
    ('etc','기타'),
)

class Club(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    category = models.CharField(max_length=10, choices=club_category, default='카테고리1')
    date = models.DateField()
    howto = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ManyToManyField(User, related_name='users', blank=True)


class Todo(models.Model):
    id = models.AutoField(primary_key = True)
    club = models.OneToOneField(Club, on_delete=models.CASCADE)
    user = models.ManyToManyField(User,related_name='todo_users',blank = True)
    title = models.CharField(max_length = 50)
    box = models.BooleanField(default=False) #투두리스트 앞에 있는 체크박스 괄호안에 blank = false 넣어줘야하나?


