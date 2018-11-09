from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
import sweetify
from .forms import UserForm , StudentForm, LoginForm
from .models import Semester, FeeTable

def check(user):
    if user.is_accountant == True:
        return True    
    else:
        return False

@user_passes_test(check,login_url='/dashboard')
def registration(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        student_form = StudentForm(request.POST)
        if student_form.is_valid() and user_form.is_valid():
            user = user_form.save(commit=False)
            user.save()
            print(user)
            student = student_form.save(commit=False)
            student.user = user
            student.save()
            fee_table = FeeTable.objects.create(student =  student)
            fee_table.save()
            return HttpResponseRedirect('/dashboard')
        else:
            messages.error(request,"Some Error On the Form.")
            return HttpResponse(request,'user/student_form.html')
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

