from django.urls import path
from chat.views import message,message_to_user

app_name = 'chat'
urlpatterns = [  
    path('',message,name="message"),
    path('message_user/<str:username>/',message_to_user,name="message_to_user"),
]