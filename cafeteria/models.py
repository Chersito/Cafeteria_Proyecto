from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('preparado', 'Preparado'),
        ('entregado', 'Entregado')
    ]
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    estado = models.CharField(max_length=10, choices=ESTADOS, default='pendiente')
    fecha_pedido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido {self.id} - {self.usuario.username}"

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"
