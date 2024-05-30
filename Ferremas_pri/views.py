from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from .models import Producto, ItemCarrito
from .serializers import ProductoSerializer

def base(request):
    context = {}
    return render(request, 'ferremas_pri/base.html', context)

def inicio(request):
    context = {}
    return render(request, 'ferremas_pri/inicio.html', context)

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'ferremas_pri/lista_productos.html', {'productos': productos})

class ProductoListCreate(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

@login_required
def ver_carrito(request):
    items = ItemCarrito.objects.filter(user=request.user)
    total = sum(item.producto.precio * item.cantidad for item in items)
    return render(request, 'Ferremas_pri/carrito.html', {'items': items, 'total': total})

@login_required
def ver_carrito_parcial(request):
    items = ItemCarrito.objects.filter(user=request.user)
    total = sum(item.producto.precio * item.cantidad for item in items)
    return render(request, 'Ferremas_pri/carrito_parcial.html', {'items': items, 'total': total})

@login_required
def agregar_al_carrito(request, producto_id):
    producto = Producto.objects.get(pk=producto_id)
    item, created = ItemCarrito.objects.get_or_create(user=request.user, producto=producto)
    if not created:
        item.cantidad += 1
        item.save()
    return redirect('ver_carrito')

@login_required
def eliminar_del_carrito(request, item_id):
    item = ItemCarrito.objects.get(pk=item_id)
    item.delete()
    return redirect('ver_carrito')

@login_required
def limpiar_carrito(request):
    ItemCarrito.objects.filter(user=request.user).delete()
    return redirect('ver_carrito')
