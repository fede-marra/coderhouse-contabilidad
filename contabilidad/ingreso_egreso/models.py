from datetime import date
from email.policy import default
from email.utils import format_datetime, formatdate
from multiprocessing.sharedctypes import Value
from django.db import models
import datetime


class Ingreso(models.Model):
    tipo_ingreso = models.ForeignKey('Tipo_ingreso', on_delete=models.CASCADE)
    de_quien = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=1000)
    monto = models.IntegerField(default=0)
    fecha = models.DateField(default=datetime.date.today)


class Egreso(models.Model):
    tipo_egreso = models.ForeignKey('Tipo_egreso', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=1000)
    monto = models.IntegerField(default=0)
    fecha = models.DateField(default=datetime.date.today)


class Tipo_egreso(models.Model):
    nombre = models.CharField(max_length=30)

class Persona(models.Model):
    nombre = models.CharField(max_length=30)