from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone



class CustomUser(AbstractUser):
    is_student = models.BooleanField(default=True)
    is_teacher = models.BooleanField(default=False)
    is_librarian = models.BooleanField(default =False)
    is_accountant = models.BooleanField(default= False)

    def __str__(self):
        return self.first_name + self.last_name

class Semester(models.Model):
    fee = models.IntegerField(default= 52000)
    semester = models.PositiveIntegerField(default = 1)

    def __str__(self):
        return str(self.semester) 


class FeeTable(models.Model):
    REQUIRED_FIELDS = ('student',) 
    student = models.OneToOneField('Student',on_delete = models.CASCADE , primary_key = True)
    paid_till_now = models.PositiveIntegerField(default = 0)
    
class Student(models.Model):
    REQUIRED_FIELDS = ('user',)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key = True, related_name = 'student',unique = True)
    # Normal Profile Data
    phone_number = models.CharField(max_length = 15)
    # Reference Data
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name + " " +self.user.last_name

class Teacher (models.Model):
    REQUIRED_FIELDS = ('user',)
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE, primary_key = True, related_name = 'teacher', unique = True)
    contact_number = models.CharField(blank = True, max_length = 14)

    # def __str__(self):
    #     return self.user.first_name

class Subject(models.Model):
    name = models.CharField(max_length = 200)
    semester = models.ForeignKey(Semester, on_delete = models.CASCADE)
    teacher = models.ForeignKey(Teacher,on_delete = models.CASCADE)

    def __str__(self):
        return self.name

