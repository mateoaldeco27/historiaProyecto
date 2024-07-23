from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.index, name='index'),

    path('ia/proyecto/<int:pk>', views.proyecto, name='proyecto'),
    path('ia/seccion/<int:pk>/', views.seccion, name='seccion'),
    
    path('historia/proyecto/<int:pk>', views.proyectoHistoria, name='proyectoHistoria'),
    path('historia/seccion/<int:pk>/', views.seccionHistoria, name='seccionHistoria'),
]
