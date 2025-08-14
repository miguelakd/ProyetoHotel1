
# Register your models here.
from django.contrib import admin
from .models import Incidencia

@admin.register(Incidencia)
class IncidenciaAdmin(admin.ModelAdmin):
    list_display = ('usuario_nombre_apellido', 'id_nivel1', 'id_nivel2', 'id_nivel3', 'incidencias', 'observaciones', 'id_estado', 'observacion_destinatario', 'fecha_registro', 'fecha_abierto', 'fecha_cierre')
    search_fields = ('observaciones', 'observacion_destinatario', 'incidencias__descripcion', 'id_estado__descripcion')
    list_filter = ('id_estado', 'fecha_registro', 'fecha_abierto', 'fecha_cierre', 'usuario')
    exclude = ('usuario','fecha_cierre',)


    def usuario_nombre_apellido(self, obj):
        return f"{obj.usuario.first_name} {obj.usuario.last_name}"
    usuario_nombre_apellido.short_description = "Usuario"

    def save_model(self, request, obj, form, change):
        if not change:
            obj.usuario = request.user
        super().save_model(request, obj, form, change)
