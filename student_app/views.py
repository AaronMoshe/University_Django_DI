from django.shortcuts import render
from student_app.models import Student, Note, Teacher
from student_app.forms import TeacherForm

# Create your views here.
def index(request):
    students = Student.objects.all().order_by('id')
    return render(request, 'students/index.html', context={'students': students})

def details(request, student_id):
    student = Student.objects.get(id=student_id)
    notes = Note.objects.filter(student=student)
    return render(request, 'students/details.html', context={'student': student, 'notes': notes})

def allTeachers(request):
	teachers = Teacher.objects.all().order_by('nom')
	return render(request, 'teachers/index.html', context={'teachers': teachers})

def detailsTeacher(request, teacher_id):
	teacher = Teacher.objects.get(id=teacher_id)
	return render(request, 'teachers/teacherDetails.html', context={'teacher': teacher})

def createNewTeacher(request):
	if request.method == 'POST':
		newTeacher = Teacher.objects.get_or_create(nom=request.POST.get('nom'), prenom=request.POST.get('prenom'), email=request.POST.get('email'), matiere=request.POST.get('matiere'), date_naissance=request.POST.get('date_naissance'))

	return render(request, 'teachers/createTeacher.html', context={'teacher_form': TeacherForm()})