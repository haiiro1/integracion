from django.contrib import admin

from .models import Producto, Categoria, Carrito,ItemCarrito

admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Carrito)
admin.site.register(ItemCarrito)
