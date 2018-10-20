from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import sweetify


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/dashboard')
            else:
                messages.error(request,'Username or Password is not correct.')
                return HttpResponseRedirect('login')           
    else:
        form = LoginForm()
        return render (request, 'user/login.html',{'form':form})


@login_required
def user_logout(request):
    logout(request)
    sweetify.sweetalert(request,'LogedOut', text = 'You Have Successfully loged Out.')
    return HttpResponseRedirect('/')
