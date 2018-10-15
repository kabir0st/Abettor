from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import Student, CustomUser, Subject, Semester

class StudentRegistrationForm(UserCreationForm):
    current_semester = forms.ChoiceField(widget = forms.Select())
    phone_number = forms.IntegerField()
    dob = forms.DateField()

    class Meta(UserCreationForm.Meta):
        model = CustomUser

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.account_type = 4
        user.save()
        student = Student.objects.create(user=user)
        return user
