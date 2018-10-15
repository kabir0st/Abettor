from django.shortcuts import render

# Create your views here.

def student_signup(request):
    if request.method == 'POST':
        print('got a post request')
    else:
        print('got a get request')

def login(request):
    print('got login')
    