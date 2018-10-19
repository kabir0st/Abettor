from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserForm , StudentForm
from .models import Semester
# Create your views here.

def student_signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        student_form = StudentForm(request.POST)
        print(student_form['phone_number'])
        if student_form.is_valid() and user_form.is_valid():
            print('Given Data is valid')
            user = user_form.save(commit=False)
            print(user.username)
            # user.save()
            # student_form.save()
            
            return HttpResponse('Good')
        else:
            print('bad oone')
            return HttpResponseRedirect('login')
    else:
        user_form = UserForm()
        student_form =  StudentForm(initial= {'current_semester': Semester.objects.get(semester = 1)})
        return render(request, 'account/student_form.html', { 'user_form':user_form, 'student_form':student_form})

def login(request):
    if request.method == 'POST':
        print('Login Requested')
    else:
        return render(request, 'account/login.html')