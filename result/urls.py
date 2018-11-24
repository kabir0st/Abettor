from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'collection of results'),
    path('<int:semester>/',views.list_draft, name = 'get year list of a semester'),
    path('<int:semester>/<int:pk>',views.show_draft, name = 'show result'),
    path('<int:semester>/<int:pk>/assign',views.assign_mark, name = 'assign mark'),
    path('new-draft',views.publish_result_draft,name = 'Publish result'),

]
