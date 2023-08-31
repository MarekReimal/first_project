from django.shortcuts import render
from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView, UpdateView, DeleteView) #mis on TemplateView vt Django dok
from django.urls import reverse_lazy
from . models import Student

# Create your views here.

# MIDA KASUTAJA NÄEB APPI LEHEL

#avaleht kuidas näeb välja
class MyHomeView(TemplateView):
    template_name = "first_app/home.html"

class StudentListView(ListView): # vaade  pannakse app urli
    # KAUSUTAB NIMEKIRJA KUVAMISEKS, ON VAATED MIDA NÄEME
    #model_list.html -> student_list.html
    model = Student # ühendab Model Student, siit tuleb info
    queryset = Student.objects.order_by("name") # sorteerib nime järgi
    context_object_name = "students" # muudab nime et oleks loetavam, default object_list nimeks students
    paginate_by = 25 # mitu rida lehel kuvab

class StudentDetailView(DetailView):
    #tagastab ainult ühe tulemuse, klik ühe isiku peal annab ühe isiku andmed
    # default template model_detail.html => student_detail.html
    model = Student

class StudentCreateView(CreateView):
    # UUE VÄLJA LISAMISEKS
    template_name = "first_app/student_from_create.html"
    model = Student
    fields = "__all__" # kõik väljad näha loomise vaatel
    success_url = reverse_lazy("first_app:student_list")

class StudentUpdateView(UpdateView):
    # model_form.html => student_form.html
    model = Student
    fields = ["name", "weight"] # uuenda ainult neid veerge
    success_url = reverse_lazy("first_app:student_list") # MIS JUHTUB PEALE õnnestunud sündmust

class StudentDeleteView(DeleteView):
    # Form -> confirm Delete Button
    # default tmplate name => model_confirm_delete.html -> student_confirm_delete.html
    model = Student
    # suuna peale edukat kustutamist
    success_url = reverse_lazy("first_app:student_list")