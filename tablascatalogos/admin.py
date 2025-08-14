
from django.contrib import admin
from .models import Nivel1,Nivel2,Nivel3,Incidencias,Estados

@admin.register(Nivel1)
class Nivel1Admin(admin.ModelAdmin):
    list_display = ('descripcion', 'fecha_registro', 'usuario', 'estado')
    search_fields = ('id', 'descripcion')
    list_filter = ('estado', 'fecha_registro')
    ordering = ('-fecha_registro',)
    exclude = ('usuario',)  # Oculta el campo usuario en el formulario

    def save_model(self, request, obj, form, change):
        if not change:  # Solo establecer usuario al crear, no al editar
            obj.usuario = request.user
        super().save_model(request, obj, form, change)


@admin.register(Nivel2)
class Nivel2Admin(admin.ModelAdmin):
    list_display = ('id_nivel1', 'descripcion', 'fecha_registro', 'usuario', 'estado')
    search_fields = ('descripcion',)
    list_filter = ('estado', 'fecha_registro', 'id_nivel1')
    ordering = ('-fecha_registro',)
    exclude = ('usuario',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.usuario = request.user
        super().save_model(request, obj, form, change)



@admin.register(Nivel3)
class Nivel3Admin(admin.ModelAdmin):
    list_display = ('id_nivel1', 'id_nivel2', 'descripcion', 'fecha_registro', 'usuario', 'estado')
    search_fields = ('descripcion',)
    list_filter = ('estado', 'fecha_registro', 'id_nivel1', 'id_nivel2')
    ordering = ('-fecha_registro',)
    exclude = ('usuario',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.usuario = request.user
        super().save_model(request, obj, form, change)


@admin.register(Incidencias)
class IncidenciasAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'fecha', 'usuario', 'estado')
    search_fields = ('descripcion',)
    list_filter = ('estado', 'fecha')
    exclude = ('usuario',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.usuario = request.user
        super().save_model(request, obj, form, change)


@admin.register(Estados)
class EstadosAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion', 'estado')
    list_display = ('id', 'descripcion', 'estado')
    search_fields = ('descripcion',)
    list_filter = ('estado',)
    ordering = ('descripcion',)
    


