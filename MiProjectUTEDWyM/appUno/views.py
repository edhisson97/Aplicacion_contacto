#from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .forms import Formulario, FormularioNotas #importamos forms
from .models import Contacto, Apuntes
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def home_view(request):
    f = Formulario(request.POST or None) #f es un objeto de la Pe:ción POST
    if request.method == 'POST':
        if f.is_valid():
            datos = f.cleaned_data
            c = Contacto()
            c.nombre = datos.get("nombre")
            c.apellido = datos.get("apellido")
            c.celular = datos.get("celular")
            c.cedula = datos.get("cedula")
            c.email = datos.get("email")
            if c.save() != True:
                print('Imprimo en pantalla y guardo data en BD')
                print(f.cleaned_data)
                messages.success(request, "Contacto agregado corectamente")
                return redirect(home_view)
    context = {
        "form":f,
    }
    return render(request,"home.html",context)

#metodo para listar contactos
def listar_contactos(request):
    contactos = Contacto.objects.all()
    return render(request, "listar_c.html", {"contactos": contactos})

def contact_view(request,):
    return render(request, "contact.html", {})

def crear_notas(request,):
    #crea el formulario y lo obtiene
    form = FormularioNotas(request.POST or None)
    #pregunta si se han enviado por el metodo post datos en el formulario sino
    #solo lo crea en pantalla
    if request.method == 'POST':
        #el formulario es valido
        if form.is_valid():
            #limpia el formulario
            datos = form.cleaned_data
            #se guarda en la base de datos
            notas = Apuntes()
            notas = form.save()
            if form.save() !=True:
                print('Imprimo en pantalla y guardo data en BD')
                #muestra en pantalla que esta registrada la nota
                messages.success(request, "Nota registrada corectamente")
                return redirect(crear_notas)
    #retorna un renderizado al html y envia el formulario
    return render(request, "crearnotas.html", {"form": form})

#metodo para listar las notas
def vernotas(request):
    busqueda = request.GET.get("buscar")
    apuntes = Apuntes.objects.all()
    print(request.GET)
    if busqueda:
        apuntes = Apuntes.objects.filter(
            #print('dentro del if')
            #Q(email = busqueda) |
            Q(nombre__icontains = busqueda) |
            Q(contenido__icontains = busqueda) 
        ).distinct()
    
    return render(request, "vernotas.html", {"apuntes": apuntes})

def index_view(request,):
    return render(request, "index.html", {})

#metodo para eliminar los contactos
def eliminarContacto(request, id):
    contacto = Contacto.objects.get(id=id)
    contacto.delete()
    messages.success(request, "Contacto eliminado corectamente")
    return redirect('/listar_c.html')

#metodo para eliminar los notas
def eliminarNota(request, id):
    notas = Apuntes.objects.get(id=id)
    notas.delete()
    messages.success(request, "Nota eliminada corectamente")
    return redirect('/vernotas')

def edicionContacto(request, id):
    contacto = Contacto.objects.get(id=id)
    f = Formulario(initial={'nombre':contacto.nombre,
                            'apellido':contacto.apellido,
                            'celular':contacto.celular,
                            'cedula':contacto.cedula,
                            'email':contacto.email})
    
     #   if formulario.is_valid():
      #      formulario.save()
       #     print('Imprimo en pantalla y guardo data en BD')
        #    messages.success(request, "Contacto editado corectamente")
    context = {
        "form":f,
        "contacto":contacto,
    }
    return render(request, "edicionContacto.html", context)

def actualizarContacto(request, id):
    contacto = Contacto.objects.get(pk=id)
    form = Formulario(request.POST, instance=contacto)
    if form.is_valid():
        form.save()
        messages.success(request, "Contacto actualizado corectamente.")
    return redirect('/contact')

def edicionNota(request, id):
    nota = Apuntes.objects.get(id=id)
    f = FormularioNotas(initial={'email':nota.email,
                            'nombre':nota.nombre,
                            'contenido':nota.contenido})
    
     #   if formulario.is_valid():
      #      formulario.save()
       #     print('Imprimo en pantalla y guardo data en BD')
        #    messages.success(request, "Contacto editado corectamente")
    context = {
        "form":f,
        "nota":nota,
    }
    return render(request, "edicionNotas.html", context)

def actualizarNota(request, id):
    nota = Apuntes.objects.get(pk=id)
    form = FormularioNotas(request.POST, instance=nota)
    if form.is_valid():
        form.save()
        messages.success(request, "Nota actualizada corectamente.")
    return redirect('/vernotas')

#metodo para listar contactos a los que se adjuntaran notas
def notas_view(request):
    #if request.method =='GET':
        #print('Success!')
        #n = Apuntes()
        #n.cedula = request.GET["cedula"]
        #n.cedula = request.GET["nombre"]
        #n.cedula = request.GET["descripcion"]
        #n.save()
    return redirect('/')
