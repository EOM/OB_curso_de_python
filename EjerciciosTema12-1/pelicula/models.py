from django.db import models
from django.urls import reverse
from director.models import Director


class Pelicula(models.Model):
    nombre = models.CharField(max_length=64, help_text='Nombre de la Pelicula')
    descripcion = models.CharField(max_length=250, help_text='Descripción de la Pelicula')
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    def get_obsolute_url(self):
        return reverse('pelicula-detalle', args=[self.id])
