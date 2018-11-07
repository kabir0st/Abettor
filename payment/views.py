from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
from user.models import CustomUser, FeeTable,Student
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

    