from django.shortcuts import render
from .models import Employee
from department.models import Department


def employee(request):
    emp = Employee.objects.all()
    context={}
    context['employees']=emp
    return render(request,'employee.html',context)

def employee_hierarchy(request):
    departments = Department.objects.all()
    employees = Employee.objects.filter(reporting_manager__isnull=True).order_by("department__name")
    context = {"departments": departments, "employees": employees}
    return render(request, "employee_hierarchy.html", context)
