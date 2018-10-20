from django.urls import path
from . import views

urlpatterns = [
    path('login', views.user_login, name = 'login'),
    path('new',views.student_signup, name = 'register new students'),
    path('logout',views.user_logout, name = 'Logout'),
]