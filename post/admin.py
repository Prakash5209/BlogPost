from django.contrib import admin
from .models import CreatePost,GroupDiscussion

@admin.register(CreatePost)
class CreatePostAdmin(admin.ModelAdmin):
    list_display = ("description","user")
    
@admin.register(GroupDiscussion)
class GroupDiscussionAdmin(admin.ModelAdmin):
    list_display = ("description","user")