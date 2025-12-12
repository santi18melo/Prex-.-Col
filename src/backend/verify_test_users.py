"""
Script para verificar usuarios de prueba en la base de datos
"""
import os
import sys
import django

sys.path.insert(0, os.path.abspath('.'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from apps.usuarios.models import Usuario

print("=" * 80)
print("VERIFICACIÓN DE USUARIOS EN LA BASE DE DATOS")
print("=" * 80)

# Lista de usuarios esperados
usuarios_esperados = [
    'admin@example.com',
    'cliente@example.com',
    'proveedor@example.com',
    'logistica@example.com',
    'vendedor@example.com'
]

print("\n📋 Verificando usuarios...")
print("-" * 80)

for email in usuarios_esperados:
    try:
        user = Usuario.objects.get(email=email)
        print(f"✅ {email}")
        print(f"   Nombre: {user.nombre}")
        print(f"   Rol: {user.rol}")
        print(f"   Activo: {user.is_active}")
        print(f"   Staff: {user.is_staff}")
        print()
    except Usuario.DoesNotExist:
        print(f"❌ {email} - NO EXISTE")
        print()

print("=" * 80)
print("RESUMEN")
print("=" * 80)

total = Usuario.objects.count()
print(f"\n📊 Total de usuarios en BD: {total}")

for rol in ['admin', 'cliente', 'proveedor', 'logistica', 'vendedor']:
    count = Usuario.objects.filter(rol=rol).count()
    print(f"   - {rol.capitalize()}: {count}")

print("\n" + "=" * 80)
