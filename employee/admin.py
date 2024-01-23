from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name','email','address','designation','reporting_manager','department')
    list_filter = ('name','designation','department')
    search_fields = ('name','address','designation')

admin.site.register(Employee,EmployeeAdmin)