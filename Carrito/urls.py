from django.urls import path
from . import views
#Carrito
urlpatterns = [
    path('', views.mostrar_carrito, name='mostrar_carrito'),
    path('agregar/<int:prod_id>/', views.añadir_al_carrito, name='añadir_al_carrito'),
    path('remover/<int:carrito_id>/', views.remover_del_carrito, name='remover_del_carrito'),
    path('aumentar/<int:carrito_id>/', views.aumentar_cantidad, name='aumentar_cantidad'),
    path('disminuir/<int:carrito_id>/', views.disminuir_cantidad, name='disminuir_cantidad'),
]