from django import forms
from app.models import *

class Student_Form(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'