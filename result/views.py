from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from user.models import Student, Semester, Subject
from .forms import ResultForm
from .models import ReportCard,Result, Marks
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
			sem = result_form.cleaned_data['semester']
			semester = Semester.objects.get(semester = 1)
			students_on_sem = Student.objects.filter(semester = semester)
			subject_list = Subject.objects.filter(semester = semester)
			for student in students_on_sem:
				reportcard = ReportCard(student = student,result = result)
				reportcard.save()
				for subject in subject_list:
					mark = Marks(reportcard = reportcard,subject = subject)
					mark.save()
			return render(request,'result/add_marks.html')
	else:
		resultform = ResultForm()
		return render(request, 'result/create_new_draft.html', {'result_form':resultform})


def show_draft(request,semester,pk):
	if request.method == "POST":
		json_str = request.body.decode(encoding='UTF-8')
		json_obj = json.loads(json_str)
		pk = json_obj['pk']
		print(json_obj['semester'])
		semester =Semester.objects.get(semester = int(json_obj['semester']))
		result = Result.objects.get(id = pk)
		response_json = {'subjects':[],'reportcard':[]}
		response_json['date'] = str(result.date)
		response_json['more_info'] = (result.more_info)
		response_json['semester']= (str(result.semester))
		reportcards = ReportCard.objects.filter(result = result)
		subjects = Subject.objects.filter(semester = semester )
		for subject in subjects:
			response_json['subjects'].append(subject.name)
		for reportcard in reportcards:
			temp_json = {}
			temp_json['student_name'] = (str(reportcard.student))
			temp_json['student_username'] = (str(reportcard.student.user.username))
			for subject in subjects:
				mark = Marks.objects.get(subject = subject, reportcard = reportcard)
				temp_json[str(subject)]  = mark.mark
				print(mark.mark)
			response_json['reportcard'].append(temp_json)
		return HttpResponse(json.dumps(response_json),content_type = 'application/json')
	else:
		response_json = {'semester':semester,'pk':pk}
		return render(request,'result/result.html',response_json)


def list_draft(request,semester):
	if request.method == "POST":
		response_json = {'date':[],'more_info':[],'semester':[],'pk':[]}
		if verify_semester(semester):
			result_list = Result.objects.filter(semester = semester)
			for result in result_list:
				response_json['date'].append(str(result.date))
				response_json['more_info'].append(str(result.more_info))
				response_json['semester'].append(str(result.semester))
				response_json['pk'].append(str(result.id))	
		return HttpResponse(json.dumps(response_json),content_type = 'application/json')
	else:
		response_json = {'semester':semester}
		return render(request,'result/list_draft.html',response_json)
