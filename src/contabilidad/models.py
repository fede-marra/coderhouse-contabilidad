from datetime import date
from email.policy import default
from email.utils import format_datetime, formatdate
from multiprocessing.sharedctypes import Value
from django.db import models
from django.contrib.auth.models import User

import datetime


class Ingreso(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo_ingreso = models.ForeignKey('Tipo_ingreso', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=1000)
    monto = models.IntegerField(default=0)
    fecha = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.nombre


class Egreso(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo_egreso = models.ForeignKey('Tipo_egreso', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=1000)
    monto = models.IntegerField(default=0)
    fecha = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.nombre


class Tipo_egreso(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class Tipo_ingreso(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


# class Persona(models.Model):
#     nombre = models.CharField(max_length=30)
#     apellido = models.CharField(max_length=30)

#     def __str__(self):
#         return self.nombre
