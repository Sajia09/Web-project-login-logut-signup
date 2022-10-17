from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout

def base(request):
    return render(request,'coupon/base.html')
def home(request):
    return render(request,'coupon/index.html')

def login(request,):
    if request.method == 'POST':
        number = request.POST['number']
        password = request.POST['password']

        user =  authenticate(request,username= number,password=password)
        if user is not None:
            auth_login(request,user)
            messages.success(request,'Successfully Logged in')
            return redirect('/index.html')
        else:
            return redirect('/home')
    return render(request,'auth/login.html')

def signup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        number = request.POST['number']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['confirmpassword']

        if(len(number)!=11):
            messages.error(request,'Number should be 11 digits')
            return  redirect('/signup')
        elif password != cpassword:
            messages.error(request,'Password and confirm password didnot match')
            return redirect('/signup')
        else:
            user = User.objects.create(username=number,email=email,password=cpassword)
            user.first_name = fname
            user.last_name = lname
            user.save()
            messages.success(request,'Your account has been successfully created')
            return redirect('/login')

    return render(request,'auth/signup.html')

def logout(request):
    auth_logout(request)
    return redirect('/')