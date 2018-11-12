from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required,user_passes_test
from user.models import Student,CustomUser
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
            book.nou_avaible = book_form['nou_registered']
            book.save()
            for _ in range(int(book.nou_registered)):    
                book_instance = BookInstance.objects.create(book =  book)
                book_instance.save()
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
        print(data)
        name = str(data['full_name']).split(" ")
        print(name)
        if (name.__len__() > 2):
            return 0
        else:
            book = BookInstance.objects.get(uuid= data['uuid'])
            user = CustomUser.objects.get(first_name = name[0], last_name = name[1])
            student = Student.objects.get(user = user)
            book.assigned_to = student
            book.is_assigned = True
            book.due_date = date.today() + timedelta(days=14)
            book.save()
            response_json = { 
                'book_name': book.book.name,
                'full_name': data['full_name']
            }
            return HttpResponse(json.dumps(response_json),content_type = 'application/json')

def book_info(request,uuid): 
    response_json = {}
    book = BookInstance.objects.get(uuid= uuid)
    response_json['book_name'] = book.book.name
    response_json['author_name'] = book.book.author
    response_json['semester'] = book.book.semester
    response_json['is_overdue'] = (book.is_overdue)
    response_json['assigned_to']= (str(book.assigned_to))
    response_json['due_date'] = (str(book.due_date))
    response_json['is_assigned']= (book.is_assigned)
    response_json['uuid']=(str(book.uuid))
    return render (request,'library/book_profile.html',response_json)