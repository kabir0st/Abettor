from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'collection of results'),
    path('<int:semester>/',views.get_sem_year, name = 'get year list of a semester'),
    path('<int:semester>/<int:year>',views.get_sem_year, name = 'get year list of a semester'),
]
