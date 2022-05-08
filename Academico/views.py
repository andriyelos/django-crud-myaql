from django.shortcuts import redirect, render
from .models import Curso
from django.contrib import messages
# Create your views here.

def home(request):
    curso = Curso.objects.all() 
    messages.success(request, '¡Cursos listados!')
    return render(request,"gestionCursos.html",{"cursos": curso})

def registrarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos= request.POST['numCreditos']

    curso = Curso.objects.create(
        codigo = codigo,nombre=nombre,creditos = creditos)
    messages.success(request, '¡Curso registrado!')
    return redirect('/')

def edicionCursos(request,codigo):
    curso = Curso.objects.get(codigo= codigo)
    return render(request,"edicionCurso.html", {"cursos":curso})

def editarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos= request.POST['numCreditos']

    curso = Curso.objects.get(codigo = codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()

    messages.success(request, '¡Cursos Actualizado!')
    
    return redirect('/')


def eliminarCurso(request,codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()

    messages.success(request, '¡Cursos Eliminado!')

    return redirect('/')

