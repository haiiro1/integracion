from django.urls import path
from Ferremas_pri import views
urlpatterns = [
    path('', views.Inicio, name="Inicio"),
   
]