from django.db import models
from django.contrib import admin

# Create your models here.

class Student(models.Model): # klass mis loob tabeli
    # tabeli tegemsiel vaja teha make migration ja migrate
    name = models.CharField(max_length=100)  # väli välja tüüp ja pikkus
    birth_of_date = models.DateField(null=True, blank=True) # võib olla tühi
    weight = models.IntegerField() # väli kaal, integer tüüpi

class Teacher(models.Model): # loob õpetajate tabeli veergudega
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)

    def __str__(self): # on kaks varianti kuidas kuvada
        return f"{self.name} teaches {self.subject}"

class StudentAdmin(admin.ModelAdmin):

    list_filter = ["weight"] # lisab filtri väljale

    # funktsioon siia klassi, et muuta kuupäev vormingut
    def birthday(self, obj):
        if obj.birth_of_date is not None: # kontroll kas on kuupäev olemas
            return obj.birth_of_date.strftime("%d.%m.%Y") # kui on siis vormindab

    list_display = ["birthday", "name", "weight"]  # admin tabelis on näha listi sisu
    list_per_page = 10 # mitu rida DB'st ühel lehel näitab

"""
class TeacherAdmin(admin.ModelAdmin): # on kaks varianti kuidas kuvada
    list_display = ["name", "subject"]
"""