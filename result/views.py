from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from user.models import Student, Semester
from .forms import ResultForm


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


def publish_result(request):
	if request.method == "POST":
			pass
	else:
		resultform = ResultForm()
		return render(request, 'result/publish_result.html', {'result_form':resultform})
