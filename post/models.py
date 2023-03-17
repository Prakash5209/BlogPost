from django.db import models
from django.conf import settings

class Status(models.TextChoices):
    DRAFT = ('draft','DRAFT')
    PUBLIC = ('public','PUBLIC')
    

class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        abstract = True
        

class CreatePost(models.Model):
    title = models.CharField(max_length = 255,null=True,blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to = 'posts',blank=True,null=True)
    # status = models.CharField(max_length = 255,choices = Status.choices, default = Status.DRAFT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE,blank = True,null = True)
    
    def __str__(self):
        return str(self.id)
    
    @property
    def likes_count(self):
        return self.likes.filter(is_liked = True).count()
    
class GroupDiscussion(TimeStampModel):
    description = models.CharField(max_length=200,null=True,blank=True)
    post = models.ForeignKey(CreatePost,on_delete = models.CASCADE,related_name="group_chat")
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return str(self.id)
    

class Like(models.Model):
    is_liked = models.BooleanField(default=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank = True,null=True)
    post = models.ForeignKey(CreatePost,on_delete=models.CASCADE,related_name = 'likes')
    def __str__(self):
        return str(self.id)
