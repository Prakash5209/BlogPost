# from django.db import models
# from django.conf import settings

# class Message(models.Model):
#     description = models.CharField(max_length=255)
#     from_user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE,null = True,blank= True,related_name = "send_message")
#     to_user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE,null = True,blank = True,related_name = "received_message")
    
#     def __str__(self):
#         return str(self.id)


from django.db import models
from django.conf import settings

class Message(models.Model):
    description = models.TextField()
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='send_messages')
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='received_messages')
    def __str__(self):
        return str(self.id)
    
    
    