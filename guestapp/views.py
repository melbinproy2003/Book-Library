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
        
        # Manually authenticate the user
        try:
            user = loginTable.objects.get(username=username, password=password)
            # Check user type
            if user.type == 'admin':
                request.session['username'] = user.username
                return redirect('webadmin')
            else:
                request.session['username'] = user.username
                return redirect('userhome')
        except loginTable.DoesNotExist:
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