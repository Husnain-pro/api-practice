from django.contrib import admin

from .models import Album, TeacherModel,Track

admin.register(TeacherModel,Album,Track)(admin.ModelAdmin)
