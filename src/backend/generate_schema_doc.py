"""
Script para generar diagrama actualizado de la base de datos
"""
import os
import sys
import django

sys.path.insert(0, os.path.abspath('.'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from django.apps import apps

print("=" * 80)
print("ESQUEMA DE BASE DE DATOS ACTUALIZADO - PREXCOL")
print("=" * 80)

for app_config in apps.get_app_configs():
    if app_config.name.startswith('apps.'):
        print(f"\n{'='*80}")
        print(f"APP: {app_config.verbose_name}")
        print(f"{'='*80}")
        
        for model in app_config.get_models():
            print(f"\n📋 Modelo: {model.__name__}")
            print("-" * 80)
            
            # Campos
            for field in model._meta.get_fields():
                field_type = field.__class__.__name__
                
                # Información adicional
                info = []
                if hasattr(field, 'null') and field.null:
                    info.append("NULL")
                if hasattr(field, 'blank') and field.blank:
                    info.append("BLANK")
                if hasattr(field, 'unique') and field.unique:
                    info.append("UNIQUE")
                if hasattr(field, 'primary_key') and field.primary_key:
                    info.append("PK")
                if field_type == 'ForeignKey':
                    info.append(f"→ {field.related_model.__name__}")
                if field_type == 'ManyToManyField':
                    info.append(f"⇄ {field.related_model.__name__}")
                
                info_str = f" [{', '.join(info)}]" if info else ""
                print(f"  • {field.name}: {field_type}{info_str}")

print("\n" + "=" * 80)
print("RELACIONES PRINCIPALES")
print("=" * 80)

print("""
Usuario (1) ──────→ (N) Pedido
Usuario (1) ──────→ (N) Factura
Usuario (1) ──────→ (1) Tienda (administrador)

Categoria (1) ────→ (N) Producto [OBLIGATORIO]
Tienda (1) ───────→ (N) Producto
Usuario (1) ──────→ (N) Producto (proveedor)

Pedido (1) ───────→ (N) DetallePedido
Producto (1) ─────→ (N) DetallePedido
Pedido (1) ───────→ (1) Factura [AUTO-GENERADA]

Producto (N) ─────⇄ (N) Seccion
""")

print("=" * 80)
print("CAMBIOS RECIENTES")
print("=" * 80)
print("""
✅ Producto.categoria: Ahora es OBLIGATORIO (on_delete=PROTECT)
✅ Factura: Generación automática al crear Pedido (signal)
✅ Categoria.slug: Generación automática desde nombre
✅ Permisos: IsAdminOrReadOnly para Categorías
✅ Permisos: IsOwnerOrAdmin para Facturas
""")

print("=" * 80)
