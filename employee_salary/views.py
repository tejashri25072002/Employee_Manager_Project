from django.shortcuts import render
from .models import EmployeeSalary

def salary(request):
    sal = EmployeeSalary.objects.all()
    context={}
    context['salaries']=sal
    return render(request,'employee_salary.html',context)
