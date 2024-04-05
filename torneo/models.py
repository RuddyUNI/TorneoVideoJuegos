from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    fecha = models.DateField()
    juego = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo
    