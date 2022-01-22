from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateUserForm

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


def dashboard(request):
    return render(request, 'HomePage.html')