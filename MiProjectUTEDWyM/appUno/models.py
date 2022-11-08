from django.db import models

#la clase contacto contiene las variables siguientes 
class Contacto(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    celular=models.CharField(max_length=10)
    cedula=models.CharField(max_length=30)
    email=models.EmailField()
    #nos devuelve todo en tipo dato
    def __str__(self): 
        #apunta con email
        return  self.email
    class Meta:
        db_table = 'contac'
        verbose_name = 'Contacto'
        verbose_name_plural = 'contactos'
        ordering = ['id']

#Creamos la clase para los apuntes 
class Apuntes(models.Model):
    email=models.ForeignKey(Contacto,null=True, on_delete=models.CASCADE,verbose_name='Nota del contacto') #id para asociar con contacto
    nombre=models.CharField(max_length=30, verbose_name='Nombre de la nota')
    contenido=models.TextField(verbose_name='Contenido de la nota')
#nos devuelve todo en tipo dato
def __str__(self): 
    #apunta con nombre
    return self.nombre