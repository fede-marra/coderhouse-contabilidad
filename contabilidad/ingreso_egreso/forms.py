
from django import forms
from django.conf import settings
from ingreso_egreso.models import personas, tipo_egreso

def _lista_personas():
    lista = []
    for persona in personas.objects.all():
        lista.append((persona.nombres, persona.nombres))

    return lista

def _lista_tipo_egresos():
    lista = []
    for item in tipo_egreso.objects.all():
        lista.append((item.tipos, item.tipos))
    return lista

class ingresosForm(forms.Form):
    dequien = forms.ChoiceField(label="Nombre", choices=_lista_personas)
    descripcion = forms.CharField(label="Descripcion",max_length=1000)
    monto = forms.IntegerField(label="Monto")
    fecha = forms.DateField(label="Fecha", input_formats=settings.DATE_INPUT_FORMATS)

class egresosForm(forms.Form):
    tipo = forms.ChoiceField(label="Tipo", choices=_lista_tipo_egresos)
    descripcion = forms.CharField(label="Descripcion",max_length=1000)
    monto = forms.IntegerField(label="Monto")
    fecha = forms.DateField(label="Fecha",input_formats=settings.DATE_INPUT_FORMATS)

class tipo_egresoForm(forms.Form):
    tipos = forms.CharField(label="Tipos", max_length=30)

class personasForm(forms.Form):
    nombres = forms.CharField(label="Personas", max_length=30)

#def borrar(request, identificador):
#
#    if request.method == "GET":
#        persona = familiares.objects.filter(id=int(identificador)).first()
#        if persona:
#            persona.delete()
#            messages.success(request, 'El item fue eliminado correctamente')
#        return HttpResponseRedirect("/Familia/")
#    else:
#        return HttpResponseBadRequest("Error no conozco ese metodo request")

class busquedaForm(forms.Form):
    bases = (("ingresos","ingresos"),("egresos","egresos"),("tipo_egresos","tipo_egresos"),("personas","personas"))
    accion = (("buscar","buscar"),("eliminar","eliminar"))
    opcion = forms.ChoiceField(label="Busqueda", choices=bases)
    opcionAccion = forms.ChoiceField(label="Accion", choices=accion)
    identificar = forms.CharField(label="id", max_length=30, required=False)