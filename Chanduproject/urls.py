"""Chanduproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from xyz import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('sampletxt/',views.sample),
    path('center/',views.centerexample),
    path('fun/',views.funitem),
    path('stringvalue/<str:name>/',views.stringvalueex),
    path('intvalue/<int:num>/',views.intvalueex),
    path('dispaly/<int:num>/<str:name>/',views.displaydata),
    path('samplehtml/',views.samplehtmlex,name=''),
    path('demohtml/',views.demohtmlex,name=''),
    path('externalhtml/',views.externalhtmlex,name=''),
    path('bootstrap/',views.bootstrapex,name=''),
    path('login/',views.loginex,name=''),
    path('register/',views.registerex,name=''),
    #path('details/',views.detailsex,name='')
    path('',include('app2.urls')),
    path('forms/',include('formsapp.urls')),
]
