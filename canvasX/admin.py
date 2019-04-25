from django.contrib import admin
from .models import Student, Professor, Course, Section, Enrolls
# Register your models here.
admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Enrolls)