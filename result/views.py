from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from user.models import Student

@login_required
def index(request):
    return render(request, 'result/index.html')

