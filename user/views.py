from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import sweetify
from .forms import UserForm , StudentForm, LoginForm
from .models import Semester, FeeTable

@login_required
def registration(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        student_form = StudentForm(request.POST)
        if student_form.is_valid() and user_form.is_valid():
            user = user_form.save(commit=False)
            user.save()
            student = student_form.save(commit=False)
            student.save()
            fee_table = FeeTable.objects.create(student =  student)
            fee_table.save()
            sweetify.sweetalert(request,'StudentRegistered', text = 'New Student Had Been Added.')
            return HttpResponseRedirect('/user/new')
        else:
            sweetify.sweetalert(request,'No', text = 'One Of the box are invalid. Please Check and Try Again')
            return HttpResponseRedirect('/user/new')
    else:
        user_form = UserForm()
        student_form =  StudentForm(initial= {'current_semester': Semester.objects.get(semester = 1)})
        return render(request, 'user/student_form.html', { 'user_form':user_form, 'student_form':student_form})


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

