from django.contrib import admin
from .models import student


# Register your models here.
class AdminStudent(admin.ModelAdmin):
    list_display=['name','roll_number','department']
admin.site.register(student,AdminStudent)
