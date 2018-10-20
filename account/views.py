from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserForm , StudentForm, LoginForm
from .models import Semester
from django.contrib.auth import authenticate, login, logout

def student_signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        student_form = StudentForm(request.POST)
        if student_form.is_valid() and user_form.is_valid():
            user = user_form.save(commit=False)
            user.is_student = True
            user.save()
            student = student_form.save()
            student.user = user
            student.save()
            return HttpResponse('New Student Registered')
        else:
            print('bad oone')
            return HttpResponseRedirect('new')
    else:
        user_form = UserForm()
        student_form =  StudentForm(initial= {'current_semester': Semester.objects.get(semester = 1)})
        print(user_form.is_valid())
        print(student_form.is_valid())
        return render(request, 'account/student_form.html', { 'user_form':user_form, 'student_form':student_form})

def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request,username= username, password=password)
            if user is not None:
                login(request,user)
                return 
            else:
                return HttpResponse('Email/Password Doesnot match.')
    else:
        login_form = LoginForm()
        print('Sent Login Form')
        return render(request, 'account/login.html',{'login_form':login_form})

def user_logout(request):
    logout(request)
    return HttpResponse('You have been loged out.')