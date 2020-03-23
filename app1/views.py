from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User,auth
from django.shortcuts import render,redirect
from .models import registration
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib import messages

def index(request):
    return  render (request,'index.html')

def about(request):
    return  render (request,'about.html')

def course(request):
    return  render (request,'course.html')

def element(request):
    return  render (request,'element.html')

def contact(request):
    return  render (request,'contact.html')

def register(request):
    if request.method == 'POST':
        mobile = request.POST['mobile']
        email = request.POST['email']
        pwd = request.POST['pwd']
        if registration.objects.filter(mobile=mobile).exists():
            messages.info(request,'Phone Number Already Exist !!!!')
            return redirect('register')
        elif registration.objects.filter(email=email).exists():
             messages.info(request, 'Email Already Exist !!!!')
             return redirect('register')
        else:
            user=registration(mobile=mobile,email=email,pwd=pwd)
            user.save()
            messages.info(request, 'Registered Successfully !!!!')
            return redirect('register')
    return redirect('index')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        pwd = request.POST['pwd']
        if registration.objects.filter(email=email).filter(pwd=pwd).exists():
            info = registration.objects.get(email=email)
            request.session['user'] = email
            #return render(request, 'alogin.html',{'stdinfo':stdinfo})
            return HttpResponse("Login Success")
        else:
            return render(request, 'login.html', {'error': "Invalid Login Credentials"})
    else:
        return render(request,'login.html')