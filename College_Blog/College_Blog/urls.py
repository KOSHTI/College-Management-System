"""
URL configuration for College_Blog project.

The `urlpatterns` list routes URLs to views. For more information, please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views:
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views:
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf:
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from ninja import NinjaAPI
from api.routers import router as college_router
from django.urls import path
from Blog.views import (
    home, list_students, get_student, create_student, update_student, delete_student,
    list_faculties, faculty_detail, create_faculty,
    list_courses, get_course, create_course,
    list_batches, get_batch, create_batch,
    list_attendance, get_attendance, create_attendance
)

# NinjaAPI instance to include college-related API routes
api = NinjaAPI()
api.add_router("/college/", college_router)

# URL patterns
urlpatterns = [
    path("admin/", admin.site.urls),                  # Admin interface
    path("api/", api.urls),                           # API endpoints

    # Homepage
    path('', home, name='home'),

    # Student-related URLs
    path('students/', list_students, name='list_students'),
    path('students/create/', create_student, name='create_student'),
    path('students/<int:student_id>/', get_student, name='get_student'),
    path('students/<int:student_id>/update/', update_student, name='update_student'),
    path('students/<int:student_id>/delete/', delete_student, name='delete_student'),

    # Faculty-related URLs
    path('faculties/', list_faculties, name='list_faculties'),
    path('faculties/<int:faculty_id>/', faculty_detail, name='faculty_detail'),
    path('faculties/create/', create_faculty, name='create_faculty'),

    # Course-related URLs
    path('courses/', list_courses, name='list_courses'),
    path('course/<int:course_id>/', get_course, name='get_course'),
    path('course/create/', create_course, name='create_course'),

    # Batch-related URLs
    path('batches/', list_batches, name='list_batches'),
    path('batch/<int:batch_id>/', get_batch, name='get_batch'),
    path('batch/create/', create_batch, name='create_batch'),

    # Attendance-related URLs
    path('attendances/', list_attendance, name='list_attendance'),
    path('attendance/<int:attendance_id>/', get_attendance, name='get_attendance'),
    path('attendance/create/', create_attendance, name='create_attendance'),
]
