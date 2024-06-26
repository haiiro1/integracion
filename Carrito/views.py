# Carrito/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Carrito
from Ferremas_pri.models import Producto
from django.contrib.auth.decorators import login_required


@login_required
def mostrar_carrito(request):
    items_carrito = Carrito.objects.filter(user=request.user)
    cantidad_items = sum([item.cantidad for item in items_carrito])
    subtotal = sum(item.producto.precio * item.cantidad for item in items_carrito)
    total = subtotal + 2800  # Asumiendo que 2800 es una tarifa fija de envío
    context = {
        'items_carrito': items_carrito,
        'subtotal': subtotal,
        'total': total,
        'cantidad_items': cantidad_items
    }
    return render(request, '', context) 

@login_required
def añadir_al_carrito(request, prod_id):
    producto = get_object_or_404(Producto, id=prod_id)
    carrito, created = Carrito.objects.get_or_create(user=request.user, producto=producto)
    if not created:
        carrito.cantidad += 1
        carrito.save()
    return redirect('mostrar_carrito')

@login_required
def remover_del_carrito(request, carrito_id):
    carrito = get_object_or_404(Carrito, id=carrito_id)
    carrito.delete()
    return redirect('mostrar_carrito')

@login_required
def aumentar_cantidad(request, carrito_id):
    carrito = get_object_or_404(Carrito, id=carrito_id)
    carrito.cantidad += 1
    carrito.save()
    return redirect('mostrar_carrito')

@login_required
def disminuir_cantidad(request, carrito_id):
    carrito = get_object_or_404(Carrito, id=carrito_id)
    if carrito.cantidad > 1:
        carrito.cantidad -= 1
        carrito.save()
    return redirect('mostrar_carrito')

