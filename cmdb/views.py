#!/usr/bin/env python3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import  auth

@login_required
def index(request):
    print(auth.get_user(request),auth._get_user_session_key(request))
    return render(request, 'index.html')