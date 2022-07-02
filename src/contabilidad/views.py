

from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render
from contabilidad.models import Ingreso, Egreso, Tipo_egreso, Tipo_ingreso
# from ingreso_egreso.forms import *
from django.contrib import messages

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView


from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# -------------------------------------------Base-------------------------------------------


class HomePageView(TemplateView):
    template_name = 'home.html'


class IndexList(LoginRequiredMixin, ListView):
    model = Ingreso
    template_name = 'index.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['ingresos'] = Ingreso.objects.all()
        context['egresos'] = Egreso.objects.all()
        return context


# -------------------------------------------Tipo Egresos-------------------------------------------


class Tipo_egresoList(ListView, LoginRequiredMixin):
    model = Tipo_egreso
    template_name = 'Tipo_egreso/tipo_egreso_list.html'


class Tipo_egresoDetail(DetailView, LoginRequiredMixin):
    model = Tipo_egreso
    template_name = 'Tipo_egreso/tipo_egreso_detail.html'


class Tipo_egresoCreate(CreateView, LoginRequiredMixin):
    model = Tipo_egreso
    fields = ['nombre']
    template_name = 'form.html'
    success_url = reverse_lazy('index')


class Tipo_egresoUpdate(UpdateView, LoginRequiredMixin):
    model = Tipo_egreso
    fields = ['nombre']
    template_name = 'form.html'
    success_url = reverse_lazy('index')


class Tipo_egresoDelete(DeleteView, LoginRequiredMixin):
    model = Tipo_egreso
    template_name = 'Tipo_egreso/tipo_egreso_delete.html'
    success_url = reverse_lazy('index')

# -------------------------------------------Tipo Ingreso-------------------------------------------


class Tipo_ingresoList(ListView, LoginRequiredMixin):
    model = Tipo_ingreso
    template_name = 'Tipo_ingreso/tipo_ingreso_list.html'


class Tipo_ingresoDetail(DetailView, LoginRequiredMixin):
    model = Tipo_ingreso
    template_name = 'Tipo_ingreso/tipo_ingreso_detail.html'


class Tipo_ingresoCreate(CreateView, LoginRequiredMixin):
    model = Tipo_ingreso
    fields = ['nombre']
    template_name = 'form.html'
    success_url = reverse_lazy('index')


class Tipo_ingresoUpdate(UpdateView, LoginRequiredMixin):
    model = Tipo_ingreso
    fields = ['nombre']
    template_name = 'form.html'
    success_url = reverse_lazy('index')


class Tipo_ingresoDelete(DeleteView, LoginRequiredMixin):
    model = Tipo_ingreso
    template_name = 'Tipo_ingreso/tipo_ingreso_delete.html'
    success_url = reverse_lazy('index')


# -------------------------------------------Ingreso-------------------------------------------


class HomeList(ListView, LoginRequiredMixin):
    model = Ingreso
    template_name = 'home.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['ingreso_list'] = Ingreso.objects.all()
        context['egreso_list'] = Egreso.objects.all()
        return context


class IngresoDetail(DetailView, LoginRequiredMixin):
    model = Ingreso
    template_name = 'Ingreso/ingreso_detail.html'


class IngresoCreate(CreateView, LoginRequiredMixin):
    model = Ingreso
    fields = ['tipo_ingreso', 'nombre', 'descripcion', 'monto', 'fecha']
    template_name = 'form.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


class IngresoUpdate(UpdateView, LoginRequiredMixin):
    model = Ingreso
    fields = ['tipo_ingreso', 'nombre', 'descripcion', 'monto', 'fecha']
    template_name = 'form.html'
    success_url = reverse_lazy('index')


class IngresoDelete(DeleteView, LoginRequiredMixin):
    model = Ingreso
    template_name = 'Ingreso/ingreso_delete.html'
    success_url = reverse_lazy('index')

# -------------------------------------------Egresos-------------------------------------------


class EgresoList(ListView, LoginRequiredMixin):
    model = Egreso
    template_name = 'home.html'


class EgresoDetail(DetailView, LoginRequiredMixin):
    model = Egreso
    template_name = 'Egreso/egreso_detail.html'


class EgresoCreate(CreateView, LoginRequiredMixin):
    model = Egreso
    fields = ['tipo_egreso', 'nombre', 'descripcion', 'monto', 'fecha']
    template_name = 'form.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


class EgresoUpdate(UpdateView, LoginRequiredMixin):
    model = Egreso
    fields = ['tipo_egreso', 'nombre', 'descripcion', 'monto', 'fecha']
    template_name = 'form.html'
    success_url = reverse_lazy('index')


class EgresoDelete(DeleteView, LoginRequiredMixin):
    model = Egreso
    template_name = 'Egreso/egreso_delete.html'
    success_url = reverse_lazy('index')
