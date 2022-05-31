from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Marca(models.Model):
    marca = models.CharField(default='NombreMarca', max_length=20)

    def __str__(self):
        return self.marca
class Categoria(models.Model):
    categoria = models.CharField(default='NombreCategoria', max_length=25)

    def __str__(self):
        return self.categoria

class Subcategoria(models.Model):
    subcategoria = models.CharField(default="NombreSubcategoria", max_length=25)

    def __str__(self):
        return self.subcategoria

class Producto(models.Model):
    serie_producto = models.CharField(max_length=10)
    nombre_producto = models.CharField(max_length=30)
    descripcion = models.TextField()
    codigo = models.CharField(max_length=10)
    modelo = models.CharField(max_length=20)
    valor = models.IntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.PROTECT, blank=True)
    imagen = models.ImageField(upload_to="productos", null=True)
    valor_oferta = models.IntegerField(blank=True, null=True)
    oferta = models.BooleanField()
    nuevo = models.BooleanField()

    def __str__(self):
        return self.nombre_producto


class Pedido(models.Model):
    num_pedido = models.IntegerField()
    despacho_domicilio = models.BooleanField()
    forma_pago = models.BooleanField()
    pedido_aceptado = models.BooleanField()
    direccion_despacho = models.CharField(max_length=70)
    numero_direccion = models.IntegerField()
    cliente = models.ForeignKey(User, on_delete=models.PROTECT, related_name='nombreCliente')    
    producto = models.ManyToManyField(Producto)
    bodeguero = models.ForeignKey(User, on_delete=models.PROTECT, related_name='nombreBodeguero')
    contador = models.ForeignKey(User, on_delete=models.PROTECT, related_name='nombreContador')    
    vendedor = models.ForeignKey(User, on_delete=models.PROTECT, related_name='nombreVendedor')    

    def __str__(self):
        return self.num_pedido

class Contacto(models.Model):
    nombre = models.CharField(max_length=25)
    email = models.CharField(max_length=35)
    consulta = models.TextField()

    def __str__(self):
        return self.nombre

class Sucursal(models.Model):
    nombre_sucursal = models.CharField(max_length=25)
    direccion = models.CharField(max_length=70)
    numero = models.IntegerField()

    def __str__(self):
        return self.nombre_sucursal

class Venta(models.Model):
    valor = models.IntegerField()
    fecha = models.DateTimeField(default=timezone.now)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.PROTECT, related_name='sucursalVenta')
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT, related_name='pedidoVenta')
    vendedor = models.ForeignKey(User, on_delete=models.PROTECT, related_name='vendedorVenta')
    cliente = models.ForeignKey(User, on_delete=models.PROTECT, related_name='clienteVenta')

    def __str__(self):
        return self.cliente