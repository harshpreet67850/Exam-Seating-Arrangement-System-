# Register your models here.
from django.contrib import admin

from .models import Classroom, ExamSeating, Student

admin.site.register(Classroom)
admin.site.register(Student)
admin.site.register(ExamSeating)
