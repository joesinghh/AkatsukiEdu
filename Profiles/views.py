from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm, CreateTeacherForm
from django.contrib.auth.decorators import login_required
from .models import User
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

@login_required
def dashboard(request):
    user = User.objects.get(username=request.user)
    return render(request, 'HomePage.html', locals())

def about(request):
    return render(request, "about.html")

@login_required
def my_courses(request):
    return render(request, 'MyCoursesPage.html')

@login_required
def course_content(request):
    return render(request, 'Course.html')
def contact(request):
    return render(request, "contactus.html")

def terms(request):
    return render(request, "terms.html")

def privacy(request):
    return render(request, "privacy.html")
