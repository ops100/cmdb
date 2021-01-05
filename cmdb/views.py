#!/usr/bin/env python3
#coding: utf-8
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import  auth
import logging
from apps.accounts.forms import Login

@login_required
def index(request):
    print(auth.get_user(request),auth._get_user_session_key(request))
    logging.info(request)
    return render(request, 'index.html')


def test(request):
    if request.method == "GET":
        forms = Login()
        return render(request, 'test.html', {'forms': forms})
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
                return render(request, 'test.html', locals())