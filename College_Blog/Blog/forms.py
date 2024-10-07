# forms.py
from django import forms
from .models import Faculty, Course

class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['first_name', 'last_name', 'email', 'department']  # List the fields you want to include in the form

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'description']  