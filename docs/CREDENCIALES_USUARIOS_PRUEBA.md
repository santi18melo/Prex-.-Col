# 🔐 CREDENCIALES DE USUARIOS DE PRUEBA - PREXCOL

## Usuarios Disponibles por Rol

Estos usuarios están creados para que puedas probar todos los dashboards y funcionalidades del sistema.

---

## 👨‍💼 ADMINISTRADOR

**Acceso completo al sistema**

```
Email: admin@example.com
Password: admin123
```

**Permisos:**
- ✅ Acceso total al sistema
- ✅ Gestionar usuarios
- ✅ Gestionar categorías
- ✅ Gestionar todos los productos
- ✅ Ver todos los pedidos
- ✅ Ver todas las facturas
- ✅ Configuración del sistema

**Dashboard:** `/dashboard-admin`

---

## 👤 CLIENTE

**Usuario comprador**

```
Email: cliente@example.com
Password: cliente123
```

**Permisos:**
- ✅ Ver catálogo de productos
- ✅ Crear pedidos
- ✅ Ver sus propios pedidos
- ✅ Ver sus propias facturas
- ❌ No puede crear productos

**Dashboard:** `/dashboard-cliente`

**Datos adicionales:**
- Nombre: Juan Cliente
- Dirección: Calle 123 #45-67, Bogotá
- Teléfono: +57 300 123 4567

---

## 🏭 PROVEEDOR

**Usuario vendedor**

```
Email: proveedor@example.com
Password: proveedor123
```

**Permisos:**
- ✅ Ver catálogo de productos
- ✅ Crear y editar sus productos
- ✅ Ver pedidos de sus productos
- ✅ Gestionar inventario
- ❌ No puede ver pedidos de otros

**Dashboard:** `/dashboard-proveedor`

**Datos adicionales:**
- Nombre: María Proveedora
- Dirección: Carrera 45 #12-34, Medellín
- Teléfono: +57 301 234 5678

---

## 🚚 LOGÍSTICA

**Usuario de entregas**

```
Email: logistica@example.com
Password: logistica123
```

**Permisos:**
- ✅ Ver todos los pedidos
- ✅ Actualizar estado de pedidos
- ✅ Gestionar entregas
- ❌ No puede crear productos

**Dashboard:** `/dashboard-logistica`

**Datos adicionales:**
- Nombre: Carlos Logística
- Dirección: Avenida 68 #23-45, Cali
- Teléfono: +57 302 345 6789

---

## 💼 VENDEDOR

**Usuario de ventas**

```
Email: vendedor@example.com
Password: vendedor123
```

**Permisos:**
- ✅ Ver catálogo de productos
- ✅ Crear pedidos para clientes
- ✅ Ver estadísticas de ventas
- ✅ Gestionar carrito de compras
- ❌ No puede modificar productos

**Dashboard:** `/dashboard-vendedor`

**Datos adicionales:**
- Nombre: Ana Vendedora
- Dirección: Diagonal 34 #56-78, Barranquilla
- Teléfono: +57 303 456 7890

---

## 🔄 Cómo Crear Estos Usuarios

Si necesitas recrear estos usuarios, ejecuta:

```bash
cd src/backend
python create_test_users.py
```

El script:
- ✅ Verifica si los usuarios ya existen
- ✅ Crea los usuarios faltantes
- ✅ Asigna los roles correctos
- ✅ Configura permisos apropiados
- ✅ Crea una tienda de ejemplo

---

## 📊 Resumen de Roles

| Rol | Email | Dashboard | Permisos Principales |
|-----|-------|-----------|---------------------|
| **Admin** | admin@example.com | `/dashboard-admin` | Acceso total |
| **Cliente** | cliente@example.com | `/dashboard-cliente` | Compras y pedidos |
| **Proveedor** | proveedor@example.com | `/dashboard-proveedor` | Gestión de productos |
| **Logística** | logistica@example.com | `/dashboard-logistica` | Gestión de entregas |
| **Vendedor** | vendedor@example.com | `/dashboard-vendedor` | Ventas |

---

## 🧪 Casos de Uso para Testing

### Probar como Admin
1. Login con `admin@example.com`
2. Accede a Dashboard Admin
3. Prueba crear categorías, productos, usuarios

### Probar como Cliente
1. Login con `cliente@example.com`
2. Navega por el catálogo
3. Agrega productos al carrito
4. Crea un pedido
5. Verifica que se generó la factura automáticamente

### Probar como Proveedor
1. Login con `proveedor@example.com`
2. Crea productos nuevos
3. Asigna categorías (obligatorio)
4. Gestiona inventario

### Probar como Logística
1. Login con `logistica@example.com`
2. Ve la lista de pedidos
3. Actualiza estados de entrega
4. Gestiona rutas

### Probar como Vendedor
1. Login con `vendedor@example.com`
2. Crea pedidos para clientes
3. Ve estadísticas de ventas
4. Gestiona carrito

---

## 🔒 Seguridad

**⚠️ IMPORTANTE:**

Estas credenciales son **SOLO PARA DESARROLLO Y PRUEBAS**.

**En producción:**
- ❌ NO uses estas contraseñas
- ✅ Cambia todas las contraseñas
- ✅ Usa contraseñas seguras (mínimo 12 caracteres)
- ✅ Habilita autenticación de dos factores
- ✅ Implementa políticas de contraseñas fuertes

---

## 📝 Notas

- Todos los usuarios tienen contraseñas simples para facilitar las pruebas
- Los usuarios se crean automáticamente al ejecutar el script
- Si un usuario ya existe, el script no lo duplica
- Puedes modificar los datos en `create_test_users.py`

---

**Última actualización:** Diciembre 2025  
**Versión:** 2.0
