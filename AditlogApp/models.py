from django.db import models
# from operator import mod
# from statistics import mode
from auditlog.registry import auditlog
from auditlog.models import AuditlogHistoryField

# Create your models here.
class student (models.Model):
    name=models.CharField(max_length=100)
    roll_number=models.IntegerField()
    department=models.CharField(max_length=100)
auditlog.register(student)