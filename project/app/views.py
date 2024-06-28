from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from  .models import Users
common=['password','12324567890','qwerty']
def index(request):
    return render(request,'index.html')
def register_view(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        bio=request.POST['bio']
        profile_pic=request.FILES.get('profile_pic')
        if User.objects.filter(username=username).exists():
            messages.error(request,'Username  already exists')
            return redirect ('register')
        elif User.objects.filter(email=email).exists():
            messages.error(request,'Email already exists')
            return redirect ('register')
        elif len(password1)<13:
            messages.error(request,'Password must contains atleast 13 words')
            return redirect ('register')
        elif password1 !=password2:
            messages.error(request,'Passwords don\'t match')
            return redirect ('register')
        elif password1 in common:
            messages.error(request,'Too common password')
            return redirect ('register')
        else:
            user=User.objects.create_user(username=username,email=email,password=password1)
            user.is_active=False
            users=Users.objects.create(user=user,bio=bio,profile_pic=profile_pic)
            user.save()
            users.save()
            messages.success(request,'Registration successfull waiting for superuser Approval')
            return redirect('wait')
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