from crudapp.models import Student
from django import forms
class StudentForm(forms.ModelForm):
    class Meta:
       model = Student
       fields = ['firstname','lastname','Email']



