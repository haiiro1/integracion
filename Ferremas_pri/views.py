from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from rest_framework import generics
from .models import Carrito, ItemCarrito, Producto
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

@login_required
def ver_carrito(request):
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    items = ItemCarrito.objects.filter(carrito=carrito)
    total = sum(item.producto.precio * item.cantidad for item in items)
    return render(request, 'Ferremas_pri/carrito.html', {'items': items, 'total': total})

@login_required
def agregar_al_carrito(request, producto_id):
    producto = Producto.objects.get(pk=producto_id)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    item, created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
    if not created:
        item.cantidad += 1
        item.save()
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        total_items = ItemCarrito.objects.filter(carrito=carrito).count()
        return JsonResponse({'total_items': total_items})
    
    return redirect('ver_carrito')

@login_required
def eliminar_del_carrito(request, item_id):
    item = ItemCarrito.objects.get(pk=item_id)
    item.delete()
    return redirect('ver_carrito')

@login_required
def limpiar_carrito(request):
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    ItemCarrito.objects.filter(carrito=carrito).delete()
    return redirect('ver_carrito')

@login_required
def obtener_contenido_carrito(request):
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    items = ItemCarrito.objects.filter(carrito=carrito)
    total = sum(item.producto.precio * item.cantidad for item in items)
    html = render_to_string('Ferremas_pri/partials/carrito_contenido.html', {'items': items, 'total': total})
    return JsonResponse({'html': html})

#                                                              Integrando la API de Transbank ~
def realizar_pago(request):
    # Recordar obtener los datos necesarios para realizar el pago en transbank pls ~
    commerce_id = "mi_commerce_id"
    commerce_payment_id = "mi_commerce_payment_id"
    processor_payment_id = "mi_processor_payment_id"
    service_id = "mi_service_id"
    client_id = "mi_client_id"

    # Llamar a la función para realizar el pago
    response = issue_payment(commerce_id, commerce_payment_id, processor_payment_id, service_id, client_id)
    
    # Procesar la respuesta y devolver una respuesta JSON
    return JsonResponse(response)
