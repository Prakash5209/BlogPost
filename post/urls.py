from django.urls import path
from post.views import home, createpost, selectedTopic, editTopic, delete_post,like_post

app_name = 'post'
urlpatterns = [
    path('',home,name='home'),
    path('create-post/',createpost,name="createpost"),
    path('topic/<int:pk>/',selectedTopic,name="selectedTopic"),
    path('edit-topic/<int:pk>/',editTopic,name="editTopic"),
    path('delete-post/<int:pk>/',delete_post,name='deletepost'),
    path('like-post/<int:postid>/',like_post,name="like_post"),
]
