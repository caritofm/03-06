from django.shortcuts import render
from .models import Genero,Alumnos


def index(request):
    alumnos = Alumnos.objects.all()
    context= {"alumnos":alumnos}
    return render(request, "alumnos/index.html", context)

def listadoSQL(request):
    alumnos = Alumnos.objects.raw("SELECT *FROM alumnos_alumno")
    context = {"alumnos":alumnos}
    return render (request,"alumnos/listadoSQL.html")

# Create your views here.
