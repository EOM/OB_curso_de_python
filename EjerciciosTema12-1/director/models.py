from django.db import models


class Director(models.Model):
    nombre = models.CharField(max_length=64, help_text='Nombre del director')
    apellido = models.CharField(max_length=64, help_text='Apellido del director')

    def __str__(self):
        return self.nombre + ' ' + self.apellido
