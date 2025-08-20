from django.urls import path
from . import views

urlpatterns = [
    path("graficoestados/", views.grafico_por_estado , name="graficoestados"),
    
]
