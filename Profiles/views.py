from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateUserForm

# Create your views here.

def home(request):
    return render(request, "home.html")

def register(request):
    form = CreateUserForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=CreateUserForm()
        messages.success(request,'registration successful login now')
        return redirect('home')

    return render(request,'signup.html',{'form':form})
