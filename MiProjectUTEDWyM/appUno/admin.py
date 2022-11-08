#del framework django importamos el administrador
#de models importamos el modelo contacto
from django.contrib import admin
from .models import Contacto
#de models importamos el modelo apuntes
from .models import Apuntes

#creamos una clase para administrar contacto
#que va a listar la información dentro de un arreglo
class AdminContacto(admin.ModelAdmin):
    list_display = ["__str__","nombre","apellido","celular","email"]
    
    #hereda del objeto contacto
class Meta(object):
    model = Contacto 

#creamos una clase para administrar apuntes
#que va a listar la información dentro de un arreglo
class AdminApuntes(admin.ModelAdmin):
    list_display = ["__str__","nombre","contenido"]
    
    #hereda del objeto apuntes
class Meta(object):
    model = Apuntes 

#registra en el entorno del administrador el modelo contacto
admin.site.register(Contacto,AdminContacto)
#registra en el entorno del administrador el modelo contacto
admin.site.register(Apuntes,AdminApuntes)
