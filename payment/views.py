from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    user = request.user
    print(user)
    return render(request,'payment/index.html')
