from django.contrib import admin
from .models import Student,Semester,CustomUser, FeeTable,Subject
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Student)
admin.site.register(Semester)
admin.site.register(FeeTable)
admin.site.register(Subject)

