from ninja import Router
from Blog.models import Student, Faculty, Course, Batch, Attendance
from typing import List
from django.shortcuts import get_object_or_404

router = Router()

# ----------------------- Student APIs -----------------------
@router.get("/students", response=List[dict])
def list_students(request):
    """Retrieve a list of all students"""
    students = Student.objects.all().values()
    return list(students)

@router.get("/student/{student_id}")
def get_student(request, student_id: int):
    """Retrieve a student by their ID"""
    student = get_object_or_404(Student, id=student_id)
    return {
        "first_name": student.first_name,
        "last_name": student.last_name,
        "email": student.email,
        "gender": student.gender,
        "dob": student.date_of_birth
    }

@router.post("/student")
def create_student(request, first_name: str, last_name: str, email: str, gender: str, dob: str):
    """Create a new student"""
    student = Student.objects.create(
        first_name=first_name,
        last_name=last_name,
        email=email,
        gender=gender,
        date_of_birth=dob
    )
    return {"message": "Student created", "student_id": student.id}

@router.put("/student/{student_id}")
def update_student(request, student_id: int, first_name: str, last_name: str, email: str, gender: str, dob: str):
    """Update an existing student"""
    student = get_object_or_404(Student, id=student_id)
    student.first_name = first_name
    student.last_name = last_name
    student.email = email
    student.gender = gender
    student.date_of_birth = dob
    student.save()
    return {"message": "Student updated"}

@router.delete("/student/{student_id}")
def delete_student(request, student_id: int):
    """Delete a student by ID"""
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return {"message": "Student deleted"}

# ----------------------- Faculty APIs -----------------------
@router.get("/faculties", response=List[dict])
def list_faculties(request):
    faculties = Faculty.objects.all().values()
    return list(faculties)

@router.get("/faculty/{faculty_id}")
def get_faculty(request, faculty_id: int):
    faculty = get_object_or_404(Faculty, id=faculty_id)
    return {
        "first_name": faculty.first_name,
        "last_name": faculty.last_name,
        "email": faculty.email,
        "department": faculty.department
    }

@router.post("/faculty")
def create_faculty(request, first_name: str, last_name: str, email: str, department: str):
    faculty = Faculty.objects.create(
        first_name=first_name,
        last_name=last_name,
        email=email,
        department=department
    )
    return {"message": "Faculty created", "faculty_id": faculty.id}

# ----------------------- Course APIs -----------------------
@router.get("/courses", response=List[dict])
def list_courses(request):
    courses = Course.objects.all().values()
    return list(courses)

@router.get("/course/{course_id}")
def get_course(request, course_id: int):
    course = get_object_or_404(Course, id=course_id)
    return {
        "course_name": course.course_name,
        "course_description": course.course_description
    }

@router.post("/course")
def create_course(request, course_name: str, course_description: str):
    course = Course.objects.create(
        course_name=course_name,
        course_description=course_description
    )
    return {"message": "Course created", "course_id": course.id}

# ----------------------- Batch APIs -----------------------
@router.get("/batches", response=List[dict])
def list_batches(request):
    batches = Batch.objects.all().values()
    return list(batches)

@router.get("/batch/{batch_id}")
def get_batch(request, batch_id: int):
    batch = get_object_or_404(Batch, id=batch_id)
    return {
        "batch_name": batch.batch_name,
        "course": batch.course.course_name
    }

@router.post("/batch")
def create_batch(request, batch_name: str, course_id: int):
    course = get_object_or_404(Course, id=course_id)
    batch = Batch.objects.create(batch_name=batch_name, course=course)
    return {"message": "Batch created", "batch_id": batch.id}

# ----------------------- Attendance APIs -----------------------
@router.get("/attendances", response=List[dict])
def list_attendance(request):
    attendances = Attendance.objects.all().values()
    return list(attendances)

@router.get("/attendance/{attendance_id}")
def get_attendance(request, attendance_id: int):
    attendance = get_object_or_404(Attendance, id=attendance_id)
    return {
        "student": attendance.student.first_name + " " + attendance.student.last_name,
        "course": attendance.course.course_name,
        "status": attendance.status
    }

@router.post("/attendance")
def create_attendance(request, student_id: int, course_id: int, status: str):
    student = get_object_or_404(Student, id=student_id)
    course = get_object_or_404(Course, id=course_id)
    attendance = Attendance.objects.create(student=student, course=course, status=status)
    return {"message": "Attendance created", "attendance_id": attendance.id}

# # Faculty APIs
# @router.get("/faculties", response=List[dict])
# def list_faculties(request):
#     faculties = Faculty.objects.all().values()
#     return list(faculties)

# @router.get("/faculty/{faculty_id}")
# def get_faculty(request, faculty_id: int):
#     faculty = get_object_or_404(Faculty, id=faculty_id)
#     return {"first_name": faculty.first_name, "last_name": faculty.last_name}

# @router.post("/faculty")
# def create_faculty(request, first_name: str, last_name: str, email: str, department: str):
#     faculty = Faculty.objects.create(first_name=first_name, last_name=last_name, email=email, department=department)
#     return {"message": "Faculty created", "faculty_id": faculty.id}
