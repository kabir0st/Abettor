from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
from user.models import CustomUser, FeeTable,Student,Semester
from django.http import HttpResponse, HttpResponseRedirect



@login_required
def index(request):
    return render(request,'payment/index.html')

def search(request):
    if request.method == "POST":
        json_str = request.body.decode(encoding='UTF-8')
        json_obj = json.loads(json_str)
        first_name = str(json_obj['first_name'])
        last_name = str(json_obj['last_name'])
        response_json = {'username':[], 'name': [], 'semester':[] }
        users = CustomUser.objects.filter(first_name=first_name,last_name = last_name, is_student= True)
        for user in users:
            student = Student.objects.get(user = user)
            response_json['username'].append(user.username)
            response_json['name'].append(user.first_name + " " + user.last_name)
            response_json['semester'].append(str(student.current_semester))
        return HttpResponse(json.dumps(response_json),content_type = 'application/json')
    else:
        return HttpResponseRedirect('/')

def get_info(request,username):
    user = CustomUser.objects.get(username = username)
    student = Student.objects.get(user = user)
    feetable = FeeTable.objects.get(student = student)
    paid_till_now  = feetable.paid_till_now
    whole_fee = 0
    all_sem = Semester.objects.all()
    for x in all_sem:
        whole_fee = whole_fee + x.fee
        if( x  == student.current_semester):
            break
    temp = whole_fee - paid_till_now
    dues = 0
    credit = 0
    if (temp > 0 ):
        dues = temp
    else: 
        credit = -temp
    data = {
        'username': username,
        'name': user.first_name + " " + user.last_name,
        'current_semester': str(student.current_semester),
        'dues':dues,
        'credits':credit,
    }
    return render(request,'payment/profile.html',data)

def pay(request,username):
    if request.method == "POST":
        json_str =  request.body.decode(encoding = 'UTF-8')
        json_obj = json.loads(json_str)
        username = json_obj['username']
        amount = json_obj['amount']
        user = CustomUser.objects.get(username = username)
        x = Student.objects.get(user = user)
        feetable = FeeTable.objects.get(student = x)
        feetable.paid_till_now = int(feetable.paid_till_now) + int(amount)
        feetable.save()
        return HttpResponseRedirect('/payment/'+username)
    else:
        return HttpResponseRedirect('/')


        