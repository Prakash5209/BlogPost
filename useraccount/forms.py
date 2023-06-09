from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from useraccount.models import Profile

User = get_user_model()

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username","password1","password2")   
        

class ProfileForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()
    class Meta:
        model = Profile
        fields = ("first_name","last_name","email","contact","address","avatar","bio",)
        widgets = {
            'contact':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'avatar':forms.TextInput(attrs={'class':'form-control'}),
            'bio':forms.TextInput(attrs={'class':'form-control'}),
        }
        
class CustomLoginForm(AuthenticationForm):
    pass