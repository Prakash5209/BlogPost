from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class usernotes(models.Model):
    # user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    description = models.TextField()