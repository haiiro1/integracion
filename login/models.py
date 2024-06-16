# accounts/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.crypto import get_random_string

class CustomUser(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Hombre'),
        ('F', 'Mujer'),
        ('O', 'Otros'),
    ]

    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    rut = models.CharField(max_length=12, unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    role = models.CharField(max_length=10, choices=[
        ('ADMIN', 'Administrador'),
        ('SELLER', 'Vendedor'),
        ('WAREHOUSE', 'Bodeguero'),
        ('ACCOUNTANT', 'Contador'),
        ('CUSTOMER', 'Cliente'),
    ], default='CUSTOMER')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'rut', 'gender']

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = get_random_string(length=10)  # Generar un nombre de usuario aleatorio
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email


class MiModelo(models.Model):
    nombre = models.CharField(max_length=100)
    contraseña = models.IntegerField()
    # Define otros campos según tus necesidades

    
