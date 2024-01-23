from django.contrib import admin
from employee_salary.models import EmployeeSalary

class EmployeeSalaryAdmin(admin.ModelAdmin):
    list_display = ('employee','salary','start_date','end_date')
    list_filter = ('employee','start_date','end_date')
    search_fields = ('employee_name',)

admin.site.register(EmployeeSalary, EmployeeSalaryAdmin)
