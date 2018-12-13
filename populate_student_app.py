import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_project.settings')
import django
django.setup()


import random
from faker import Faker
from student_app.models import Student, Note


fakegen = Faker()
matieres = ["Français", "Maths", "Physique", "Magie"];

def populate():
  for i in range(2):
  	newStudent = Student.objects.get_or_create(first_name=fakegen.first_name(), last_name=fakegen.last_name(), birthdate=fakegen.date());
  	note = Note.objects.get_or_create( student=newStudent[0], matiere=random.choice(matieres), note= fakegen.random_int(min=0, max=20), coefficient=fakegen.random_int(min=1, max=10))
  	print(i)


if __name__ == '__main__':
  print('populate script...')
  populate()
  print('done populating.')