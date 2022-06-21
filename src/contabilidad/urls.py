from django.urls import path
from contabilidad import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),

    path('tipo_egreso_list', views.Tipo_egresoList.as_view(),
         name="tipo_egreso_list"),
    path('tipo_egresos/<int:pk>/', views.Tipo_egresoDetail.as_view(),
         name="tipo_egreso_detail"),
    path('tipo_egresos/new/', views.Tipo_egresoCreate.as_view(),
         name="tipo_egreso_new"),
    path('tipo_egresos/<int:pk>/edit/',
         views.Tipo_egresoUpdate.as_view(), name="tipo_egreso_edit"),
    path('tipo_egresos/<int:pk>/delete/',
         views.Tipo_egresoDelete.as_view(), name="tipo_egreso_delete"),

    path('ingreso_list', views.IngresoList.as_view(), name="ingreso_list"),
    path('ingreso/<int:pk>/', views.IngresoDetail.as_view(), name="ingreso_detail"),
    path('ingreso/new/', views.IngresoCreate.as_view(), name="ingreso_new"),
    path('ingreso/<int:pk>/edit/',
         views.IngresoUpdate.as_view(), name="ingreso_edit"),
    path('ingreso/<int:pk>/delete/',
         views.IngresoDelete.as_view(), name="ingreso_delete"),

    path('egreso_list', views.EgresoList.as_view(), name="egreso_list"),
    path('egreso/<int:pk>/', views.EgresoDetail.as_view(), name="egreso_detail"),
    path('egreso/new/', views.EgresoCreate.as_view(), name="egreso_new"),
    path('egreso/<int:pk>/edit/', views.EgresoUpdate.as_view(), name="egreso_edit"),
    path('egreso/<int:pk>/delete/',
         views.EgresoDelete.as_view(), name="egreso_delete"),

]
