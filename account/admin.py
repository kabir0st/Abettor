from django.contrib import admin
from .models import Student,Subject,Semester,CustomUser
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Semester)

