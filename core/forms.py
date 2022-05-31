from dataclasses import fields
from django import forms
from .models import Producto
from django.contrib.auth.forms import UserCreationForm

class ProductoForms(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    pass