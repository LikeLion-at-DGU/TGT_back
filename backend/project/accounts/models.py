from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractBaseUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(('email address'), unique=True)
    # user_image = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.username


class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(('email address'), unique=True)
    nickname = models.CharField(max_length=100, blank=True)
    user_image = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField(null=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()