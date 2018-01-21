# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from meetup.forms import UserForm
# Create your views here.


def index(request):
    temp = 'meetup/index.html'
    return render(request,temp,{})


def register(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.user = request.user
            user.set_password(user.password)
            user.save()
            registered = True
            if registered == True:
                return HttpResponseRedirect('/meetup/login/')
            else:
                return HttpResponse("Username already in use.")
    else:
        user_form = UserForm()
    return render(request,'meetup/register.html',{})
