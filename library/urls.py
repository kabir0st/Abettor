from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('search', views.search, name = 'search book by name'),
    path('book/register',views.register_book, name = "register new book"),
    path('<str:uuid>',views.book_info, name = "show book info"),
    path('book/assign',views.assign_book, name = "Assign Books"),
]
