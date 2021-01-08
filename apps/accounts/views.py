# coding:utf-8

from .forms import *
from django.shortcuts import render, HttpResponse,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render
import hashlib
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt



def Account_Register(request):
    if request.method == 'GET':
        forms = Register()
        return render(request, 'accounts/register.html', {'forms': forms})
    if request.method == 'POST':
        forms = Register(request.POST)
        if forms.is_valid():
            print("form is valid ^_^** ", forms.cleaned_data)
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            User.objects.create_user(username=username, password=password)
            return HttpResponseRedirect('/accounts/login/')
        else:
            return render(request, 'accounts/register.html', locals())

def Account_Login(request):
    if request.method == "GET":
        forms = Login()
        return render(request, 'accounts/login.html', {'forms': forms})
    if request.method == "POST":
        forms = Login(request.POST)
        if forms.is_valid():
            username=forms.cleaned_data['username']
            password=forms.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            print("user:%s" % user)
            if user:
                auth.login(request,user)
                return redirect('/')
            else:
                msg = "登陆失败"
                return render(request, 'accounts/login.html', locals())

# 修改密码
def Account_Set_password(request):
    if request.method == "GET":
        forms = Register()
        return render(request, 'accounts/set_password.html', {'forms': forms})
    if request.method == "POST":
        forms = Register(request.POST)
        if forms.is_valid():
            print("cleaned_data: %s" % forms.cleaned_data)
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            try:
                user = User.objects.get(username=username)
                print("username: %s,pass: %s" % (user,password))
                if user:
                    user.set_password(password)
                    user.save()
                    print("密码修改成功！")
                    return redirect('/accounts/login/')
            except Exception as e:
                print(e)
                return HttpResponse("用户不存在")

def Account_Logout(request):
    auth.logout(request)
    return redirect('/accounts/login/')
