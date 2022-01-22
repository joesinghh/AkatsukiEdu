from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm, CreateTeacherForm

# Create your views here.

def home(request):
    return render(request, "index.html")

def register(request):
    form = CreateUserForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=CreateUserForm()
        return redirect('login')

    return render(request,'SignUpPage.html',{'form':form})

def tregister(request):
    form = CreateTeacherForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.is_teacher = True
        obj.is_verified = False
        obj.save()
        form=CreateTeacherForm()
        return redirect('login')

    return render(request,'TeacherSignUp.html',{'form':form})


def dashboard(request):
    return render(request, 'HomePage.html')

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contactus.html")
