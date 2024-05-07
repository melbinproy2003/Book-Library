from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from . models import userTable,loginTable
from django.contrib import messages, auth
from django.urls import reverse

# Create your views here.
def userregistration(request):
    logintable = loginTable()
    usertable = userTable()

    if request.method == 'POST':
        usertable.username = request.POST['username']
        usertable.email = request.POST['email']
        usertable.password = request.POST['password']
        usertable.cpassword = request.POST['cpassword']

        logintable.username = request.POST['username']
        logintable.email = request.POST['email']
        logintable.password = request.POST['password']
        logintable.cpassword = request.POST['cpassword']
        logintable.type = 'user'

        if request.POST['password'] == request.POST['cpassword']:
            usertable.save()
            logintable.save()
            messages.success(request,'Registration success')
            return redirect('login')
        else:
            messages.error(request,'Password is not matching')
            return redirect('registration')
    return render(request,'guest/signup.html')

def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # User is valid, and the password matches
            login(request, user)
            # Redirect based on user type
            if user.groups.filter(name='admin').exists():
                return redirect('webadmin')
            else:
                return redirect('userhome')
        else:
            # Authentication failed
            messages.error(request, 'Invalid username or password')

    # GET request or failed POST request
    return render(request, 'guest/signin.html')

def userhome(request):
    name = request.session['username']
    return render(request,'user/home.html',{'name':name})

def webadmin(request):
    name = request.session['username']
    return render(request,'webadmin/home.html',{'name':name})

def logout_view(request):
    logout(request)
    return redirect('login')