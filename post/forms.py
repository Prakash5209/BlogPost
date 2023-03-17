from django import forms 
from .models import CreatePost,GroupDiscussion

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = CreatePost
        fields = ("title","description","image",)
        widgets = {
            'title':forms.TextInput(attrs={'class':'createpost-form'}),
            'description':forms.TextInput(attrs={'class':'createpost-description'}),
        }
        
class GroupDiscussionForm(forms.ModelForm):
    class Meta:
        model = GroupDiscussion
        fields = ("description",)
        widgets = {
            'description':forms.TextInput(attrs={'class':'form-control'}),
        }
        