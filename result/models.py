from django.db import models
from user.models import Semester,Teacher,Student,Subject
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class Result(models.Model):
    date = models.DateField(default = timezone.now)
    semester = models.ForeignKey(Semester,on_delete= models.CASCADE)
    more_info = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return str(self.more_info) + " " + str(self.semester)
    
class ReportCard(models.Model):
    student = models.ForeignKey(Student,on_delete= models.CASCADE)
    result = models.ForeignKey(Result,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.student.user.username + " " +str(self.result))

class Marks(models.Model):
    reportcard = models.ForeignKey(ReportCard,on_delete = models.CASCADE)
    mark = models.PositiveIntegerField(default = 0)
    subject = models.ForeignKey(Subject,on_delete = models.CASCADE)

    def __str__(self):
        return str(self.subject) + " " + str(self.reportcard)