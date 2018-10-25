from django.urls import path, include
from . import views

urlpatterns = [
    path('new',views.registration, name = 'User Registration'),
    path('login',views.user_login, name = 'Login User'),
    path('logout',views.user_logout, name = 'Logout'),
]

