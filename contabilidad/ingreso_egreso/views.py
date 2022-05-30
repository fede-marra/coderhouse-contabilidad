from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render
from ingreso_egreso.models import egresos, ingresos, tipo_egreso, personas
from ingreso_egreso.forms import *
from django.contrib import messages

#def index(request):
#    pass
#    #diccionario = {"ingresos":ing}
#    #return render(request,"mostrar.html",diccionario)

def ingreso(request):
    
    ing = ingresos.objects.all
    if request.method == "POST":
        form = ingresosForm(request.POST)
        if form.is_valid():
            dequien = form.cleaned_data["dequien"]
            descripcion = form.cleaned_data["descripcion"]
            monto = form.cleaned_data["monto"]
            fecha = form.cleaned_data["fecha"]
            ingresos.objects.create(dequien=dequien, descripcion=descripcion, monto=monto, fecha=fecha)
            messages.success(request,"El ingreso se ha registrado con exito")
        else:
            messages.error(request,form.errors.as_text())
        return HttpResponseRedirect("/ingresos")
    elif request.method == "GET":
        form = ingresosForm()
       
        
    else:
        return HttpResponseBadRequest("Error no conozco ese metodo para esta request")

    return render(request,'ingresos.html',{'form':form, "ingresos":ing})

def egreso(request):
    egr = egresos.objects.all
    if request.method == "POST":
        form = egresosForm(request.POST)
        if form.is_valid():
            tipo = form.cleaned_data["tipo"]
            descripcion = form.cleaned_data["descripcion"]
            monto = form.cleaned_data["monto"]
            fecha = form.cleaned_data["fecha"]
            egresos.objects.create(tipo=tipo, descripcion=descripcion, monto=monto, fecha=fecha)
            messages.success(request,"El ingreso se ha registrado con exito")
        else:
            messages.error(request,form.errors.as_text())
        return HttpResponseRedirect("/egresos")
    elif request.method == "GET":
        form = egresosForm()
    else:
        return HttpResponseBadRequest("Error no conozco ese metodo para esta request")

    return render(request,'egresos.html',{'form':form, "egresos":egr})

def tipoEgreso(request):
    if request.method == "POST":
        form = tipo_egresoForm(request.POST)
        if form.is_valid():
            tipos = form.cleaned_data["tipos"]
            tipo_egreso.objects.create(tipos=tipos)
            messages.success(request,"El tipo de egreso se ha registrado con exito")
        return HttpResponseRedirect("/tiposEgresos")
    elif request.method == "GET":
        form = tipo_egresoForm()
    else:
        return HttpResponseBadRequest("Error no conozco ese metodo para esta request")

    return render(request,'tiposEgresos.html',{'form':form})

def persona(request):
    if request.method == "POST":
        form = personasForm(request.POST)
        if form.is_valid():
            nombres = form.cleaned_data["nombres"]
            personas.objects.create(nombres=nombres)
            messages.success(request,"La persona se ha registrado con exito")
        return HttpResponseRedirect("/personas")
    elif request.method == "GET":
        form = personasForm()
    else:
        return HttpResponseBadRequest("Error no conozco ese metodo para esta request")

    return render(request,'personas.html',{'form':form})

def mostrarPersonas(request):
    per = personas.objects.all
    diccionario = {"personas":per}
    return render(request,"mostrarPersonas.html",diccionario)

def mostrarTiposEgresos(request):
    egre = tipo_egreso.objects.all
    diccionario = {"tipos":egre}
    return render(request,"mostrarEgresos.html",diccionario)
