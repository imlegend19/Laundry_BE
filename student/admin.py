from django.contrib import admin, auth
import django.contrib.auth.models
from import_export.admin import ImportExportModelAdmin

from student.models import Student

admin.site.unregister(auth.models.Group)


@admin.register(Student)
class ViewAdmin(ImportExportModelAdmin):
    pass
