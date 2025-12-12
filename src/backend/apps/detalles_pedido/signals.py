from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.productos.models import Pedido
from .models import Factura

@receiver(post_save, sender=Pedido)
def crear_factura_al_confirmar_pedido(sender, instance, created, **kwargs):
    """
    Crea una factura automáticamente cuando un pedido se marca como 'entregado'
    o cuando se crea si así se desea (dependiendo de la regla de negocio).
    Aquí asumiremos que se crea al estar 'entregado' o 'pendiente' si el pago está confirmado.
    Para simplificar y cumplir con 'al crear o ver pedidos', la crearemos cuando el pedido tenga total > 0.
    """
    if instance.total > 0 and not hasattr(instance, 'factura'):
        # Solo crear si no existe ya
        Factura.objects.create(
            pedido=instance,
            cliente=instance.cliente,
            subtotal=instance.total, # Simplificación: subtotal = total
            impuestos=0,
            total=instance.total
        )
