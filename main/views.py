from django.http import request
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import Profile
import uuid
from django.conf import  settings
from django.core.mail import send_mail
from django.contrib.auth  import authenticate


def home(request):
  x=Profile.objects.filter(is_approve=True).order_by('-created_at')
  params={'data':x}
  return render(request,'index.html',params)

def sign_in(request):
  return render(request,'sign-in.html')

def login(request):
  if request.method=="POST":
    loginusername=request.POST['loginusername']
    loginpassword=request.POST['loginpassword']

    user=authenticate(username= loginusername, password= loginpassword)
    if user is not None:
      params={"text":"login successfull","color":"text-green-600",'name':loginusername}
      return render(request,"index.html",params)
    else:
        params={"text":"Invalid credentials! Please try again","color":"text-red-600"}
        return render(request,'sign-in.html',params)

  return HttpResponse("404- Not found")

def sign_up(request):
  if request.method=="POST":
    username=request.POST['username']
    email=request.POST['email']
    password=request.POST['password']
    try:
      if User.objects.filter(username=username).first():
        params={"text":"Username is already taken","color":"text-red-600"}
        return render(request,'sign-up.html',params)
      if User.objects.filter(email=email).first():
        params={"text":"Email is already in used","color":"text-red-600"}
        print(params)
        return render(request,'sign-up.html',params)

      user_obj=User.objects.create(username=username,email=email)
      user_obj.set_password(password)
      user_obj.save()
      token=str(uuid.uuid4())
      profile_obj=Profile.objects.create(user=user_obj,auth_token=token)
      profile_obj.save()
      send_mail_to_verify(email,token)
      return redirect('/token')
    except Exception as e:
      pass
  return render(request,'sign-up.html')

def success(request):
  return render(request,'success.html')
def token_send(request):
  return render(request,'token_send.html')

def verify(request , auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()

        if profile_obj:
            if profile_obj.is_approve:
                return redirect('/sign-in')
            profile_obj.is_approve = True
            profile_obj.save()
            return redirect('/success')
        else:
            return HttpResponse(
              '<center><h1>verification failed</h1></center>'
            )
            
    except Exception as e:
        print(e)
        return redirect('/')
def send_mail_to_verify(email,token):
  subject="Account verification"
  message=f"""to verify your account please click here - 
  http://127.0.0.1:8000/verify/{token}"""
  email_from = settings.EMAIL_HOST_USER
  recipient_list=[email]
  send_mail(subject,message,email_from,recipient_list)