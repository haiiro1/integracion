from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Producto
import unittest
from unittest.mock import patch, MagicMock
from .api import Mindicador

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

class TestMindicador(unittest.TestCase):

    @patch('requests.get')
    def test_get_dolar_price_success(self, mock_get):
        # Configurar el mock de requests.get para simular una respuesta exitosa
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = '{"serie":[{"valor":800}]}'
        mock_get.return_value = mock_response

        # Instanciar Mindicador y llamar get_dolar_price
        mindicador = Mindicador('dolar', 2024)
        dolar_price = mindicador.get_dolar_price()

        # Verificar que el precio del dólar obtenido sea correcto
        self.assertEqual(dolar_price, 800)

    @patch('requests.get')
    def test_get_dolar_price_failure(self, mock_get):
        # Configurar el mock de requests.get para simular una respuesta fallida
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        # Instanciar Mindicador y llamar get_dolar_price
        mindicador = Mindicador('dolar', 2024)
        dolar_price = mindicador.get_dolar_price()

        # Verificar que el precio del dólar sea None cuando la solicitud falla
        self.assertIsNone(dolar_price)

if __name__ == '__main__':
    unittest.main()