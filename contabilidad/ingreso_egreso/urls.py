from django.urls import path
from ingreso_egreso import views

urlpatterns = [
    path('', views.ingreso, name="ingreso"),
    path('ingresos/', views.ingreso, name="ingreso"),
    path('egresos/', views.egreso, name="egreso"),
    path('tiposEgresos/', views.tipoEgreso, name='tiposEgresos'),
    path('personas/', views.persona, name='personas'),
    path('mostrarPersonas/', views.mostrarPersonas, name='mostrarPersonas'),
    path('mostarEgresos/', views.mostrarTiposEgresos, name='mostrarEgresos'),
    path('busqueda/', views.busqueda, name='busqueda'),
]