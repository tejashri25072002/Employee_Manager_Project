from django.db import models
from department.models import Department

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(unique=True)
    address=models.CharField(max_length=300)
    DESIGNATION__CHOICES=(
        ('Associate','Associate'),('TL','Team Leader'),('Manager','Manager'),
    )
    designation=models.CharField(max_length=50,choices=DESIGNATION__CHOICES,default="Manager")
    reporting_manager=models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)
    department=models.ForeignKey('department.Department',on_delete=models.CASCADE)
