from django.contrib import admin
from student_app.models import Student, Note, Teacher

# Register your models here.
admin.site.register(Student)
admin.site.register(Note)
admin.site.register(Teacher)