from django.urls import path
from . import views

urlpatterns =[
    path('department/',views.department),
]