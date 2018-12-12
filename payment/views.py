from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
import json
from user.models import CustomUser, FeeTable,Student,Semester
from django.http import HttpResponse, HttpResponseRedirect
import requests

def check(user):
	if user.is_accountant == True:
		return True
	else:
		return False

@login_required
def index(request):
	if request.user.is_accountant == True:
		return render(request,'payment/index_accountant.html')
	elif request.user.is_student == True:
		username = request.user.username
		data = get_info_student(username)
		return render(request,'payment/index_student.html',data)
	else:
		return HttpResponse('wtf')

@user_passes_test(check,login_url='/')
def search(request):
	if request.method == "POST":
		json_str = request.body.decode(encoding='UTF-8')
		json_obj = json.loads(json_str)
		if(json_obj['qr']):
			uuid = json_obj['uuid']
			users = CustomUser.objects.filter(uuid = uuid,is_student=True)
		else:
			first_name = str(json_obj['first_name'])
			last_name = str(json_obj['last_name'])
			users = CustomUser.objects.filter(first_name=first_name,last_name = last_name, is_student= True)    

		response_json = {'username':[], 'name': [], 'semester':[] }
		for user in users:
			student = Student.objects.get(user = user)
			response_json['username'].append(user.username)
			response_json['name'].append(user.first_name + " " + user.last_name)
			response_json['semester'].append(str(student.semester))
		return HttpResponse(json.dumps(response_json),content_type = 'application/json')
	else:
		return HttpResponseRedirect('/')


@user_passes_test(check,login_url='/')
def get_info(request,username):
	user = CustomUser.objects.get(username = username)
	student = Student.objects.get(user = user)
	feetable = FeeTable.objects.get(student = student)
	paid_till_now  = feetable.paid_till_now
	whole_fee = 0
	all_sem = Semester.objects.all()
	for x in all_sem:
		whole_fee = whole_fee + x.fee
		if( x  == student.semester):
			break
	temp = whole_fee - paid_till_now
	dues = 0
	credit = 0
	if (temp > 0 ):
		dues = temp
	else: 
		credit = -temp
	data = {
		'uuid': user.uuid,
		'username': username,
		'name': user.first_name + " " + user.last_name,
		'current_semester': str(student.semester),
		'dues':dues,
		'credits':credit,
	}
	return render(request,'payment/profile.html',data)


@user_passes_test(check,login_url='/')
def pay(request,username):
	if request.method == "POST":
		json_str =  request.body.decode(encoding = 'UTF-8')
		json_obj = json.loads(json_str)
		username = json_obj['username']
		amount = json_obj['amount']
		pay_db(username,amount)
		return HttpResponseRedirect('/payment/'+username)

	else:
		return HttpResponseRedirect('/')

def get_info_student(username):
	user = CustomUser.objects.get(username = username)
	student = Student.objects.get(user = user)
	feetable = FeeTable.objects.get(student = student)
	paid_till_now  = feetable.paid_till_now
	whole_fee = 0
	all_sem = Semester.objects.all()
	for x in all_sem:
		whole_fee = whole_fee + x.fee
		if( x  == student.semester):
			break
	temp = whole_fee - paid_till_now
	dues = 0
	credit = 0
	if (temp > 0 ):
		dues = temp
	else: 
		credit = -temp
	data = {
		'uuid': user.uuid,
		'username': username,
		'name': user.first_name + " " + user.last_name,
		'current_semester': str(student.semester),
		'dues':dues,
		'credits':credit,
	}
	return data


def verify_khalti(request):
	report = {}
	if request.method == 'POST':
		json_str = request.body.decode(encoding='UTF-8')
		json_obj = json.loads(json_str)
		amount = json_obj['amount']
		token = json_obj['token']
		username = request.user.username
		url = "https://khalti.com/api/v2/payment/verify/"
		payload = {
		"token": token,
		"amount": amount
		}
		headers = {
		"Authorization": "Key test_secret_key_36c4ba1d1af34d2c901a2a11493c16b3"
		}
		response = requests.post(url, payload, headers = headers)
		if (str(response) == '<Response [200]>'):
			amount = amount/100
			pay_db(username,amount)
			report['status'] = True
			report['description'] = 'Payment is sucessful'
		else:
			report['status'] = False
			report['description'] = 'Payment failed'
	return HttpResponse(json.dumps(report), content_type="application/json")

def pay_db(username,amount):
	try:
		user = CustomUser.objects.get(username = username)
		x = Student.objects.get(user = user)
		feetable = FeeTable.objects.get(student = x)
		feetable.paid_till_now = int(feetable.paid_till_now) + int(amount)
		feetable.save()
		return True
	except:
		return False