from django.urls import path, include
from . import views

urlpatterns = [
    path('new',views.registration, name = 'User Registration'),
    path('login',views.user_login, name = 'Login User'),
    path('logout',views.user_logout, name = 'Logout'),
    # path('<str:username>',views.show_user_profile, name = "Show / edit User Profile")
]

