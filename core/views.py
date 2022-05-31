from urllib.request import Request
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria, Producto
from .forms import ProductoForms, CustomUserCreationForm
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets
from .serializers import ProductoSerializer

# Create your views here.
class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

def home(request):

    productos = Producto.objects.all()
    data = {
        'productos': productos
    }

    return render(request, 'core/home.html', data)

@permission_required('app.add_producto')
def add_product(request):

    data = {
        'form': ProductoForms()
    }

    if request.method == 'POST':
        formulario = ProductoForms(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto agregado correctamente")
        else:
            data["form"] = formulario

    return render(request, 'core/vendedor/agregar.html', data)

@permission_required('app.view_producto')
def list_product(request):

    productos = Producto.objects.all()
    data = {
        'productos': productos
    }


    return render(request, 'core/vendedor/listar.html', data)

@permission_required('app.change_producto')
def edit_product(request, id):

    producto = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductoForms(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForms(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto modificado correctamente")
            return redirect(to="list_product")
        data["form"] = formulario
            

    return render(request, 'core/vendedor/editar.html', data)

@permission_required('app.delete_producto')
def delete_product(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Producto eliminado correctamente")
    return redirect(to="list_product")

def detail_product(request, id):
    producto = get_object_or_404(Producto, id=id)
    data = {
        'productos': producto
    }

    return render(request,'core/detalle.html', data)

def products(request):
    queryset = request.GET.get("buscar")
    if queryset:
        productos = Producto.objects.filter(
            Q(nombre_producto__icontains = queryset) |
            Q(serie_producto__icontains = queryset) |
            Q(categoria__categoria__icontains = queryset) |
            Q(subcategoria__subcategoria__icontains = queryset) |
            Q(marca__marca__icontains = queryset) |
            Q(modelo__icontains = queryset)
        ).distinct()
    else:
        productos = Producto.objects.all()

    categorias = Categoria.objects.all()

    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 1)
        productos = paginator.page(page)
    except:
        raise Http404


    data = {
        'productos': productos,
        'categorias': categorias,
        'paginator': paginator
    }

    return render(request, 'core/productos.html', data)

def signup(request):

    data = {
        'form': CustomUserCreationForm
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Registrado con éxito")
            return redirect(to="home")
        data["form"] = formulario

    return render(request, 'registration/signup.html', data)

