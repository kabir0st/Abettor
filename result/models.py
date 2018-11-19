from django.db import models
from user.models import Semester,Teacher,Student,Subject
from django.utils import timezone

class Result(models.Model):
    date = models.DateField(default = timezone.now)
    semester = models.ForeignKey(Semester,on_delete= models.CASCADE)
    
class ReportCard(models.Model):
    student = models.ForeignKey(Student,on_delete= models.CASCADE)
    result = models.ForeignKey(Result,on_delete=models.CASCADE)

class Marks(models.Model):
    reportcard = models.ForeignKey(ReportCard,on_delete = models.CASCADE)
    mark = models.PositiveIntegerField()
    subject = models.ForeignKey(Subject,on_delete = models.CASCADE)
