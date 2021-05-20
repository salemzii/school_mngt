from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('students/', views.students, name='students'),
    path('staffs/', views.staffs, name='staffs'),
    path('courses/', views.courses, name='courses'),
    path('data/', views.course_view, name='data'),
    path('<int:course_id>/', views.course_data_view, name='course-data'),
    path('students/<int:student_id>/', views.student_data_view, name='student-data'),
    path('staffs/<int:staff_id>/', views.staff_data_view, name='staff-data'),
    path('new-student/', views.Student_create_view.as_view(), name='create-student'),
    path('students/delete/<int:student_id>/', views.Student_delete_view.as_view(), name='delete-student'),
    path('students/update/<int:student_id>/', views.Student_update_view.as_view(), name='update-student'),
    path('new-staff/', views.Staff_create_view.as_view(), name='create-staff'),
    path('staffs/delete/<int:staff_id>/', views.Staff_delete_view.as_view(), name='delete-staff'),
    path('staffs/update/<int:staff_id>/', views.Staff_update_view.as_view(), name='update-staff'),
]
