from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,logout
def index(request):
    return render(request,'index.html')
def register_view(request):
    return render(request,'register.html')
def login_view(request):
    return render(request,'login.html')
def wait(request):
    return render(request,'wait.html')
def superuser(request):
    return render(request,'superuser.html')
def userprofile(request):
    return render(request,'userprofile.html')
def logout(request):
    return redirect('index')