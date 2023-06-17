from django.db import models

# Create your models here.
class Animal(models.Model):
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    encargado = models.TextField(max_length=100)
    raza = models.TextField(max_length=100)

