from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Nombre')
    telefono = models.IntegerField(verbose_name="Numero de telefono")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'

    def __str__(self):
        return self.nombre