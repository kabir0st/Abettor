from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('search',views.search, name="search"),
    path('<str:username>',views.get_info, name = "Pay Biils"),
    path('<str:username>/pay',views.pay, name = "payment"),
    path('khalti/verify',views.verify_khalti,name = "verify khalti"),
]
