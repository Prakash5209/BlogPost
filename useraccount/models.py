from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class User(AbstractUser):
    pass

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    contact = models.CharField(max_length=10,blank=True,null=True)
    address = models.CharField(max_length=255,blank=True,null=True)
    avatar = models.ImageField(upload_to="profile", blank = True, null = True)
    bio = models.TextField(blank=True,null = True)
    
    def __str__(self):
        return str(self.user)