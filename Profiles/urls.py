from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .forms import Login
urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.register, name='signup'),
    path('tsignup', views.tregister, name='tsignup'),
    path('login',auth_views.LoginView.as_view(template_name='LoginPage.html',authentication_form=Login),name='login'),
    path('home', views.dashboard, name='dashboard'),

    path('mycourses',),
    path('course<int:pk>',),

] 
