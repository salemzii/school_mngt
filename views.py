from django.shortcuts import render
from .models import Students, Staff, Courses
from django.views.generic import UpdateView, DeleteView, CreateView


def home_view(request):
    return render(request, 'manager_app/home.html', {'title': 'Home Page...'})


def students(request):
    s = Students.objects.all()
    context = {
        'students': s.order_by,
    }
    return render(request, 'manager_app/students.html', context)


def staffs(request):
    st = Staff.objects.all()
    context = {
        'staffs': st
    }
    return render(request, 'manager_app/staffs.html', context)


def courses(request):
    c = Courses.objects.all()
    st = Students.objects.all()

    context = {
        'courses': c,
        'students': st,
    }

    return render(request, 'manager_app/courses.html', context)


def course_view(request):
    course = Courses.objects.all()
    st = Students.objects.all()

    context = {
        'courses': course,
        'students': st,
    }
    return render(request, 'manager_app/stu-course.html', context)


def course_data_view(request, course_id):
    q = Courses.objects.get(id=course_id)
    context = {
        'course': q,
    }
    return render(request, 'manager_app/course_view.html', context)


def student_data_view(request, student_id):
    q = Students.objects.get(id=student_id)
    context = {
        'student': q,
    }
    return render(request, 'manager_app/student_view.html', context)


def staff_data_view(request, staff_id):
    q = Staff.objects.get(id=staff_id)
    context = {
        'staff': q,
    }
    return render(request, 'manager_app/staff_view.html', context)


class Student_create_view(CreateView):
    model = Students
    fields = ["name", 'course', 'email', 'phone_number', 'matric_number', 'date_admitted']
    template_name = 'manager_app/add_student.html'
    success_url = '/students'


class Student_delete_view(DeleteView):
    model = Students
    template_name = 'manager_app/delete_student.html'
    success_url = '/students'
    pk_url_kwarg = 'student_id'


class Student_update_view(UpdateView):
    model = Students
    fields = ["name", 'course', 'email', 'phone_number', 'matric_number', 'date_admitted']
    template_name = 'manager_app/add_student.html'
    pk_url_kwarg = 'student_id'
    success_url = '/students'


class Staff_create_view(CreateView):
    model = Staff
    fields = ["name", 'lecture_course', 'job_type', 'email', 'phone_number', 'date_employed']
    template_name = 'manager_app/add_staff.html'
    success_url = '/staffs'


class Staff_delete_view(DeleteView):
    model = Staff
    template_name = 'manager_app/delete_staff.html'
    success_url = '/staffs'
    pk_url_kwarg = 'staff_id'


class Staff_update_view(UpdateView):
    model = Staff
    fields = ["name", 'lecture_course', 'job_type', 'email', 'phone_number', 'date_employed']
    template_name = 'manager_app/add_staff.html'
    pk_url_kwarg = 'staff_id'
    success_url = '/staffs'
