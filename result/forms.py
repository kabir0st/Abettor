from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms import ModelForm
from .models import ReportCard, Result
from user.models import Semester,Student

class ResultForm(ModelForm):
    semester = forms.ModelChoiceField(queryset = Semester.objects.all(), label = None)
    
    class Meta(UserCreationForm):
        model = Result
        fields = ['date','semester']
