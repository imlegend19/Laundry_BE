from django.contrib import admin, auth
import django.contrib.auth.models

from student.models import Student

admin.site.unregister(auth.models.Group)
admin.site.register(Student)
