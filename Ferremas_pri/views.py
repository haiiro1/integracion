from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Producto
from .serializers import ProductoSerializer


def testeo(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def base(request):
    context = {}
    return render(request, 'ferremas_pri/base.html', context)

def inicio(request):
    context = {}
    return render(request, 'ferremas_pri/inicio.html', context)

class ProductoListCreate(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer