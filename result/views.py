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
			semester = Semester.objects.get(semester = result_form.cleaned_data['semester'])
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


def show_darft(request):
	if request.method == "POST":
		json_str = request.body.decode(encoding='UTF-8')
		json_obj = json.loads(json_str)
		pk = json_obj['pk']
		semester = json_obj['semester']
		result = Result.objects.get(id = pk)
		response_json = {'subjects':[],'reportcard_detail':{'student_name':"",'student_username':"",'marks':[]}}
		response_json['date'].append(result.date)
		response_json['more_info'].append(result.more_info)
		response_json['semester'].append(str(result.semester))
		reportcards = ReportCard.objects.get(result = result)
		subjects = Subject.objects.get(semester = semester )
		for subject in subjects:
			response_json['subjects'].append(subject.name)
		for reportcard in reportcards:
			response_json['reportcard_detail']['student_name'] = str(reportcard.student)
			response_json['reportcard_detail']['student_username'] = str(reportcard.student.user.username)
			for subject in subjects:
				mark = Marks.objects.get(subject = subject, reportcard = reportcard)
				response_json['reportcard_detail']['marks'].append(mark)
		return render('result/show_darft.html',response_json)
	else:
		return render(request,'/')


def list_draft(request,semester):
	response_json = {'date':[],'more_info':[],'semester':[],'pk':[]}
	if verify_semester(semester):
		result_list = Result.objects.filter(semester = semester)
		for result in result_list:
			response_json['date'].append(result.date)
			response_json['more_info'].append(result.more_info)
			response_json['semester'].append(str(result.semester))
			response_json['pk'].append(result.id)
		return render(request,'list_draft.html',response_json)