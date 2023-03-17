# from django import forms 
# from chat.models import Message

# class ChatForm(forms.ModelForm):
#     class Meta:
#         model = Message
#         fields = ("description",)


from django import forms
from chat.models import Message

class ChatForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ("description",)
        widgets = {
            'description':forms.TextInput(attrs={'class':'form-control'}),
        }