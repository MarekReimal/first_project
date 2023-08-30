import os
import random
import django
from faker import Faker
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_project.settings") # vajalik et teaks kuhu kirjutada
django.setup()
from first_app.models import Student
from first_app.models import Teacher
fakegen = Faker()

# kood mis loob juhulikke isikuid DB'sse, saab käivitada eraldi sõltumata vewebi lehest
# käivita terminalis (venv) C:\Users\marek\Documents\Django_projektid\first_project>py manage.py runserver

def populate(n=5): # vaikimisi teeb viis korda, kui on argument antud siis teeb selle arvu kordi
    for entry in range(n):
        sujects = ["Matemaatika", "Kirjandus", "Geograafia", "Ajalugu", "Kunstiõpetus"]
        fake_name = fakegen.name()  # loob nime
        # t = random.choices(teachers) # annab tulemuseks [] listi ühe väärtusega
        fake_subject = random.choices(sujects)[0] # võtab listist esimese, seal ongi ainult üks kirje
        Teacher.objects.get_or_create(name=fake_name, subject=fake_subject)

populate(9) # kutsub funkt.
