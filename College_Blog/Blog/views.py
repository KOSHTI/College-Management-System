from django.shortcuts import render, get_object_or_404, redirect
from Blog.models import Student, Faculty, Course, Batch, Attendance
from .forms import FacultyForm, CourseForm

# from django.http import HttpResponse

def home(request):
    """Render the homepage."""
    return render(request, 'home.html')  


# ----------------------- For Students -----------------------
def list_students(request):
    """Retrieve a list of all students and render to a template."""
    students = Student.objects.all()
    return render(request, 'students_list.html', {'students': students})

def get_student(request, student_id):
    """Retrieve a student by their ID."""
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'student_detail.html', {'student': student})

def create_student(request):
    """Create a new student."""
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        gender = request.POST['gender']
        dob = request.POST['dob']

        # Create the student object
        student = Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            gender=gender,
            date_of_birth=dob
        )

        return redirect('list_students')  # Redirect to the student list after creation

    # On GET request, no need to pass 'student' since it hasn't been created yet
    return render(request, 'create_student.html')  # Render the form for student creation


def update_student(request, student_id):
    """Update an existing student."""
    student = get_object_or_404(Student, id=student_id)
    
    if request.method == 'POST':
        student.first_name = request.POST['first_name']
        student.last_name = request.POST['last_name']
        student.email = request.POST['email']
        student.gender = request.POST['gender']
        student.date_of_birth = request.POST['dob']
        student.save()
        return redirect('list_students')  # Redirect to the student list after updating

    return render(request, 'update_student.html', {'student': student})  # Render the update form

def delete_student(request, student_id):
    """Delete a student by ID."""
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        student.delete()
        return redirect('list_students')  # Redirect to the student list after deletion

    return render(request, 'delete_student.html', {'student': student})  # Render delete confirmation


# ----------------------- For Faculty -----------------------
def list_faculties(request):
    """Retrieve a list of all faculties and render to a template."""
    faculties = Faculty.objects.all()
    return render(request, 'faculties_list.html', {'faculties': faculties})

def faculty_detail(request, faculty_id):
    """Retrieve a faculty by their ID."""
    faculty = get_object_or_404(Faculty, id=faculty_id)
    return render(request, 'faculty_detail.html', {'faculty': faculty})

def create_faculty(request):
    if request.method == 'POST':
        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form, which creates a Faculty object
            return redirect('list_faculties')  # Redirect to the faculty list after creation
    else:
        form = FacultyForm()  # Create an empty form instance for a GET request

    return render(request, 'create_faculty.html', {'form': form})  # Pass the form to the template


# ----------------------- For Course -----------------------
def list_courses(request):
    """Retrieve a list of all courses and render to a template."""
    courses = Course.objects.all()
    return render(request, 'courses_list.html', {'courses': courses})

def get_course(request, course_id):
    """Retrieve a course by its ID."""
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'course_detail.html', {'course': course})

def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()  # Save the course form and create a course object
            return redirect('list_courses')  # Redirect to the course list after creation
    else:
        form = CourseForm()  # Create an empty form instance for a GET request

    return render(request, 'create_course.html', {'form': form})   # Render the course creation form


# ----------------------- For Batches -----------------------
def list_batches(request):
    """Retrieve a list of all batches and render to a template."""
    batches = Batch.objects.all()
    return render(request, 'batches_list.html', {'batches': batches})

def get_batch(request, batch_id):
    """Retrieve a batch by its ID."""
    batch = get_object_or_404(Batch, id=batch_id)
    return render(request, 'batch_detail.html', {'batch': batch})

def create_batch(request):
    """Create a new batch."""
    if request.method == 'POST':
        batch_name = request.POST['batch_name']
        start_date = request.POST.get('start_date')  # Use get to avoid MultiValueDictKeyError
        course_id = request.POST['course_id']
        course = get_object_or_404(Course, id=course_id)

        if not start_date:
            return render(request, 'create_batch.html', {'error': 'Start date is required', 'courses': Course.objects.all()})

        # Create batch
        batch = Batch.objects.create(batch_name=batch_name, start_date=start_date, course=course)
        return redirect('list_batches')  # Redirect to the batches list after creation

    courses = Course.objects.all()  # Get all courses to display in the form
    return render(request, 'create_batch.html', {'courses': courses})  # Render the batch creation form


# ----------------------- For Attendance -----------------------
def list_attendance(request):
    """Retrieve a list of all attendance records and render to a template."""
    attendances = Attendance.objects.all()
    return render(request, 'attendance_list.html', {'attendances': attendances})

def get_attendance(request, attendance_id):
    """Retrieve an attendance record by its ID."""
    attendance = get_object_or_404(Attendance, id=attendance_id)
    return render(request, 'attendance_detail.html', {'attendance': attendance})

def create_attendance(request):
    """Create a new attendance record."""
    if request.method == 'POST':
        student_id = request.POST.get('student_id')  # Use get to avoid KeyError
        course_id = request.POST.get('course_id')    # Use get to avoid KeyError
        status = request.POST.get('status')            # Use get to avoid KeyError

        # Ensure that student and course exist
        student = get_object_or_404(Student, id=student_id) if student_id else None
        course = get_object_or_404(Course, id=course_id) if course_id else None

        if student and course:  # Ensure both objects are valid before creating attendance
            attendance = Attendance.objects.create(student=student, course=course, status=status)
            return redirect('list_attendance', {'attendance': attendance})  # Redirect to the attendance list after creation

    # Render the form with the necessary data for GET request
    students = Student.objects.all()  # Get all students to display in the form
    courses = Course.objects.all()  # Get all courses to display in the form
    return render(request, 'create_attendance.html', {'students': students, 'courses': courses})