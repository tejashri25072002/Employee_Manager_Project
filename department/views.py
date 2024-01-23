from django.shortcuts import render
from .models import Department

def department(request):
    dept = Department.objects.all()
    context={}
    context['departments']=dept
    return render(request,'department.html',context)
