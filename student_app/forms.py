from django import forms
from student_app.models import Teacher

class TeacherForm(forms.ModelForm):
	class Meta:
		model = Teacher
		fields = ['nom', 'prenom','email', 'matiere', 'date_naissance']
		widgets = {
			'nom': forms.TextInput(attrs={
				'id': 'teacher-nom',
				'placeholder': 'Write your last name',
				'required': True
				}),
			'prenom': forms.TextInput(attrs={
				'id': 'teacher-prenom',
				'placeholder': 'Write your first name',
				'required': True
				}),
			'email': forms.TextInput(attrs={
				'id': 'teacher-username',
				'placeholder': 'Write your email',
				'required': True
				}),
			'matiere': forms.TextInput(attrs={
				'id': 'teacher-text',
				'placeholder': 'Write your matiere',
				'required': True
				}),
			'date_naissance': forms.TextInput(attrs={
				'id': 'teacher-date_naissance',
				'placeholder': 'date de naissance',
				'required': True
				}),

		}