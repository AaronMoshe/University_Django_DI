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