from django.urls import path
from . import views 

app_name = 'student_app'

urlpatterns = [
	path('', views.index, name='index'),
	path('student/<int:student_id>/', views.details, name='student'),
]