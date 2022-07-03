from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from autenticacion import views

urlpatterns = [

    path('crear/', views.SignUpView.as_view(), name='signup'),
    path('perfil/<pk>/', views.UsuarioProfile.as_view(), name='profile'),
    path('editar/<pk>/', views.UsuarioUpdate.as_view(), name='update'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('avatar/<pk>/editar/',
         views.AvatarUpdate.as_view(), name='update_avatar'),
    path('avatar/<pk>/crear/', views.AvatarCreate.as_view(), name='create_avatar'),
    path("avatar/", views.agregarAvatar, name="agregar_avatar"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
