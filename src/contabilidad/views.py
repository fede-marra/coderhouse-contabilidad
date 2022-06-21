

from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render
from contabilidad.models import Ingreso, Egreso, Tipo_egreso
# from ingreso_egreso.forms import *
from django.contrib import messages

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView


from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# -------------------------------------------Base-------------------------------------------


class HomePageView(TemplateView):
    template_name = 'home.html'


class Login(LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy("egreso_list")


class Logout(LogoutView):
    template_name = 'logout.html'

# -------------------------------------------Tipo Egresos-------------------------------------------


class Tipo_egresoList(ListView, LoginRequiredMixin):
    model = Tipo_egreso
    template_name = 'tipo_egresos/tipo_egreso_list.html'


class Tipo_egresoDetail(DetailView, LoginRequiredMixin):
    model = Tipo_egreso
    template_name = 'tipo_egresos/tipo_egreso_detail.html'


class Tipo_egresoCreate(CreateView, LoginRequiredMixin):
    model = Tipo_egreso
    fields = ['nombre']
    template_name = 'form.html'
    success_url = reverse_lazy('tipo_egreso_list')


class Tipo_egresoUpdate(UpdateView, LoginRequiredMixin):
    model = Tipo_egreso
    fields = ['nombre']
    template_name = 'form.html'
    success_url = reverse_lazy('tipo_egreso_list')


class Tipo_egresoDelete(UserPassesTestMixin, DeleteView, LoginRequiredMixin):
    model = Tipo_egreso
    template_name = 'tipo_egresos/tipo_egreso_delete.html'
    success_url = reverse_lazy('tipo_egreso_list')

# -------------------------------------------Ingresos-------------------------------------------


class IngresoList(ListView, LoginRequiredMixin):
    model = Ingreso
    template_name = 'Ingreso/ingreso_list.html'


class IngresoDetail(DetailView, LoginRequiredMixin):
    model = Ingreso
    template_name = 'Ingreso/ingreso_detail.html'


class IngresoCreate(CreateView, LoginRequiredMixin):
    model = Ingreso
    fields = ['nombre', 'descripcion', 'monto', 'fecha']
    template_name = 'form.html'
    success_url = reverse_lazy('ingreso_list')


class IngresoUpdate(UpdateView, LoginRequiredMixin):
    model = Ingreso
    fields = ['nombre', 'descripcion', 'monto', 'fecha']
    template_name = 'form.html'
    success_url = reverse_lazy('ingreso_list')


class IngresoDelete(UserPassesTestMixin, DeleteView, LoginRequiredMixin):
    model = Ingreso
    template_name = 'Ingreso/ingreso_delete.html'
    success_url = reverse_lazy('ingreso_list')

# -------------------------------------------Egresos-------------------------------------------


class EgresoList(ListView, LoginRequiredMixin):
    model = Egreso
    template_name = 'Egreso/egreso_list.html'


class EgresoDetail(DetailView, LoginRequiredMixin):
    model = Egreso
    template_name = 'Egreso/egreso_detail.html'


class EgresoCreate(CreateView, LoginRequiredMixin):
    model = Egreso
    fields = ['tipo_egreso', 'nombre', 'descripcion', 'monto', 'fecha']
    template_name = 'form.html'
    success_url = reverse_lazy('egreso_list')


class EgresoUpdate(UpdateView, LoginRequiredMixin):
    model = Egreso
    fields = ['tipo_egreso', 'nombre', 'descripcion', 'monto', 'fecha']
    template_name = 'form.html'
    success_url = reverse_lazy('egreso_list')


class EgresoDelete(UserPassesTestMixin, DeleteView, LoginRequiredMixin):
    model = Egreso
    template_name = 'Egreso/egreso_delete.html'
    success_url = reverse_lazy('egreso_list')
