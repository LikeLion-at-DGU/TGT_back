from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(('email address'), unique=True)
    user_image = models.ImageField(upload_to='users', null=True)
    
