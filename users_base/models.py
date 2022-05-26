from django.db import models
from django.contrib.auth.models import AbstractUser

def user_profile_path(instance, filename):
    return 'user/{0}/{1}'.format(instance.user.id, filename)
class User(AbstractUser):
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to=user_profile_path, default="avatar.png")

    username = models.EmailField("email adress", unique=True)
    REQUIRED_FIELDS = []