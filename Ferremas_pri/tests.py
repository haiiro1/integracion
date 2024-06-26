from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Producto

class ProductoTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.producto_data = {
            'codigo_producto': 'PRD001',
            'nombre': 'Producto de Prueba',
            'descripcion': 'Descripción del producto de prueba',
            'marca': 'Marca de prueba',
            'precio': '100.00',
            'stock': '10'
        }
        self.url = reverse('producto-list-create')
    
    def test_obtener_producto(self):
        producto = Producto.objects.create(**self.producto_data)
        url_detalle = reverse('producto-retrieve-update-destroy', kwargs={'pk': producto.id})
        response = self.client.get(url_detalle)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre'], 'Producto de Prueba')