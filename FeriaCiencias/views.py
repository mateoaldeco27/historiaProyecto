from django.shortcuts import render
from .models import Proyecto, Seccion, Articulo

def index(request):
    proyectos = Proyecto.objects.all()
    context = {"proyectos": proyectos}
    return render(request, "index.html", context)


def proyecto(request, pk):
    proyectos = Proyecto.objects.all()
    proyecto = Proyecto.objects.get(id=pk)
    secciones = Seccion.objects.filter(idProyecto__nombre__icontains=proyecto.nombre)
    context = {"proyecto": proyecto, "proyectos": proyectos, "secciones": secciones}
    return render(request, "ia/proyecto.html", context)


def seccion(request, pk):
    proyectos = Proyecto.objects.all()
    secciones = Seccion.objects.all()
    seccion = Seccion.objects.get(id=pk)
    articulos = Articulo.objects.filter(idSeccion__titulo__icontains=seccion.titulo)
    context = {"proyectos": proyectos, "secciones": secciones, "seccion": seccion, "articulos": articulos}
    return render(request, "ia/seccion.html", context)

def proyectoHistoria(request, pk):
    proyectos = Proyecto.objects.all()
    proyecto = Proyecto.objects.get(id=pk)
    secciones = Seccion.objects.filter(idProyecto__nombre__icontains=proyecto.nombre)
    context = {"proyecto": proyecto, "proyectos": proyectos, "secciones": secciones}
    return render(request, "historia/proyectoHistoria.html", context)


def seccionHistoria(request, pk):
    proyectos = Proyecto.objects.all()
    proyecto = Proyecto.objects.get(nombre__icontains="Ciencias Naturales")
    secciones = Seccion.objects.filter(idProyecto__nombre__icontains=proyecto.nombre).values()
    seccion = Seccion.objects.get(id=pk)
    articulos = Articulo.objects.filter(idSeccion__titulo__icontains=seccion.titulo).values()
    context = {"proyectos": proyectos, "secciones": secciones, "seccion": seccion, "articulos": articulos}
    return render(request, "historia/seccionHistoria.html", context)

# def articuloHistoria(request, pk):
#     proyectos = Proyecto.objects.all()
#     proyecto = Proyecto.objects.get(nombre__icontains="Ciencias Naturales")
#     secciones = Seccion.objects.filter(idProyecto__nombre__icontains=proyecto.nombre).values()
#     articulo = Articulo.objects.get(id=pk)
#     context = {"proyectos": proyectos, "secciones": secciones, "articulo": articulo}
#     return render(request, "historia/articuloHistoria.html", context)
def articuloHistoria(request, pk):
    proyectos = Proyecto.objects.all()
    proyecto = Proyecto.objects.get(nombre__icontains="Ciencias Naturales")
    secciones = Seccion.objects.filter(idProyecto__nombre__icontains=proyecto.nombre).values()
    articulo = Articulo.objects.get(id=pk)
    articulos = Articulo.objects.filter(idSeccion_id=articulo.idSeccion).values()
    
    context = {"proyectos": proyectos, "secciones": secciones, "articulo": articulo, "articulos":articulos}
    return render(request, "historia/articuloHistoria.html", context)