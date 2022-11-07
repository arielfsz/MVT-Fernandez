from django.db import models

class Persona(models.Model):

    nombre = models.CharField(max_length=50)
    camiseta = models.IntegerField()
    nacimiento = models.DateField()