from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import login
urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.register, name='signup'),
    path('login',auth_views.LoginView.as_view(template_name='LoginPage.html',authentication_form=login),name='login')

]
