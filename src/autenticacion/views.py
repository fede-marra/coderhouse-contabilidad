from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import CreateView, UpdateView, DetailView

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin


class SignUpView(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'form.html'
    success_message = 'Usuario creado correctamente'


class UsuarioProfile(DetailView):
    model = User
    template_name = 'profile.html'


class UsuarioUpdate(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'form.html'
    fields = ['first_name', 'last_name', 'email']

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.request.user.pk})


class Login(LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy("index")


class Logout(LogoutView):
    template_name = 'logout.html'
