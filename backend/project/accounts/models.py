from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db.models.signals import post_save
from django.dispatch import receiver


# class User(AbstractUser):
#     username = models.CharField(max_length=20, unique=True)
#     email = models.EmailField(('email address'), unique=True)
#     user_image = models.ImageField(upload_to='proifle_image/', null=True, blank=True)


class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(('email address'), unique=True)
    nickname = models.CharField(max_length=100, blank=True)
    user_image = models.ImageField(upload_to='proifle_image/', null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()