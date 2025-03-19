from django.shortcuts import render
from .models import Producto, Pedido

def menu_inicio(request):
    return render(request, 'cafeteria/menu_inicio.html')

def lista_productos(request):
    productos = Producto.objects.filter(disponible=True)
    return render(request, 'cafeteria/lista_productos.html', {'productos': productos})

def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'cafeteria/lista_pedidos.html', {'pedidos': pedidos})

