# Carrito/models.py
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from Ferremas_pri.models import Producto

class Carrito(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Carrito de {self.user.username}"

