from django.urls import path
from Ferremas_pri import views
urlpatterns = [ 
    path('', views.inicio, name='inicio'),
    path('testeo/', views.testeo, name='testeo'),
    #productos
    path('productos/', views.lista_productos, name='lista_productos'),
    path('api/productos/', views.ProductoListCreate.as_view(), name='producto-list-create'),
    path('api/productos/<int:pk>/', views.ProductoRetrieveUpdateDestroy.as_view(), name='producto-retrieve-update-destroy'),
    #carrito
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar/<int:item_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('limpiar/', views.limpiar_carrito, name='limpiar_carrito'),
    path('contenido/', views.obtener_contenido_carrito, name='obtener_contenido_carrito'),
    #api cambio de divisa
    path('get_dolar_price/', views.get_dolar_price, name='get_dolar_price'),
]