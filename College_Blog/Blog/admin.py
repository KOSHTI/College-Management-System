from django.contrib import admin
from Blog.models import *

# Register your models here.
models = [
    Student, 
    Faculty, 
    Course, 
    Batch, 
    Attendance,
]

for model in models:
    admin.site.register(model)
