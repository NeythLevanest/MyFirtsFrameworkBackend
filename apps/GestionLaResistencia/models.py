from django.db import models

# Create your models here.
class Persona(models.Model):
    idPersona = models.CharField(max_length=10)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    fechaNacimiento = models.DateField()

    def NombreCompleto(self):
        cadena="{0} {1}"
        return cadena.format(self.apellido, self.nombre)
    def __str__(self):
        return self.NombreCompleto()