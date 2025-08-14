from django.db import models
from django.contrib.auth.models import User
from tablascatalogos.models import Nivel1, Nivel2, Nivel3, Incidencias, Estados
from django.utils import timezone

class Incidencia(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # El admin.py lo llenará
    id_nivel1 = models.ForeignKey(Nivel1, on_delete=models.CASCADE)
    id_nivel2 = models.ForeignKey(Nivel2, on_delete=models.CASCADE)
    id_nivel3 = models.ForeignKey(Nivel3, on_delete=models.CASCADE)
    incidencias = models.ForeignKey(Incidencias, on_delete=models.CASCADE, null=True, blank=True)
    observaciones = models.TextField()
    id_estado = models.ForeignKey(Estados, on_delete=models.CASCADE)
    observacion_destinatario = models.TextField(blank=True, null=True)

    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_abierto = models.DateTimeField(auto_now_add=True)
    fecha_cierre = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.usuario.first_name} {self.usuario.last_name} - {self.id_estado.descripcion}"

    def save(self, *args, **kwargs):
        # Si es nuevo y no está cerrado, poner "Abierto"
        if not self.pk and self.id_estado.descripcion.lower() != "cerrado":
            self.id_estado = Estados.objects.get(descripcion__iexact="Abierto")

        # Si pasa a cerrado y no tiene fecha de cierre, asignarla
        if self.id_estado.descripcion.lower() == "cerrado" and self.fecha_cierre is None:
            self.fecha_cierre = timezone.now()

        super().save(*args, **kwargs)
