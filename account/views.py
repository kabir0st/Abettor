from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import StudentRegistrationForm

# Create your views here.

def student_signup(request):
    if request.method == 'POST':
        student_form = StudentRegistrationForm(request.POST)
        if student_form.is_valid():
            print('Given Data is valid')
            pass
        else:
            print('bad oone')
            return HttpResponseRedirect('login')
    else:
        student_form =  StudentRegistrationForm()
        return render(request, 'account/student_form.html', {'form':student_form})

def login(request):
    if request.method == 'POST':
        print('Login Requested')
    else:
        return render(request, 'account/login.html')