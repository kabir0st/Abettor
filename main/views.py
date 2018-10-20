from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'main/home.html')

def dashboard(request):
    return HttpResponse('youare in the dashboard')