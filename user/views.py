from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import UserForm , StudentForm, LoginForm
from .models import Semester, FeeTable,CustomUser,Student
import json


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
    if request.user.is_authenticated:
        return HttpResponseRedirect('/dashboard')
    else:
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
    return HttpResponseRedirect('/')


def user_qrlogin(request):
    if request.method == "POST":
        response_json = {}
        json_str = request.body.decode(encoding='UTF-8')
        json_obj = json.loads(json_str)
        uuid = json_obj['uuid']
        try:
            user = CustomUser.objects.get(uuid = uuid)
            pin_number = json_obj['pin_number']
            if (str(pin_number) == str(user.pin_number)):
                login(request,user)
                response_json['status'] = True
                return HttpResponse(json.dumps(response_json),content_type = 'application/json')
            else:
                response_json['status'] = False
                response_json['error'] = "Sorry, The pin is invalid."
                return HttpResponse(json.dumps(response_json),content_type = 'application/json')
            
        except:
            response_json['status'] = False
            response_json['error'] = "The Scanned Qr code has no User."
            return HttpResponse(json.dumps(response_json),content_type = 'application/json')
        
@login_required
def profile_setting(request):
    if request.method == "POST":
        response_json = {}
        json_str = request.body.decode(encoding='UTF-8')
        json_obj = json.loads(json_str)
        if (json_obj['get']):
            user = request.user
            response_json ={'first_name': user.first_name,'last_name':user.last_name,'email':user.email,'pin_number':user.pin_number}
            if (user.is_student):
                student = Student.objects.get(user = user)
                response_json['phone_number'] = student.phone_number
            return HttpResponse(json.dumps(response_json),content_type = 'application/json')
        else:
            print(json_obj)
            user = CustomUser.objects.get(username = request.user.username)
            if (json_obj['first_name']):
                user.first_name = json_obj['first_name']
            if (json_obj['last_name']):
                user.last_name = json_obj['last_name']
            if (json_obj['email']):
                user.email = json_obj['email']
            if (json_obj['pin_number']):
                user.pin_number = json_obj['pin_number']
            user.save()
            if user.is_student:
                student = Student.objects.get(user = user)
                if(json_obj['phone_number']):
                    student.phone_number = json_obj['phone_number']
                student.save()
            return HttpResponse("all good")
    else:
        return render(request,'user/profile_setting.html')
                

