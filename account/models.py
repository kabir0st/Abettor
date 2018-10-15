from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ACCOUNT_TYPE_CHOICE = (
        (0,'superuser'),
        (1,'teacher'),
        (2,'accountant'),
        (3,'librarian'),
        (4,'student')
    )
    account_type = models.PositiveSmallIntegerField(choices = ACCOUNT_TYPE_CHOICE,blank= True, null = True)



class Subject(models.Model):
    subject_name = models.CharField(unique = True, max_length = 100)
    #books = models.ManyToManyField(Book)

    def __str__(self):
        return self.subject_name

class Semester(models.Model):
    fee = models.IntegerField(default= 52000)
    semester = models.PositiveIntegerField(default = 1)
    subjects = models.ManyToManyField(Subject)

class Student(models.Model):
    REQUIRED_FIELDS = ('user',)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key = True, related_name = 'student',unique = True)
    current_semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    phone_number = models.IntegerField(blank= True)
    dob = models.DateField(blank = True)