from django.shortcuts import render
from django.db.models import Count
from incidencias.models import Incidencia  # Importa desde la app incidencias
from tablascatalogos.models import Estados

# graficos/views.py


def grafico_por_estado(request):
    # 1. Obtener el total de incidencias para el cálculo del porcentaje
    total_incidencias = Incidencia.objects.count()

    # Si no hay incidencias, se evita la división por cero
    if total_incidencias == 0:
        return render(request, 'dashboard/graficoestados.html', {'labels': [], 'data_porcentajes': []})

    # 2. Contar el número de incidencias por cada id de estado
    conteo_por_estado = Incidencia.objects.values('id_estado').annotate(
        total=Count('id_estado')
    )

    # 3. Obtener las descripciones de los estados para las etiquetas del gráfico
    estados_ids = [item['id_estado'] for item in conteo_por_estado]
    estados_map = {
        estado.id: estado.descripcion
        for estado in Estados.objects.filter(id__in=estados_ids)
    }

    # 4. Preparar los datos para el gráfico
    labels = []
    data_porcentajes = []

    for item in conteo_por_estado:
        estado_id = item['id_estado']
        total = item['total']
        
        # Obtener la descripción del estado usando el mapeo
        label_descripcion = estados_map.get(estado_id, 'Desconocido')
        labels.append(label_descripcion)
        
        # Calcular el porcentaje
        porcentaje = round((total / total_incidencias) * 100, 2)
        data_porcentajes.append(porcentaje)

    # 5. Pasar los datos al template
    context = {
        'labels': labels,
        'data_porcentajes': data_porcentajes,
    }
    return render(request, 'dashboard/graficoestados.html', context)