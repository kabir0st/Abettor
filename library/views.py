from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required,user_passes_test
from user.models import Student
from .forms import BookForm
from django.contrib import messages
from .models import BookInstance,Books
import json

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
    print('search')
    if request.method == "POST":
        print("POST")
        json_str = request.body.decode(encoding='UTF-8')
        json_obj = json.loads(json_str)
        book_name = str(json_obj['book_name'])
        response_json = {'assigned_to':[], 'due_date': [], 'is_assigned':[],'uuid':[]}
        books = Books.objects.filter(name = book_name)
        for book in books:        
                temp_book = BookInstance.objects.filter(book = book)
                for bookinstance in temp_book:
                    response_json['assigned_to'].append(bookinstance.assigned_to)
                    response_json['due_date'].append(bookinstance.due_date)
                    response_json['is_assigned'].append(bookinstance.is_assigned)
                    response_json['uuid'].append(str(bookinstance.uuid))
        print(response_json)
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
            print(book)
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
