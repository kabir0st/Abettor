from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name = 'login'),
    path('student/new',views.student_signup, name = 'register new students'),
]