from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from autenticacion import views

urlpatterns = [
  
    path('crear/', views.SignUpView.as_view(), name='usuario_signup'),
    path('perfil/<pk>/', views.UsuarioProfile.as_view(), name='usuario_profile'),
    path('editar/<pk>/', views.UsuarioUpdate.as_view(), name='usuario_update'),
]
