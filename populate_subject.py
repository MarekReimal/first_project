import os
import random
import django
from faker import Faker
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_project.settings") # vajalik et teaks kuhu kirjutada
django.setup()
from first_app.models import Subjects
fakegen = Faker()

# kood mis loob juhulikke isikuid DB'sse, saab käivitada eraldi sõltumata vewebi lehest
# käivita terminalis (venv) C:\Users\marek\Documents\Django_projektid\first_project>py manage.py runserver

def populate(n=1): # vaikimisi teeb viis korda, kui on argument antud siis teeb selle arvu kordi
    subjects = ["Matemaatika", "Kirjandus", "Geograafia", "Ajalugu", "Kunstiõpetus"]
    for entry in subjects:
        Subjects.objects.get_or_create(subject= entry)

populate() # kutsub funkt.