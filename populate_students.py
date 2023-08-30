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
        """
        fake_name = fakegen.name() # loob nime
        fake_birth = fakegen.date_between() # loob kuupäeva
        fake_weight = random.randrange(50, 150) # loob kaalu
        # print(f"{fake_name}, {fake_birth}, {fake_weight}") # test
        # kirjuta andmed DB'se
        Student.objects.get_or_create(name=fake_name, birth_of_date=fake_birth, weight=fake_weight)
        """

        fake_name = fakegen.name()  # loob nime
        Teacher.objects.get_or_create(name=fake_name)

populate(9) # kutsub funkt.
