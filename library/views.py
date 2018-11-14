from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required,user_passes_test
from user.models import Student,CustomUser,Semester
from .forms import BookForm
from django.contrib import messages
from .models import BookInstance,Books
import json
from datetime import date,timedelta

def check(user):
    if user.is_accountant == True:
        return True
    else:
        return False


@login_required
def index(request):
    if check(request.user):
        return render(request,'library/index_account.html')
    else:
        return render(request,'library/index_student.html')


def search(request):
    if request.method == "POST":
        json_str = request.body.decode(encoding='UTF-8')
        json_obj = json.loads(json_str)
        book_name = str(json_obj['book_name'])
        response_json = {'assigned_to':[], 'due_date': [], 'is_assigned':[],'uuid':[],'is_overdue':[]}
        books = Books.objects.filter(name = book_name)
        for book in books:        
                temp_book = BookInstance.objects.filter(book = book)
                for bookinstance in temp_book:
                    response_json['is_overdue'].append(bookinstance.is_overdue)
                    response_json['assigned_to'].append(str(bookinstance.assigned_to))
                    response_json['due_date'].append(str(bookinstance.due_date))
                    response_json['is_assigned'].append(bookinstance.is_assigned)
                    response_json['uuid'].append(str(bookinstance.uuid))
        return HttpResponse(json.dumps(response_json),content_type = 'application/json')
    else:
        return HttpResponseRedirect('/')



def register_book(request):
    if request.method == 'POST':
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            book = book_form.save(commit=False)
            book.save()
            for _ in range(int(book.nou_registered)):    
                book_instance = BookInstance.objects.create(book =  book)
                book_instance.save()
            book.reset()
            return HttpResponseRedirect('/library')
        else:
            messages.error(request,"Some Error On the Form.")
            return HttpResponse(request,'library/register_book.html')
    else:
        book_form = BookForm()
        return render(request, 'library/register_book.html', {'book_form':book_form})


def assign_book(request):
    if request.method == 'POST':
        json_str = request.body.decode(encoding = 'UTF-8')
        data = json.loads(json_str)
        book = BookInstance.objects.get(uuid= data['uuid'])
        user = CustomUser.objects.get(username = data['username'])
        student = Student.objects.get(user = user)
        book.assigned_to = student
        book.is_assigned = True
        book.due_date = date.today() + timedelta(days=14)
        book.save()
        response_json = { 
            'book_name': book.book.name,
            'username': data['username']
        }
        return HttpResponse(json.dumps(response_json),content_type = 'application/json')


def book_info(request,uuid): 
    response_json = {}
    try:
        book = BookInstance.objects.get(uuid= uuid)
        response_json['book_name'] = book.book.name
        response_json['author_name'] = book.book.author
        response_json['semester'] = book.book.semester
        response_json['is_overdue'] = (book.is_overdue)
        response_json['assigned_to']= (str(book.assigned_to))
        response_json['due_date'] = (str(book.due_date))
        response_json['is_assigned']= (book.is_assigned)
        response_json['uuid']=(str(book.uuid))
        if (book.is_assigned):
            response_json['username'] = book.assigned_to.user.username
        return render (request,'library/book_profile.html',response_json)
    except:
        return HttpResponse("Redirect to 404 page")


def book_returned(request):
    if request.method == 'POST':
        json_str = request.body.decode(encoding = 'UTF-8')
        data = json.loads(json_str)
        book = BookInstance.objects.get(uuid= data['uuid'])
        book.is_assigned = False 
        book.save()
        response_json = { 
            'book_name': book.book.name,
        }
        return HttpResponse(json.dumps(response_json),content_type = 'application/json')
    else:
        return HttpResponse("Redirect to 404 page")


def extend_due_date(request):
    if request.method == 'POST':
        json_str = request.body.decode(encoding = 'UTF-8')
        data = json.loads(json_str)
        book = BookInstance.objects.get(uuid= data['uuid'])
        book.due_date = book.due_date + timedelta(days=14)
        book.save()
        response_json = { 
            'book_name': book.book.name,
        }
        return HttpResponse(json.dumps(response_json),content_type = 'application/json')
    else:
        return HttpResponse("Redirect to 404 page")

def get_books(request):
    if request.method == "POST":
        json_str = request.body.decode(encoding='UTF-8')
        json_obj = json.loads(json_str)
        response_json = {'book_name':[],'author':[],'registered_units':[],'avaible_units':[],'borrowed_units':[]}
        semester = Semester.objects.get(semester = int(json_obj['semester']))
        book_set = semester.books_set.all()
        for book in book_set:    
            response_json['book_name'].append(book.name)
            response_json['author'].append(book.author)
            response_json['registered_units'].append(book.nou_registered)
            response_json['avaible_units'].append(book.nou_avaible)
            response_json['borrowed_units'].append(book.nou_borrowed)
        return HttpResponse(json.dumps(response_json),content_type = 'application/json')
    else:
        return HttpResponse("Need 404")

