from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from rest_framework import generics
from .models import Producto
from  .api import Mindicador
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from .serializers import ProductoSerializer
from django.http import JsonResponse
from django.template.loader import render_to_string
from .transbank_integration import issue_payment




def get_dolar_price(request):
    mindicador = Mindicador('dolar', 2024)
    dolar_price = mindicador.get_dolar_price()
    return JsonResponse({'dolar_price': dolar_price})

def testeo(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def base(request):
    context = {}
    return render(request, 'ferremas_pri/base.html', context)

def inicio(request):
    productos = Producto.objects.all()
    return render(request, 'ferremas_pri/inicio.html', {'productos': productos})

def pagar(request):
    return render(request, 'ferremas_pri/pagar.html')

#                                                                           Cosas de Productos ~
def lista_productos(request):
    context = {}
    return render(request, 'ferremas_pri/lista_productos.html',context)

class ProductoListCreate(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


#                                                                               Cosas Carrito ~



#                                                              Integrando la API de Transbank ~

