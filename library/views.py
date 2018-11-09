from django.shortcuts import render
from django.contrib.auth.decorators import login_required


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

