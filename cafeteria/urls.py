from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_inicio, name='menu_inicio'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('pedidos/', views.lista_pedidos, name='lista_pedidos'),
]
