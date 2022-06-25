from dataclasses import fields
from django import forms
from .models import Producto, Pedido
from django.contrib.auth.forms import UserCreationForm

class ProductoForms(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'

class PedidoForms(forms.ModelForm):

    class Meta:
        model = Pedido
        fields = ('despacho_domicilio', 'direccion_despacho', 'numero_direccion', 'forma_pago')

class CustomUserCreationForm(UserCreationForm):
    pass