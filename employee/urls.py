from django.urls import path
from . import views

urlpatterns = [
    path('employee',views.employee),
    path('employee_hierarchy',views.employee_hierarchy),
]