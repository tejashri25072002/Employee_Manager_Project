from django.db import models
from employee.models import Employee

class EmployeeSalary(models.Model):
    employee = models.ForeignKey('employee.Employee', on_delete=models.CASCADE)
    salary=models.DecimalField(max_digits=10,decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
