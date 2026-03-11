from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib import messages
from .models import Contact,Category,Momo,EmailVerfication,Testemonials
from django.core.mail import send_mail
from django.template.loader import render_to_string
from datetime import datetime
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib.auth.decorators import login_required
import qrcode
import re
import random
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.forms import PasswordChangeForm
User=get_user_model()
# Create your views here.
def index(request):
    category= Category.objects.all()
    cateid=request.GET.get('category')
    if cateid=='all':
        momo=Momo.objects.filter(is_available=True)
    elif cateid:
        momo= Momo.objects.filter(category=cateid,is_available=True)
    else:
        momo=Momo.objects.filter(is_available=True)
    if request.method== "POST":
        
        name= request.POST.get("name")
        phone= request.POST.get("phone")
        email= request.POST.get("email")
        message= request.POST.get("message")

        try:
            user= Contact(name=name,phone=phone,email=email,message=message)
            user.full_clean()
            user.save()

            subject = "Thank You for Your Valuable Feedback"
            message = render_to_string('core/mail.html',{'name':name,'date':datetime.now()})
            from_email='anisholi751106@gmail.com'
            recipient_list=[email,'anisholi751106@gmail.com']

            send_mail(subject=subject, message=message,from_email=from_email,recipient_list=recipient_list,fail_silently=False)
            messages.success(request, 'Form submitted successfully !!! Check your mail')
            return redirect('index')
        except Exception as e:
            messages.error(request,e)
            return redirect('index')
    context= {
            'category':category,
            'momo':momo,
            'cateid':cateid

        }
    return render(request,'core/index.html',context)


@login_required(login_url='log_in')
def about(request):
    return render(request,'core/about.html')

login_required(login_url='log_in')
def contact(request):
    return render(request,'core/contact.html')
@login_required(login_url='log_in')
def menu(request):
    category= Category.objects.all()
    qr =qrcode.make(f'http://127.0.0.1:8000/{request.path}')
    qr.save('core/static/images/qr.png') 
    context={
        'category':category
    }
    return render(request,'core/menu.html',context)

def service(request):
    return render(request,'core/services.html')

def testemonial(request):
    testemonial= Testemonials.objects.all()
    context={
        'testemonial':testemonial
    }
    return render(request,'core/testemonial.html',context)


"""
==========================================================================
==========================================================================
                      Auth part
===========================================================================
=========================================================================
"""
def register(request):

    if request.method == "POST":
        fname= request.POST.get('fname')
        lname= request.POST.get('lname')
        username= request.POST.get('username')
        email= request.POST.get('email')
        password= request.POST.get('password')
        password1= request.POST.get('password1')

        if password == password1:

            if User.objects.filter(username=username).exists():
                messages.error(request,'Username already exists')
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.error(request,'Email already exists')
                return redirect('register')
            
            if not re.search(r'[A-Z]',password):
                messages.error(request,'password doesnot contain upper case')
                return redirect('register')
            if not re.search(r'\d',password):
                messages.error(request,'password doesnot contain Digit')
                return redirect('register')
            
            if username.lower() in password.lower():
                messages.error(request,'password should not be username')
                return redirect('register')
            if not re.search(r'\W',password):
                messages.error(request,"no special character")
                return redirect('register')
            try:
                user= User(username=username,first_name=fname,email=email)
                validate_password(password,user=user)

                user= User.objects.create_user(first_name=fname,last_name=lname,username=username,email=email,password=password,is_active=False)
                token =str(random.randint(10000,999999))
                request.session['email']=email
                EmailVerfication.objects.create(user=user,token=token)
                subjects="Email Verification"
                message=f'Dear {username} you email verification code is {token}'
                from_email="anisholi751106@gmail.com"
                recipient_list=[email]
                send_mail(subject=subjects,message=message,from_email=from_email,recipient_list=recipient_list,fail_silently=False)
                messages.success(request, "you account is register successfully and verify email !!!!")
                return redirect('email_verify')
            except ValidationError as e:
                for error in e.messages:
                    messages.error(request,error)
                return redirect('register')
                   
        else:
            messages.error(request, "Password doesnot match")
            return redirect('register')
    return render(request,'accounts/register.html')


def log_in(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        username= request.POST.get('username')
        password= request.POST.get('password')
        remember_me= request.POST.get('remember_me')

        if not User.objects.filter(username=username).exists():
            messages.error(request,"This username doesnot exits try again")
            return redirect('log_in')
        u= User.objects.get(username=username)
        if not  u.is_active:
            messages.error(request, "first verify your email")
            return redirect('email_verify')

        user= authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            if remember_me:
                request.session.set_expiry(3600)
            else:
                request.session.set_expiry(0)
            messages.success(request,f"Welcome back!!! {request.user.username}")

            next= request.POST.get('next','')
            
            return redirect(next if next else 'index')
        else:
            messages.error(request,'Incorrect password try again')
            return redirect('log_in')
        
    next = request.GET.get('next','')
    return render(request,'accounts/login.html',{'next':next})


def log_out(request):
    logout(request)
    return redirect('log_in')

def verify_email(request):
    if request.method == "POST":
        email= request.session['email']
        token= request.POST.get('token')

        try:
            user=User.objects.get(email=email)
            email_verify = EmailVerfication.objects.get(user=user,token=token)
            if timezone.now() >email_verify.is_created + timedelta(minutes=5):
                messages.error(request,"Token Expired")
                email_verify.delete()
                return redirect('email_verify')
            user.is_active=True
            user.save()
            email_verify.delete()
            del request.session['email']
            #request.session.pop('email')
            #request.session.flush()
            #request.session.clear()
            return redirect('log_in')
        except User.DoesNotExist:
            messages.error(request,'Email doesnot exists')
            return redirect("email_verify")
        except EmailVerfication.DoesNotExist:
            messages.error(request, "Token invalid")
            return redirect("email_verify")
        
            
    return render(request, "accounts/email_verify.html")


def password_change(request):
    form=PasswordChangeForm(user=request.user)
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('log_in')
    return render(request,'accounts/password_change.html',{'form':form})

