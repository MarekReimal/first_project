from django.contrib import admin
from .models import Student, StudentAdmin # teeb admin lehel Student tabeli nähtavaks
#from .models import Teacher, TeacherAdmin # on kaks varianti kuidas kuvada
from .models import Teacher
from .models import Subject
# Student on minu tehtud klass


# Register your models here.
admin.site.register(Student, StudentAdmin) # teeb Student tabeli nähtavaks
#admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Teacher)
admin.site.register(Subject)