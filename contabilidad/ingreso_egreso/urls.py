from django.urls import path
from ingreso_egreso import views

urlpatterns = [
    # path('', views.busqueda, name="busqueda"),
    path('', views.PersonaList.as_view(), name="persona_list"),
    path('persona/<int:pk>/', views.PersonaDetail.as_view(), name="persona_detail"),
    path('persona/new/', views.PersonaCreate.as_view(), name="persona_new"),
    path('persona/<int:pk>/edit/', views.PersonaUpdate.as_view(), name="persona_edit"),
    path('persona/<int:pk>/delete/', views.PersonaDelete.as_view(), name="persona_delete"),
    # path('ingresos/', views.ingreso, name="ingreso"),
    # path('egresos/', views.egreso, name="egreso"),
    # path('tiposEgresos/', views.tipoEgreso, name='tiposEgresos'),
    # path('personas/', views.persona, name='personas'),
    # path('mostrarPersonas/', views.mostrarPersonas, name='mostrarPersonas'),
    # path('mostarEgresos/', views.mostrarTiposEgresos, name='mostrarEgresos'),
    # path('busqueda/', views.busqueda, name='busqueda'),
]
