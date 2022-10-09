from email.policy import default
from django.db import models


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
    
    