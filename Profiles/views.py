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

@login_required
def UserListView(request):
    user=User.objects.get(username=request.user)
    post=UserPost.objects.filter(artist=request.user)
    # following_ = Following.objects.get(user=request.user) 
    total=len(post)
    profile = Profile.objects.get(user=user)
    following_obj = Following.objects.get(user = user)
    follower,following = following_obj.follower.count(), following_obj.following.count()
    
    return render(request,'profile.html',locals())