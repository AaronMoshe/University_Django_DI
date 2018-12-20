from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birthdate = models.DateField()

    def __str__(self):
        return self.first_name

class Note(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	matiere = models.CharField(max_length=20)
	note = models.IntegerField(default=0)
	coefficient = models.IntegerField(default=0)

	def __str__(self):
		return self.matiere

class Teacher(models.Model):
	nom = models.CharField(max_length=20)
	prenom = models.CharField(max_length=20)
	email = models.EmailField(max_length=40, unique=True)
	matiere = models.CharField(max_length=20)
	date_naissance = models.DateField()

	def __str__(self):
        return self.prenom

class Diplome(models.Model):
	nom = models.CharField(max_length=30)

	def __str__(self):
        return self.prenom


class Teacher(models.Model):
	nom = models.CharField(max_length=20)
	prenom = models.CharField(max_length=20)
	email = models.EmailField(max_length=40, unique=True)
	diplome = models.ForeignKey(Diplome, on_delete=models.CASCADE)
	noteBac = models.IntegerField(default=0)

	def __str__(self):
        return self.prenom




