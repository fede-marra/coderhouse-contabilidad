from datetime import date
from email.policy import default
from email.utils import format_datetime, formatdate
from multiprocessing.sharedctypes import Value
from django.db import models
import datetime

class ingresos(models.Model):
    
    dequien = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=1000)
    monto = models.IntegerField(default=0)
    fecha = models.DateField(default=datetime.date.today)

class egresos(models.Model):
    tipo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=1000)
    monto = models.IntegerField(default=0)
    fecha = models.DateField(default=datetime.date.today)

class tipo_egreso(models.Model):
    tipos = models.CharField(max_length=30)
   
class personas(models.Model):
    nombres = models.CharField(max_length=30)