from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


#                           Productos~

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    codigo_producto = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50, blank=True, null=True)
    categorias = models.ManyToManyField(Categoria, related_name='productos')  # Relación con categorías
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.codigo_producto}"


#                           Carrito~

class Carrito(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through='ItemCarrito')
    def __str__(self):
        return f"Carrito de {self.usuario.username}"

class ItemCarrito(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
