"""MiProjectUTEDWyM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from appUno.views import home_view, listar_contactos, contact_view, notas_view, index_view, crear_notas, vernotas, eliminarContacto, eliminarNota, edicionContacto, actualizarContacto, edicionNota, actualizarNota

urlpatterns = [
    path('',home_view, name='home'),
    path('home',home_view, name='home'),
    path('index',index_view, name='index'),
    path('notas/',notas_view, name='notas'),
    path('contact/',listar_contactos, name='listar_c'),
    path('crear/',crear_notas, name='listar_c'),
    path('vernotas/',vernotas, name='vernotas'),
    path('eliminarContacto/<int:id>',eliminarContacto),
    path('eliminarNota/<int:id>',eliminarNota),
    path('edicionContacto/<int:id>',edicionContacto),
    path('actualizarContacto/<int:id>',actualizarContacto),
    path('edicionNota/<int:id>',edicionNota),
    path('actualizarNota/<int:id>',actualizarNota),
    path('admin/', admin.site.urls),
]
