from .models import User, Course, Chapter
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
             
        ]

class CreateTeacherForm(UserCreationForm):
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
            'document'
            
        ]

class Login(AuthenticationForm):
    username=forms.CharField(label=None,widget=TextInput(attrs={'class':'validate','placeholder':'Username'}))
    password=forms.CharField(label=None,widget=PasswordInput(attrs={'class':'password','placeholder':'Password'}))

    
# class CourseCreateView(CreateView,LoginRequiredMixin):
#     model=Course
#     fields=[
#         'cover',
#         'title',
#     ]
#     def form_valid(self,form):
#         form.instance.author=self.request.user
#         return super().form_valid(form)