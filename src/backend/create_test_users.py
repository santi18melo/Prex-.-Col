"""
Script para crear usuarios de prueba de todos los roles
"""
import os
import sys
import django

sys.path.insert(0, os.path.abspath('.'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from apps.usuarios.models import Usuario
from apps.productos.models import Tienda

print("=" * 80)
print("CREANDO USUARIOS DE PRUEBA PARA TODOS LOS ROLES")
print("=" * 80)

# Datos de usuarios por rol
usuarios_data = [
    {
        'email': 'admin@example.com',
        'password': 'admin123',
        'nombre': 'Administrador Principal',
        'rol': 'admin',
        'is_staff': True,
        'is_superuser': True
    },
    {
        'email': 'cliente@example.com',
        'password': 'cliente123',
        'nombre': 'Juan Cliente',
        'rol': 'cliente',
        'direccion': 'Calle 123 #45-67, Bogotá',
        'telefono': '+57 300 123 4567'
    },
    {
        'email': 'proveedor@example.com',
        'password': 'proveedor123',
        'nombre': 'María Proveedora',
        'rol': 'proveedor',
        'direccion': 'Carrera 45 #12-34, Medellín',
        'telefono': '+57 301 234 5678'
    },
    {
        'email': 'logistica@example.com',
        'password': 'logistica123',
        'nombre': 'Carlos Logística',
        'rol': 'logistica',
        'direccion': 'Avenida 68 #23-45, Cali',
        'telefono': '+57 302 345 6789'
    },
    {
        'email': 'vendedor@example.com',
        'password': 'vendedor123',
        'nombre': 'Ana Vendedora',
        'rol': 'vendedor',
        'direccion': 'Diagonal 34 #56-78, Barranquilla',
        'telefono': '+57 303 456 7890'
    }
]

print("\n📝 Creando usuarios...")
print("-" * 80)

for user_data in usuarios_data:
    email = user_data['email']
    
    # Verificar si el usuario ya existe
    if Usuario.objects.filter(email=email).exists():
        user = Usuario.objects.get(email=email)
        print(f"ℹ️  Usuario ya existe: {user.nombre} ({user.email}) - Rol: {user.rol}")
    else:
        # Crear nuevo usuario
        password = user_data.pop('password')
        user = Usuario.objects.create_user(**user_data)
        user.set_password(password)
        user.save()
        print(f"✅ Usuario creado: {user.nombre} ({user.email}) - Rol: {user.rol}")

print("\n" + "=" * 80)
print("CREDENCIALES DE ACCESO")
print("=" * 80)

print("""
🔐 ADMIN (Acceso total al sistema)
   Email: admin@example.com
   Password: admin123
   Dashboard: /dashboard-admin
   
👤 CLIENTE (Compras y pedidos)
   Email: cliente@example.com
   Password: cliente123
   Dashboard: /dashboard-cliente
   
🏭 PROVEEDOR (Gestión de productos)
   Email: proveedor@example.com
   Password: proveedor123
   Dashboard: /dashboard-proveedor
   
🚚 LOGÍSTICA (Gestión de entregas)
   Email: logistica@example.com
   Password: logistica123
   Dashboard: /dashboard-logistica
   
💼 VENDEDOR (Ventas)
   Email: vendedor@example.com
   Password: vendedor123
   Dashboard: /dashboard-vendedor
""")

print("=" * 80)
print("RESUMEN")
print("=" * 80)

total_usuarios = Usuario.objects.count()
print(f"\n✅ Total de usuarios en el sistema: {total_usuarios}")

for rol in ['admin', 'cliente', 'proveedor', 'logistica', 'vendedor']:
    count = Usuario.objects.filter(rol=rol).count()
    print(f"   - {rol.capitalize()}: {count}")

print("\n" + "=" * 80)
print("✨ Usuarios de prueba listos para usar")
print("=" * 80)

# Crear tienda de ejemplo si no existe (para proveedores)
print("\n📦 Verificando tiendas...")
if not Tienda.objects.exists():
    admin_user = Usuario.objects.filter(rol='admin').first()
    if admin_user:
        tienda = Tienda.objects.create(
            nombre='Tienda Principal',
            direccion='Calle Principal #123',
            administrador=admin_user
        )
        print(f"✅ Tienda creada: {tienda.nombre}")
else:
    print(f"ℹ️  Ya existen {Tienda.objects.count()} tienda(s) en el sistema")

print("\n✅ ¡Listo! Puedes iniciar sesión con cualquiera de estos usuarios.")
