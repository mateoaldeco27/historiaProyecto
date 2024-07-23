from django.contrib import admin
from FeriaCiencias.models import Proyecto, Seccion, Articulo, ArtImagen

admin.site.register(Proyecto)

class seccionDetalle(admin.ModelAdmin):
    list_display = ["id", "titulo", "descripcion", "imagen", "idProyecto", "link"]


admin.site.register(Seccion, seccionDetalle)
admin.site.register(Articulo)
admin.site.register(ArtImagen)

