# dashboard/admin.py

from django.contrib import admin
from django.urls import path
from django.db import models
from django.shortcuts import render
from django.db.models import Count
from incidencias.models import Incidencia
from tablascatalogos.models import Estados

# 1. Definimos el modelo "dummy" AQUI MISMO
class Dummy(models.Model):
    class Meta:
        verbose_name = "Dashboard"
        verbose_name_plural = "Dashboard"
        app_label = "dashboard"
        managed = False

# 2. Registramos el modelo y definimos la lógica de la página
@admin.register(Dummy)
class DummyAdmin(admin.ModelAdmin):
    # Sobrescribe las URLs del administrador para añadir la tuya
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                '',
                self.admin_site.admin_view(self.dashboard_view),
                name='dashboard_view',
            ),
        ]
        return custom_urls + urls

    # Deshabilitamos los permisos para que no se pueda agregar, editar o eliminar
    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

    # 3. La vista que contendrá la lógica de los gráficos
    def dashboard_view(self, request):
        total_incidencias = Incidencia.objects.count()

        if total_incidencias == 0:
            context = {
                'title': 'Gráficos de Incidencias',
                'labels': [],
                'data_porcentajes': [],
                'data_conteos': [],
            }
        else:
            conteo_por_estado = Incidencia.objects.values('id_estado').annotate(
                total=Count('id_estado')
            ).order_by('id_estado')
            
            estados_ids = [item['id_estado'] for item in conteo_por_estado]
            estados_map = {
                estado.id: estado.descripcion
                for estado in Estados.objects.filter(id__in=estados_ids)
            }

            labels = []
            data_porcentajes = []
            data_conteos = []
            
            for item in conteo_por_estado:
                label_descripcion = estados_map.get(item['id_estado'], 'Desconocido')
                labels.append(label_descripcion)
                porcentaje = round((item['total'] / total_incidencias) * 100, 2)
                data_porcentajes.append(porcentaje)
                data_conteos.append(item['total'])

            context = {
                'title': 'Gráficos de Incidencias',
                'labels': labels,
                'data_porcentajes': data_porcentajes,
                'data_conteos': data_conteos,
            }

        contexto_admin = self.admin_site.each_context(request)
        contexto_admin.update(context)

        return render(request, 'dashboard/graficoestados.html', contexto_admin)