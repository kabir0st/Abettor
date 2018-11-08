from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('search',views.search, name="search"),
    path('<str:username>',views.get_info, name = "Pay Biils"),
]
