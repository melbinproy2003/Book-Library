from django.contrib.auth import logout
from django.shortcuts import render, redirect
from . models import userTable,loginTable
from django.contrib import messages, auth

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
        Luser=loginTable.objects.filter(username=username,password=password,type='user').exists()
        # try:
        if Luser is not None:
                Luser_details = loginTable.objects.get(username=username,password=password)
                Luser_name = Luser_details.username
                type = Luser_details.type
                if type == 'user':
                    request.session['username']=Luser_name
                    return redirect('userhome')
                elif type == 'admin':
                    request.session['username'] = Luser_name
                    return redirect('webadmin')
        else:
                messages.error(request,'invalid username or password')
        # except:
        #     messages.error(request,'in the exception')
    return render(request,'guest/signin.html')

def userhome(request):
    name = request.session['username']
    return render(request,'user/home.html',{'name':name})

def webadmin(request):
    name = request.session['username']
    return render(request,'webadmin/home.html',{'name':name})

def logout_view(request):
    logout(request)
    return redirect('login')