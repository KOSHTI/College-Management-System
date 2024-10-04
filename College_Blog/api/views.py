from Blog.models import Student, Faculty, Course, Batch, Attendance
from django.shortcuts import get_object_or_404
from django.db.models import F

# Function to handle complex student data processing or filtering
def get_student_details(student_id: int):
    """Return detailed information about a student."""
    student = get_object_or_404(Student, id=student_id)
    
    # Construct a detailed dictionary of student information
    student_data = {
        "first_name": student.first_name,
        "last_name": student.last_name,
        "email": student.email,
        "gender": student.gender,
        "dob": student.date_of_birth,
        "courses": list(student.courses.values_list('course_name', flat=True)),
        "attendance_records": get_student_attendance(student_id)
    }
    
    return student_data

# Function to get a list of attendance records for a specific student
def get_student_attendance(student_id: int):
    """Retrieve attendance records for a student."""
    attendance_records = Attendance.objects.filter(student_id=student_id).values(
        "course__course_name", "status", "date"
    )
    return list(attendance_records)

# Function to create or update attendance (with more custom logic)
def mark_attendance(student_id: int, course_id: int, status: str):
    """Mark attendance for a student in a specific course."""
    student = get_object_or_404(Student, id=student_id)
    course = get_object_or_404(Course, id=course_id)
    
    # Check if attendance record already exists
    attendance, created = Attendance.objects.update_or_create(
        student=student, 
        course=course, 
        defaults={"status": status}
    )
    
    if created:
        return {"message": "Attendance marked", "attendance_id": attendance.id}
    else:
        return {"message": "Attendance updated", "attendance_id": attendance.id}

# Function to get the details of a faculty member
def get_faculty_details(faculty_id: int):
    """Return detailed information about a faculty member."""
    faculty = get_object_or_404(Faculty, id=faculty_id)
    
    faculty_data = {
        "first_name": faculty.first_name,
        "last_name": faculty.last_name,
        "email": faculty.email,
        "department": faculty.department,
        "courses_taught": list(faculty.courses.values_list('course_name', flat=True))
    }
    
    return faculty_data

# Function to retrieve course details and the enrolled students
def get_course_details(course_id: int):
    """Return details of a course and its students."""
    course = get_object_or_404(Course, id=course_id)
    
    course_data = {
        "course_name": course.course_name,
        "description": course.course_description,
        "students_enrolled": list(course.students.values_list(
            F('first_name') + ' ' + F('last_name'), flat=True))
    }
    
    return course_data

# Function to handle batch details
def get_batch_details(batch_id: int):
    """Return details about a specific batch, including associated students and courses."""
    batch = get_object_or_404(Batch, id=batch_id)
    
    batch_data = {
        "batch_name": batch.batch_name,
        "start_date": batch.start_date,
        "end_date": batch.end_date,
        "course": batch.course.course_name,
        "students_enrolled": list(batch.students.values_list(
            F('first_name') + ' ' + F('last_name'), flat=True)),
    }
    
    return batch_data

# Function to create a new batch
def create_batch(course_id: int, batch_name: str, start_date: str, end_date: str):
    """Create a new batch for a specific course."""
    course = get_object_or_404(Course, id=course_id)
    batch = Batch.objects.create(
        course=course,
        batch_name=batch_name,
        start_date=start_date,
        end_date=end_date
    )
    
    return {"message": "Batch created", "batch_id": batch.id}

# Function to add students to a batch
def add_students_to_batch(batch_id: int, student_ids: List[int]):
    """Add students to a batch."""
    batch = get_object_or_404(Batch, id=batch_id)
    students = Student.objects.filter(id__in=student_ids)
    
    batch.students.add(*students)
    
    return {"message": "Students added to batch", "batch_id": batch.id}

