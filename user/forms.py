from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms import ModelForm
from .models import Student, CustomUser, Semester

class UserForm(UserCreationForm,ModelForm):
    username = forms.CharField(min_length=3, max_length=30)
    email = forms.EmailField(required = True)
    first_name = forms.CharField(required =  True)
    last_name = forms.CharField(required =True)

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['first_name','last_name','email','username']


class StudentForm(ModelForm):
    current_semester = forms.ModelChoiceField(queryset = Semester.objects.all(), label = None)
    phone_number = forms.CharField(min_length= 6, max_length=15, required = True)
    profile_image = forms.ImageField()
    class Meta:
        model = Student
        fields = ['current_semester','phone_number','profile_image']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(max_length = 32, widget= forms.PasswordInput)

    class Meta: 
        fields = ['username','password']