from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms import ModelForm
from .models import Student, CustomUser, Subject, Semester

# class StudentRegistrationForm(UserCreationForm):
#     current_semester = forms.ModelChoiceField(queryset = Semester.objects.all(), label = None)
#     phone_number = forms.IntegerField()

#     class Meta(UserCreationForm.Meta):
#         model = CustomUser
#         #fields = ['username','first_name','last_name','email','password1','password2']

#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.account_type = 4
#         user.save()
#         student = Student.objects.create(user=user)
#         return user

class UserForm(UserCreationForm,ModelForm):
    email = forms.EmailField(required = True)

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['first_name','last_name','email','username','password1','password2']

class StudentForm(ModelForm):
    current_semester = forms.ModelChoiceField(queryset = Semester.objects.all(), label = None)
    class Meta:
        model = Student
        fields = ['current_semester','phone_number']