from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('search', views.index, name = 'search book by name'),
    path('book/register',views.register_book, name = "register new book"),
]
