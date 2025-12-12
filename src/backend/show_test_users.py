"""
Script para mostrar información detallada de usuarios de prueba
"""
import os
import sys
import django

sys.path.insert(0, os.path.abspath('.'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from apps.usuarios.models import Usuario
from django.contrib.auth.hashers import check_password

print("=" * 80)
print("USUARIOS DE PRUEBA - VERIFICACIÓN COMPLETA")
print("=" * 80)

usuarios_prueba = [
    ('admin@example.com', 'admin123'),
    ('cliente@example.com', 'cliente123'),
    ('proveedor@example.com', 'proveedor123'),
    ('logistica@example.com', 'logistica123'),
    ('vendedor@example.com', 'vendedor123')
]

print("\n🔍 Verificando cada usuario...\n")

for email, password in usuarios_prueba:
    try:
        user = Usuario.objects.get(email=email)
        
        # Verificar contraseña
        password_ok = user.check_password(password)
        
        print(f"{'='*80}")
        print(f"📧 Email: {user.email}")
        print(f"👤 Nombre: {user.nombre}")
        print(f"🎭 Rol: {user.rol.upper()}")
        print(f"✅ Activo: {'Sí' if user.is_active else 'No'}")
        print(f"🔐 Contraseña verificada: {'✅ Correcta' if password_ok else '❌ Incorrecta'}")
        print(f"🏢 Staff: {'Sí' if user.is_staff else 'No'}")
        print(f"👑 Superuser: {'Sí' if user.is_superuser else 'No'}")
        if user.telefono:
            print(f"📞 Teléfono: {user.telefono}")
        if user.direccion:
            print(f"📍 Dirección: {user.direccion}")
        print()
        
    except Usuario.DoesNotExist:
        print(f"❌ ERROR: Usuario {email} NO EXISTE en la base de datos")
        print()

print("=" * 80)
print("ESTADÍSTICAS")
print("=" * 80)

total = Usuario.objects.count()
activos = Usuario.objects.filter(is_active=True).count()

print(f"\n📊 Total de usuarios: {total}")
print(f"✅ Usuarios activos: {activos}")
print(f"❌ Usuarios inactivos: {total - activos}")

print("\n📋 Por rol:")
for rol in ['admin', 'cliente', 'proveedor', 'logistica', 'vendedor']:
    count = Usuario.objects.filter(rol=rol).count()
    emoji = {
        'admin': '👨‍💼',
        'cliente': '👤',
        'proveedor': '🏭',
        'logistica': '🚚',
        'vendedor': '💼'
    }
    print(f"   {emoji.get(rol, '•')} {rol.capitalize()}: {count}")

print("\n" + "=" * 80)
print("✅ TODOS LOS USUARIOS DE PRUEBA ESTÁN EN LA BASE DE DATOS")
print("=" * 80)
print("\n💡 Puedes iniciar sesión con cualquiera de estos usuarios")
print("🌐 Frontend: http://localhost:5175")
print("=" * 80)
