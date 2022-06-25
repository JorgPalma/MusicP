from django.urls import path, include
from .views import home, add_product, list_product, edit_product,\
     delete_product, detail_product, products, signup, ProductoViewset, cart, add_cart, less_cart,\
     clean_cart, delete_cart, buy
from rest_framework import routers

router = routers.DefaultRouter()
router.register('producto', ProductoViewset)

urlpatterns = [
    path('', home, name="home"),
    path('agregar/', add_product, name="add_product"),
    path('listar', list_product, name="list_product"),
    path('editar/<id>/', edit_product, name="edit_product"),
    path('borrar/<id>/', delete_product, name="delete_product"),
    path('detalle/<id>/', detail_product, name="detail_product"),
    path('productos/', products, name="products"),
    path('signup/', signup, name="signup"),
    path('api/', include(router.urls)),
    path('cart/', cart, name="cart"),
    path('add_cart/<int:id>/', add_cart, name="add_cart"),
    path('less_cart/<int:id>/', less_cart, name="less_cart"),
    path('delete_cart/<int:id>', delete_cart, name="delete_cart"),
    path('clean_cart/', clean_cart, name="clean_cart"),
    path('comprar/', buy, name="buy")
]