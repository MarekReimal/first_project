from django.urls import path
from . import views


# kõik first apiga seotud lingid et teaks kuhu minna, millist faili avada
# koostab url lingi
app_name = "first_app"
urlpatterns = [
    path("", views.MyHomeView.as_view(), name="home"), # home vaade
    # views.StudentListView.as_view() - milline vaade avatakse
    # student_list/ osa mis on aadressi väljal näha
    path("student_list/", views.StudentListView.as_view(), name="student_list"), # kui õpilasi näha tahad siis vaja ulrli kirjutada first_app/student_list
    path("student_detail/<int:pk>", views.StudentDetailView.as_view(), name="student_detail"),
    path("student_create/", views.StudentCreateView.as_view(), name="student_create"),
    path("student_update/<int:pk>", views.StudentUpdateView.as_view(), name="student_update"),
    path("student_delete/<int:pk>", views.StudentDeleteView.as_view(), name="student_delete"), # siin student_delete on viide mille järgi leitakse
    path("teacher_list/", views.TeacherListView.as_view(), name="teacher_list"),
    path("teacher_create/", views.TeacherCreateView.as_view(), name="teacher_create"),
    path("subject_list/", views.SubjectListView.as_view(), name="subject_list"),
    path("subject_create/", views.SubjectCreateView.as_view(), name="subject_create"),
    path("subject_update/<int:pk>", views.SubjectUpdateViev.as_view(), name="subject_update"),
    path("subject_delete/<int:pk>", views.SubjectDeleteView.as_view(), name="subject_delete")
]