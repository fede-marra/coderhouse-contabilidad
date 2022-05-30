from django import forms
from django.conf import settings
from ingreso_egreso.models import personas, tipo_egreso


class ingresosForm(forms.Form):
    items = []
    records = personas.objects.all()
    for n in records:
        items.append((n.nombres,n.nombres))
    dequien = forms.ChoiceField(label="Nombre", choices=items)
    descripcion = forms.CharField(label="Descripcion",max_length=1000)
    monto = forms.IntegerField(label="Monto")
    fecha = forms.DateField(label="Fecha", input_formats=settings.DATE_INPUT_FORMATS)

class egresosForm(forms.Form):
    items = []
    records = tipo_egreso.objects.all()
    for n in records:
        items.append((n.tipos,n.tipos)) 
    tipo = forms.ChoiceField(label="Tipo", choices=items)
    descripcion = forms.CharField(label="Descripcion",max_length=1000)
    monto = forms.IntegerField(label="Monto")
    fecha = forms.DateField(label="Fecha",input_formats=settings.DATE_INPUT_FORMATS)

class tipo_egresoForm(forms.Form):
    tipos = forms.CharField(label="Tipos", max_length=30)

class personasForm(forms.Form):
    nombres = forms.CharField(label="Personas", max_length=30)
    