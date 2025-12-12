from celery import shared_task
from django.core.files.base import ContentFile
import time
from .models import Factura

@shared_task
def generate_invoice_pdf_task(factura_id):
    """
    Tarea simulada para generación de PDF de factura.
    """
    try:
        factura = Factura.objects.get(id=factura_id)
        # Simulate processing time
        time.sleep(2)
        
        # Create dummy PDF content (text file for simplicity in this demo)
        content = f"Factura {factura.numero_factura}\nCliente: {factura.cliente.nombre}\nTotal: {factura.total}"
        
        file_name = f"factura_{factura.numero_factura}.txt"
        factura.archivo_pdf.save(file_name, ContentFile(content))
        factura.save()
        return f"Factura generated for ID {factura_id}"
    except Factura.DoesNotExist:
        return f"Factura ID {factura_id} not found"
