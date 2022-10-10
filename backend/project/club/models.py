from email.policy import default
from pyexpat import model
from statistics import mode
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
    introduce = models.TextField()
    content = models.TextField()
    category = models.CharField(max_length=10, choices=club_category, default='카테고리1')
    start_date = models.DateField()
    end_date = models.DateField()
    howto = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ManyToManyField(User, related_name='users', blank=True)
    post = models.CharField(max_length=200, null=True, blank=True)
