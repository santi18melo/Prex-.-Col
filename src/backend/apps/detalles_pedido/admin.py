from django.contrib import admin
from .models import Factura

@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('numero_factura', 'pedido', 'cliente', 'total', 'fecha_emision')
    search_fields = ('numero_factura', 'cliente__nombre', 'pedido__id')
    list_filter = ('fecha_emision',)
    readonly_fields = ('numero_factura', 'fecha_emision')
