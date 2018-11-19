from django.db import models
from datetime  import date
from django_mysql.models import ListCharField
from user.models import Semester,Teacher,Student
from django.utils import timezone

class Result(models.Model):
    date = models.DateField(default = timezone.now)
    semester = models.ForeignKey(Semester,on_delete= models.CASCADE)
    
class ReportCard(models.Model):
    student = models.ForeignKey(Student,on_delete= models.CASCADE)
    marks = ListCharField(
        base_field = models.PositiveIntegerField(default= 0),
        size = 7,
        max_length = (7*4),
        blank =True
    )
    result = models.ForeignKey(Result,on_delete=models.CASCADE)