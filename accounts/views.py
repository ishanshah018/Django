from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required



# Create your views here.

def signupaccount(request):
    if request.method=="GET":
        return render(request,'signupaccount.html',{'form':UserCreationForm})
    else:
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('home')
            except IntegrityError:
                return render(request,'signupaccount.html',{'form':UserCreationForm,'error':'Username already exists, Choose new Usewrname'})
        else:
            return render(request,'signupaccount.html',{'form':UserCreationForm,'error':"Passwords does not match"})
        
@login_required        
def logoutaccount(request):
    logout(request)
    return redirect('home')

def loginaccount(request):
    if request.method=="GET":
        return render(request,"loginaccount.html",{'form':AuthenticationForm})
    else:
        user=authenticate(username=request.POST['username'],password=request.POST['password'])
        
        if user is None:
            return render(request,'loginaccount.html',{'form':AuthenticationForm(),'error':"Username and password does not match"})
        else:
            login(request,user)
            return redirect('home')