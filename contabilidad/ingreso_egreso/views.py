

from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render
from ingreso_egreso.models import Persona, Ingreso, Egreso, Tipo_egreso
# from ingreso_egreso.forms import *
from django.contrib import messages

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

# Personas


class PersonaList(ListView):
    model = Persona
    template_name = 'persona/persona_list.html'


class PersonaDetail(DetailView):
    model = Persona
    template_name = 'persona/persona_detail.html'


class PersonaCreate(CreateView):
    model = Persona
    fields = ['nombre']
    template_name = 'persona/persona_form.html'
    success_url = reverse_lazy('persona_list')


class PersonaUpdate(UpdateView):
    model = Persona
    fields = ['nombre']
    template_name = 'persona/persona_form.html'
    success_url = reverse_lazy('persona_list')


class PersonaDelete(DeleteView):
    model = Persona
    template_name = 'persona/persona_delete.html'
    success_url = reverse_lazy('persona_list')


# Ingresos
# Egresos

# def ingreso(request):

#     ing = ingresos.objects.all
#     if request.method == "POST":
#         form = ingresosForm(request.POST)

#         if form.is_valid():
#             dequien = form.cleaned_data["dequien"]
#             descripcion = form.cleaned_data["descripcion"]
#             monto = form.cleaned_data["monto"]
#             fecha = form.cleaned_data["fecha"]
#             ingresos.objects.create(
#                 dequien=dequien, descripcion=descripcion, monto=monto, fecha=fecha)
#             messages.success(request, "El ingreso se ha registrado con exito")
#         else:
#             messages.error(request, form.errors.as_text())
#         return HttpResponseRedirect("/ingresos")
#     elif request.method == "GET":
#         form = ingresosForm()

#     else:
#         return HttpResponseBadRequest("Error no conozco ese metodo para esta request")

#     return render(request, 'ingresos.html', {'form': form, "ingresos": ing})


# def egreso(request):
#     egr = egresos.objects.all
#     if request.method == "POST":
#         form = egresosForm(request.POST)
#         if form.is_valid():
#             tipo = form.cleaned_data["tipo"]
#             descripcion = form.cleaned_data["descripcion"]
#             monto = form.cleaned_data["monto"]
#             fecha = form.cleaned_data["fecha"]
#             egresos.objects.create(
#                 tipo=tipo, descripcion=descripcion, monto=monto, fecha=fecha)
#             messages.success(request, "El egreso se ha registrado con exito")
#         else:
#             messages.error(request, form.errors.as_text())
#         return HttpResponseRedirect("/egresos")
#     elif request.method == "GET":
#         form = egresosForm()
#     else:
#         return HttpResponseBadRequest("Error no conozco ese metodo para esta request")

#     return render(request, 'egresos.html', {'form': form, "egresos": egr})


# def tipoEgreso(request):
#     if request.method == "POST":
#         form = tipo_egresoForm(request.POST)
#         if form.is_valid():
#             tipos = form.cleaned_data["tipos"]
#             tipo_egreso.objects.create(tipos=tipos)
#             messages.success(
#                 request, "El tipo de egreso se ha registrado con exito")
#         return HttpResponseRedirect("/tiposEgresos")
#     elif request.method == "GET":
#         form = tipo_egresoForm()
#     else:
#         return HttpResponseBadRequest("Error no conozco ese metodo para esta request")

#     return render(request, 'tiposEgresos.html', {'form': form})


# def persona(request):
#     if request.method == "POST":
#         form = personasForm(request.POST)
#         if form.is_valid():
#             nombres = form.cleaned_data["nombres"]
#             personas.objects.create(nombres=nombres)
#             messages.success(request, 'La persona se ha registrado con exito')
#         return HttpResponseRedirect("/personas")
#     elif request.method == "GET":
#         form = personasForm()
#     else:
#         return HttpResponseBadRequest("Error no conozco ese metodo para esta request")

#     return render(request, 'personas.html', {'form': form})


# def mostrarPersonas(request):
#     per = personas.objects.all
#     diccionario = {"personas": per}
#     return render(request, "mostrarPersonas.html", diccionario)


# def mostrarTiposEgresos(request):
#     egre = tipo_egreso.objects.all
#     diccionario = {"tipos": egre}
#     return render(request, "mostrarEgresos.html", diccionario)


# def busqueda(request):
#     if request.method == "POST":
#         form = busquedaForm(request.POST)
#         if form.is_valid():
#             opcion = form.cleaned_data["opcion"]
#             opcionAccion = form.cleaned_data["opcionAccion"]
#             if opcionAccion == "buscar":
#                 if opcion == "ingresos":
#                     suma = 0
#                     h = 0
#                     for h in ingresos.objects.all():
#                         suma = suma + h.monto
#                     valor = ingresos.objects.all
#                     return render(request, 'busqueda.html', {'form': form, "ingresos": valor, "tipo": opcion, "suma": suma})
#                 elif opcion == "egresos":
#                     suma = 0
#                     h = 0
#                     for h in egresos.objects.all():
#                         suma = suma + h.monto
#                     valor = egresos.objects.all
#                     return render(request, 'busqueda.html', {'form': form, "egresos": valor, "tipo": opcion, "suma": suma})
#                 elif opcion == "tipo_egresos":
#                     valor = tipo_egreso.objects.all
#                     return render(request, 'busqueda.html', {'form': form, "tipos": valor, "tipo": opcion})
#                 else:
#                     opcion = "personas"
#                     valor = personas.objects.all
#                     return render(request, 'busqueda.html', {'form': form, "personas": valor, "tipo": opcion})
#             if opcionAccion == "eliminar":
#                 if opcion == "ingresos":
#                     valor = ingresos.objects.all
#                     id = form.cleaned_data["identificar"]
#                     valores = ingresos.objects.filter(id=id)
#                     valores.delete()
#                     messages.success(
#                         request, "El ingreso se ha eliminado con exito")
#                 if opcion == "egresos":
#                     valor = egresos.objects.all
#                     id = form.cleaned_data["identificar"]
#                     valores = egresos.objects.filter(id=id)
#                     valores.delete()
#                     messages.success(
#                         request, "El egreso se ha eliminado con exito")
#                 if opcion == "tipo_egresos":
#                     valor = tipo_egreso.objects.all
#                     id = form.cleaned_data["identificar"]
#                     valores = tipo_egreso.objects.filter(id=id)
#                     valores.delete()
#                     messages.success(
#                         request, "El tipo de egreso se ha eliminado con exito")
#                 if opcion == "personas":
#                     valor = personas.objects.all
#                     id = form.cleaned_data["identificar"]
#                     valores = personas.objects.filter(id=id)
#                     valores.delete()
#                     messages.success(
#                         request, "La persona se ha eliminado con exito")
#         return HttpResponseRedirect("/busqueda")
#     elif request.method == "GET":
#         form = busquedaForm()
#     else:
#         return HttpResponseBadRequest("Error no conozco ese metodo para esta request")

#     return render(request, 'busqueda.html', {'form': form})
