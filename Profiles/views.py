from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm, CreateTeacherForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
# Create your views here.
from .forms import CreateTeacherForm

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
        form.save()
        form=CreateTeacherForm()
        return redirect('login')

    return render(request,'TeacherSignUp.html',{'form':form})

@login_required
def dashboard(request):
    user = User.objects.get(username=request.user)
    posts = Course.objects.all()
    return render(request, 'HomePage.html', locals())

def about(request):
    return render(request, "about.html")

@login_required
def my_courses(request):
    user = User.objects.get(username=request.user)
    return render(request, 'MyCoursesPage.html', locals())

@login_required
def course_content(request, pk):
    scourse = Course.objects.get(id=pk)
    user = User.objects.get(username=request.user)
    return render(request, "Course.html", locals())

def contact(request):
    return render(request, "contactus.html")

def terms(request):
    return render(request, "terms.html")

def browsecourses(request):
    return render(request, "BrowseCourses.html")


def privacy(request):
    return render(request, "privacy.html")

class CourseCreateView(CreateView,LoginRequiredMixin):
    model=Course
    fields=[
        'cover',
        'title',
        
    ]
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)


class CourseUpdateView(UpdateView,LoginRequiredMixin):
    model=Course
    fields=[
        'cover' 
    ]

class CourseDeleteView(DeleteView,LoginRequiredMixin):
    model=Course
    template_name=''
    success_url='/dashboard'

