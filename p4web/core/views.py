from django.shortcuts import render, redirect
from .models import Libro
from .forms import LibroForm

# Create your views here.

def home(request):

    return render(request, 'core/home.html')

def registro(request):

    return render(request, 'core/registro.html')

def libros(request):
    libros=Libro.objects.all()
    datos={
        'libros':libros
    }

    return render(request, 'core/libros.html', datos)

def form_libro(request):
    datos = {
        'form': LibroForm()
    }
    if request.method == 'POST':
        formulario = LibroForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Libro ingresado"
    

    return render(request, 'core/form_libro.html', datos)

def form_mod_libro(request, id):
    libro = Libro.objects.get(ISBN=id)
    datos = {
        'form': LibroForm(data=request.POST, instance=libro)
    }
    if request.method == 'POST':
        formulario = LibroForm(data=request.POST, instance=libro)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos modificados"
    return render(request, 'core/form_mod_libro.html', datos)

def form_del_libro(request,id):
    libro = Libro.objects.get(ISBN=id)
    libro.delete()
    return redirect(to=libros)