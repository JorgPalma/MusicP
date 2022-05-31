from ast import Sub
from django.contrib import admin
from .models import Marca, Producto, Pedido, Categoria, Sucursal, Venta, Contacto, Subcategoria

# Register your models here.

admin.site.register(Marca)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(Categoria)
admin.site.register(Sucursal)
admin.site.register(Venta)
admin.site.register(Contacto)
admin.site.register(Subcategoria)