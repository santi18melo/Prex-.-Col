from rest_framework import serializers
from .models import Factura

class FacturaSerializer(serializers.ModelSerializer):
    cliente_nombre = serializers.ReadOnlyField(source='cliente.nombre')
    pedido_id = serializers.ReadOnlyField(source='pedido.id')
    
    class Meta:
        model = Factura
        fields = [
            'id', 'numero_factura', 'pedido_id', 'cliente', 'cliente_nombre',
            'fecha_emision', 'subtotal', 'impuestos', 'total', 'archivo_pdf'
        ]
        read_only_fields = ['numero_factura', 'fecha_emision', 'archivo_pdf']
