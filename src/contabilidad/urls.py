from django.urls import path
from contabilidad import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('index/', views.IndexList.as_view(), name='index'),


    path('ingreso/<int:pk>/', views.IngresoDetail.as_view(), name="ingreso_detail"),
    path('ingreso/new/', views.IngresoCreate.as_view(), name="ingreso_new"),
    path('ingreso/<int:pk>/edit/',
         views.IngresoUpdate.as_view(), name="ingreso_edit"),
    path('ingreso/<int:pk>/delete/',
         views.IngresoDelete.as_view(), name="ingreso_delete"),

    path('egreso/<int:pk>/', views.EgresoDetail.as_view(), name="egreso_detail"),
    path('egreso/new/', views.EgresoCreate.as_view(), name="egreso_new"),
    path('egreso/<int:pk>/edit/', views.EgresoUpdate.as_view(), name="egreso_edit"),
    path('egreso/<int:pk>/delete/',
         views.EgresoDelete.as_view(), name="egreso_delete"),

    path('tipo_egreso/list/', views.Tipo_egresoList.as_view(),
         name="tipo_egreso_list"),
    path('tipo_egreso/<int:pk>/', views.Tipo_egresoDetail.as_view(),
         name="tipo_egreso_detail"),
    path('tipo_egreso/new/', views.Tipo_egresoCreate.as_view(),
         name="tipo_egreso_new"),
    path('tipo_egreso/<int:pk>/edit/',
         views.Tipo_egresoUpdate.as_view(), name="tipo_egreso_edit"),
    path('tipo_egreso/<int:pk>/delete/',
         views.Tipo_egresoDelete.as_view(), name="tipo_egreso_delete"),

    path('tipo_ingreso/list/', views.Tipo_ingresoList.as_view(),
         name="tipo_ingreso_list"),
    path('tipo_ingreso/<int:pk>/', views.Tipo_ingresoDetail.as_view(),
         name="tipo_ingreso_detail"),
    path('tipo_ingreso/new/', views.Tipo_ingresoCreate.as_view(),
         name="tipo_ingreso_new"),
    path('tipo_ingreso/<int:pk>/edit/',
         views.Tipo_ingresoUpdate.as_view(), name="tipo_ingreso_edit"),
    path('tipo_ingreso/<int:pk>/delete/',
         views.Tipo_ingresoDelete.as_view(), name="tipo_ingreso_delete"),

]
