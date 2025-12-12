from django.db import models
from apps.productos.models import Pedido, Producto  # Assuming Pedido exists in productos model for now
from apps.usuarios.models import Usuario

class Factura(models.Model):
    """
    Modelo de factura generada para un pedido.
    Se crea automáticamente cuando un pedido y sus detalles son confirmados.
    """
    pedido = models.OneToOneField(
        'productos.Pedido', 
        on_delete=models.CASCADE, 
        related_name='factura'
    )
    cliente = models.ForeignKey(
        Usuario, 
        on_delete=models.PROTECT,
        related_name='facturas'
    )
    fecha_emision = models.DateTimeField(auto_now_add=True)
    numero_factura = models.CharField(max_length=20, unique=True, editable=False)
    
    subtotal = models.DecimalField(max_digits=12, decimal_places=2)
    impuestos = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=12, decimal_places=2)
    
    archivo_pdf = models.FileField(upload_to='facturas/', blank=True, null=True)
    
    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"
        ordering = ['-fecha_emision']

    def __str__(self):
        return f"Factura {self.numero_factura} - {self.cliente.nombre}"

    def save(self, *args, **kwargs):
        if not self.numero_factura:
            import uuid
            self.numero_factura = f"FACT-{uuid.uuid4().hex[:8].upper()}"
        super().save(*args, **kwargs)

    def generar_pdf(self):
        """
        Lógica placeholder para generar PDF de factura.
        En una implementación real, usaría reportlab o similar.
        """
        # Aquí iría la lógica de generación real.
        pass
