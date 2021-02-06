from django.urls import path
from formsapp import views

urlpatterns = [
     path('d/',views.demo),
     path('reg/',views.reg),
]