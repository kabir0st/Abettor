from django import forms
from django.forms import ModelForm
from user.models import Student, Semester
from .models import Books


class BookForm(ModelForm):
    semester = forms.ModelChoiceField(queryset = Semester.objects.all(), label = None)
    
    class Meta:
        model = Books
        fields = ['name','author','nou_registered','semester']