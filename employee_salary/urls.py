from django.urls import path
from . import views

urlpatterns = [
    path('salary',views.salary),
]