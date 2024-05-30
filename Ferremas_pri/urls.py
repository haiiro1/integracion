from django.urls import path
from Ferremas_pri import views
urlpatterns = [ 
    path('', views.inicio, name='inicio'),
    path('testeo/', views.testeo, name='testeo'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('api/productos/', views.ProductoListCreate.as_view(), name='producto-list-create'),
    path('api/productos/<int:pk>/', views.ProductoRetrieveUpdateDestroy.as_view(), name='producto-retrieve-update-destroy'),
]