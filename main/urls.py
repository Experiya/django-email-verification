# from django_email_verification import urls as mail_urls
from django.shortcuts import render
from django.urls import path, include
from .import views

urlpatterns=[
    path('',views.home,name='home'),
    path('sign-in',views.sign_in,name='sign_in'),
    path('login',views.login,name='sign_up'),
    path('sign-up',views.sign_up,name='sign_up'),
    path('success',views.success,name='verified'),
    path('token',views.token_send,name='token'),
    path('verify/<auth_token>',views.verify,name='check'),
]