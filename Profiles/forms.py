from .models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from validate_email import validate_email
from django.forms.widgets import PasswordInput,TextInput
import requests

class CreateUserForm(UserCreationForm):
    email=forms.EmailField(widget=TextInput(attrs={'placeholder':'Email'}),required=True)
    username=forms.CharField(widget=TextInput(attrs={'class':'validate','placeholder':'Username'}))
    password1=forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}))
    password2=forms.CharField(widget=PasswordInput(attrs={'placeholder':'Confirm Password'}))
    class Meta:
        model=User
        fields=[
            'username',
            'email',
            'password1',
            'password2',
            'is_teacher'
            
        ]
    def clean_email(self,*args,**kwargs):
        cleaned_data = super(CreateUserForm, self).clean()
        email = cleaned_data.get("email")
        
        response = requests.get("https://apilayer.net/api/check?access_key=a448482d0743db46d06084a7c97f32c9&email={}".format(email))
        dic = response.json()
        if dic['smtp_check']==True and dic['format_valid']==True and dic['mx_found']==True:
            return email
        else:
            raise forms.ValidationError("Invalid Email")