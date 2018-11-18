from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from user.models import Student, Semester

@login_required
def index(request):
    return render(request, 'result/index.html')

def get_sem_year(request,semester):
    if (verify_semester(semester)):
        pass
    
    
def verify_semester(sem):
    try:
        x = Semester.objects.get(semester=sem)
        return True
    except:
        return False