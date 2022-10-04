from email.policy import default
from django.db import models


club_category = (
    ('카테고리1','카테고리1'),
    ('카테고리2','카테고리2'),
    ('카테고리3','카테고리3'),
)

class Club(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    category = models.CharField(max_length=10, choices=club_category, default='카테고리1')
    date = models.DateField()
    