from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Nivel1(models.Model):
    descripcion = models.TextField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.descripcion
    
    class Meta:
        verbose_name = 'Nivel1'
        verbose_name_plural ='Nivel1'
    

class Nivel2(models.Model):
    id_nivel1 = models.ForeignKey(Nivel1, on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)

    def __str__(self):
    #    return f"{self.id_nivel1.descripcion} - {self.descripcion}"
         return self.descripcion
    
    class Meta:
        verbose_name = 'Nivel2'
        verbose_name_plural ='Nivel2'
    

class Nivel3(models.Model):
    id_nivel1 = models.ForeignKey('Nivel1', on_delete=models.CASCADE)
    id_nivel2 = models.ForeignKey('Nivel2', on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)

    def __str__(self):
       # return f"{self.id_nivel1.descripcion } - {self.id_nivel2.descripcion} - {self.descripcion}"
         return self.descripcion

    
    class Meta:
        verbose_name = 'Nivel3'
        verbose_name_plural ='Nivel3'
    

class Incidencias(models.Model):
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.descripcion
    
    
    class Meta:
        verbose_name = 'Incidentes'
        verbose_name_plural ='Incidentes'
    
    

class Estados(models.Model):
    
    descripcion = models.TextField()
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.descripcion
    
    
    class Meta:
        verbose_name = 'Estados'
        verbose_name_plural ='Estados'
    