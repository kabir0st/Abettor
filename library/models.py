from django.db import models
from user.models import Student,Semester

class Books(models.Model):    
    name = models.CharField(max_length = 200)
    semester = models.ForeignKey(Semester,on_delete=models.CASCADE)
    author = models.CharField (max_lenght = 200)
    nou_avaible = models.PositiveIntegerField(default = 1)
    nau_borrowed = models.PositiveIntegerField(default = 0)
    nou_registered = models.PositiveIntegerField(default = 1)

class Book(models.Model):
    book = models.ForeignKey(Books,on_delete = models.CASCADE)
    