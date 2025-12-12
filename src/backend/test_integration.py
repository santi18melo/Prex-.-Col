"""
Script de prueba para verificar las APIs de Categorías y Facturas
"""
import os
import sys
import django

# Setup Django
sys.path.insert(0, os.path.abspath('.'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from apps.categorias.models import Categoria
from apps.detalles_pedido.models import Factura
from apps.productos.models import Producto, Pedido, DetallePedido, Tienda
from apps.usuarios.models import Usuario

print("=" * 60)
print("PRUEBAS DE INTEGRACIÓN - CATEGORÍAS Y FACTURAS")
print("=" * 60)

# Test 1: Verificar Categorías
print("\n1. Verificando Categorías...")
categorias = Categoria.objects.all()
print(f"   ✓ Total de categorías: {categorias.count()}")
for cat in categorias[:5]:
    print(f"   - {cat.nombre} (Slug: {cat.slug}, Activa: {cat.activa})")

# Test 2: Verificar que todos los productos tienen categoría
print("\n2. Verificando Productos con Categoría...")
productos_sin_categoria = Producto.objects.filter(categoria__isnull=True).count()
total_productos = Producto.objects.count()
print(f"   ✓ Total de productos: {total_productos}")
print(f"   ✓ Productos sin categoría: {productos_sin_categoria}")
if productos_sin_categoria == 0:
    print("   ✅ TODOS los productos tienen categoría asignada")
else:
    print(f"   ⚠️  HAY {productos_sin_categoria} productos sin categoría")

# Test 3: Verificar Facturas
print("\n3. Verificando Facturas...")
facturas = Factura.objects.all()
print(f"   ✓ Total de facturas: {facturas.count()}")
for factura in facturas[:3]:
    print(f"   - Factura #{factura.numero_factura}: ${factura.total} (Cliente: {factura.cliente.nombre})")

# Test 4: Verificar relación Pedido-Factura
print("\n4. Verificando relación Pedido-Factura...")
pedidos_con_factura = Pedido.objects.filter(factura__isnull=False).count()
total_pedidos = Pedido.objects.count()
print(f"   ✓ Total de pedidos: {total_pedidos}")
print(f"   ✓ Pedidos con factura: {pedidos_con_factura}")
if pedidos_con_factura > 0:
    print("   ✅ Sistema de facturación automática funcionando")

# Test 5: Crear una categoría de prueba
print("\n5. Creando categoría de prueba...")
try:
    test_cat, created = Categoria.objects.get_or_create(
        nombre="Categoría Test",
        defaults={'descripcion': 'Categoría creada por script de prueba'}
    )
    if created:
        print(f"   ✅ Categoría creada: {test_cat.nombre} (Slug: {test_cat.slug})")
    else:
        print(f"   ℹ️  Categoría ya existía: {test_cat.nombre}")
except Exception as e:
    print(f"   ❌ Error: {e}")

print("\n" + "=" * 60)
print("RESUMEN DE PRUEBAS")
print("=" * 60)
print(f"✓ Categorías: {categorias.count()}")
print(f"✓ Productos: {total_productos}")
print(f"✓ Productos con categoría: {total_productos - productos_sin_categoria}")
print(f"✓ Facturas: {facturas.count()}")
print(f"✓ Pedidos con factura: {pedidos_con_factura}")
print("=" * 60)
