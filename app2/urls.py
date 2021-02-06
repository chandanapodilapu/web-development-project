from django.urls import path
from app2 import views

urlpatterns=[
     path('demo/',views.demo),
     path('addstudent/',views.addstudent,name='addstudent'),
     path('details/',views.details,name='details'),
     path('update/<int:id>',views.update,name='update'),
     path('delete/<int:id>',views.delete,name='delete'),
     path('about/',views.about),
     path('home/',views.home)
]