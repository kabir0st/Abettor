from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
from user.models import CustomUser, FeeTable

@login_required
def index(request):
    if request.method == 'POST':
        json_str = request.body.decode(encoding='UTF-8')
        json_obj = json.loads(json_str)
        first_name = json_obj['first_name']
        last_name = json_obj['last_name']
        print(first_name,last_name)
        username = CustomUser.objects.get(first_name=first_name,last_name=last_name)
        if (username):
            print(username)
        else:
             print(username)   
    else:
        return render(request,'payment/index.html')

    