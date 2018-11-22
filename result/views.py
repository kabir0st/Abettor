from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from user.models import Student, Semester
from .forms import ResultForm
from .models import ReportCard,Result
import json

@login_required
def index(request):
	return render(request, 'result/index.html')

def get_sem_year(request,semester):
	if (verify_semester(semester)):
		pass
	
	
def verify_semester(sem):
	try:
		_ = Semester.objects.get(semester=sem)
		return True
	except:
		return False


def publish_result_draft(request):
	if request.method == "POST":
		result_form = ResultForm(request.POST)
		if (result_form.is_valid()):
			result = result_form.save()
			students_on_sem = Student.objects.filter(semester = result_form.cleaned_data['semester'])
			for student in students_on_sem:
				reportcard = ReportCard(student = student,result = result)
				reportcard.save()
			return render(request,'result/result_draft.html')
	else:
		resultform = ResultForm()
		return render(request, 'result/create_new_draft.html', {'result_form':resultform})


def list_draft(request,semester):
	response_json = {'date':[],'uuid':[],'semester':[]}
	if verify_semester(semester):
		result_list = Result.objects.filter(semester = semester)
		for result in result_list:
			response_json['date'].append(result.date)
			response_json['uuid'].append(result.uuid)
			response_json['semester'].append(str(result.semester))
		return render('list_draft.html',response_json)

def show_draft(request):
	if request.method == "POST":
		json_str = request.body.decode(encoding='UTF-8')
		json_obj = json.loads(json_str)
		pass