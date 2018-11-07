from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime

class CustomUser(AbstractUser):
    is_student = models.BooleanField(default=True)
    is_teacher = models.BooleanField(default=False)
    is_librarian = models.BooleanField(default =False)
    is_accountant = models.BooleanField(default= False)

    def __str__(self):
        return self.first_name + self.last_name


class Subject(models.Model):
    subject_name = models.CharField(unique = True, max_length = 100)
    #books = models.ManyToManyField(Book)

    def __str__(self):
        return self.subject_name

class Semester(models.Model):
    fee = models.IntegerField(default= 52000)
    semester = models.PositiveIntegerField(default = 1)
    subjects = models.ManyToManyField(Subject,blank = True)

    def __str__(self):
        return str(self.semester) 


class FeeTable(models.Model):
    REQUIRED_FIELDS = ('student',)
    student = models.OneToOneField('Student',on_delete = models.CASCADE , primary_key = True)
    credit = models.PositiveIntegerField(default = 0)
    dues = models.PositiveIntegerField(default = 0)
    paid_sem = models.PositiveIntegerField(default = 0)

class Student(models.Model):
    REQUIRED_FIELDS = ('user',)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key = True, related_name = 'student',unique = True)
    # Normal Profile Data
    phone_number = models.CharField(max_length = 15)
    dob = models.DateField(default = datetime.date.today)
    registered_on = models.DateTimeField (default = datetime.datetime.now)
    # Reference Data
    current_semester = models.ForeignKey(Semester, on_delete=models.CASCADE)


class Teacher (models.Model):
    REQUIRED_FIELDS = ('user',)
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE, primary_key = True, related_name = 'teacher', unique = True)
    contact_number = models.CharField(blank = True, max_length = 14)

    # def __str__(self):
    #     return self.user.first_name