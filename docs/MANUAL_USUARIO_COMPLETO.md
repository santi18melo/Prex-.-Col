# 📖 MANUAL DE USUARIO - PREXCOL

## Sistema de Gestión de Productos y Pedidos

---

## 📑 Tabla de Contenidos

1. [Introducción](#introducción)
2. [Acceso al Sistema](#acceso-al-sistema)
3. [Roles de Usuario](#roles-de-usuario)
4. [Navegación General](#navegación-general)
5. [Módulo de Productos](#módulo-de-productos)
6. [Módulo de Categorías](#módulo-de-categorías)
7. [Módulo de Pedidos](#módulo-de-pedidos)
8. [Módulo de Facturas](#módulo-de-facturas)
9. [Panel Administrativo](#panel-administrativo)
10. [Preguntas Frecuentes](#preguntas-frecuentes)

---

## 1. Introducción

### ¿Qué es PREXCOL?

PREXCOL es un sistema integral de gestión de productos y pedidos diseñado para facilitar:
- 📦 Gestión de productos y catálogos
- 🏷️ Organización por categorías
- 🛒 Creación y seguimiento de pedidos
- 📄 Generación automática de facturas
- 👥 Gestión de usuarios y permisos

### Características Principales

✅ **Interfaz Intuitiva**: Diseño moderno y fácil de usar  
✅ **Categorías Obligatorias**: Todos los productos deben tener una categoría  
✅ **Facturación Automática**: Las facturas se generan al crear un pedido  
✅ **Roles y Permisos**: Control de acceso basado en roles  
✅ **Responsive**: Funciona en desktop, tablet y móvil  

---

## 2. Acceso al Sistema

### 2.1 Página de Inicio

**URL**: `http://localhost:5175`

Al acceder al sistema, verás la página de inicio con:
- Botón **"Iniciar Sesión"** (esquina superior derecha)
- Botón **"Registrarse"**
- Información sobre el sistema

### 2.2 Iniciar Sesión

1. Click en **"Iniciar Sesión"**
2. Ingresa tu **correo electrónico**
3. Ingresa tu **contraseña**
4. Click en **"Ingresar"**

**Credenciales de Prueba**:
```
Admin:
Email: admin@example.com
Password: admin123

Cliente:
Email: cliente@example.com
Password: cliente123

Proveedor:
Email: proveedor@example.com
Password: proveedor123
```

### 2.3 Registro de Nuevo Usuario

1. Click en **"Registrarse"**
2. Completa el formulario:
   - Nombre completo
   - Correo electrónico
   - Contraseña (mínimo 8 caracteres)
   - Confirmar contraseña
   - Seleccionar rol (Cliente/Proveedor)
3. Click en **"Registrarse"**
4. Serás redirigido al dashboard

---

## 3. Roles de Usuario

### 👤 Cliente
**Permisos**:
- ✅ Ver catálogo de productos
- ✅ Crear pedidos
- ✅ Ver sus propios pedidos
- ✅ Ver sus propias facturas
- ❌ No puede crear productos

### 🏭 Proveedor
**Permisos**:
- ✅ Ver catálogo de productos
- ✅ Crear y editar sus productos
- ✅ Ver pedidos de sus productos
- ✅ Gestionar inventario
- ❌ No puede ver pedidos de otros

### 👨‍💼 Admin
**Permisos**:
- ✅ Acceso total al sistema
- ✅ Gestionar usuarios
- ✅ Gestionar categorías
- ✅ Gestionar todos los productos
- ✅ Ver todos los pedidos
- ✅ Ver todas las facturas
- ✅ Configuración del sistema

### 🚚 Logística
**Permisos**:
- ✅ Ver todos los pedidos
- ✅ Actualizar estado de pedidos
- ✅ Gestionar entregas
- ❌ No puede crear productos

---

## 4. Navegación General

### 4.1 Barra de Navegación

La barra superior contiene:
- **Logo PREXCOL**: Click para volver al inicio
- **Catálogo**: Ver productos disponibles
- **Mis Pedidos**: Ver tus pedidos (clientes)
- **Dashboard**: Panel de control (según rol)
- **Ayuda** 🆘: Acceso a este manual
- **Perfil**: Configuración de cuenta
- **Cerrar Sesión**: Salir del sistema

### 4.2 Botón de Ayuda 🆘

En **TODAS** las vistas del sistema encontrarás un botón de ayuda flotante:
- **Ubicación**: Esquina inferior derecha
- **Función**: Abre este manual de usuario
- **Acceso rápido**: Siempre disponible

---

## 5. Módulo de Productos

### 5.1 Ver Catálogo

**Ruta**: Dashboard → Catálogo

#### Vista por Categorías (Predeterminada)

1. Al entrar al catálogo, verás un **grid de categorías**
2. Cada categoría muestra:
   - 🖼️ Imagen representativa
   - 📝 Nombre de la categoría
   - 📄 Descripción breve
3. **Click en una categoría** para ver sus productos

#### Vista de Productos

1. Después de seleccionar una categoría:
   - Verás solo productos de esa categoría
   - Botón **"← Volver a Categorías"** en la parte superior
   - Filtros disponibles:
     - 🔍 Búsqueda por nombre
     - 🏷️ Sección
     - 💰 Rango de precio
     - 📊 Ordenar por precio

### 5.2 Detalles de Producto

Cada producto muestra:
- 🖼️ **Imagen** del producto
- 📝 **Nombre** y descripción
- 💰 **Precio**
- 📦 **Stock** disponible
- 🏪 **Tienda** que lo vende
- 🏷️ **Categoría**
- 🛒 Botón **"Agregar al carrito"**

### 5.3 Crear Producto (Proveedor/Admin)

**Ruta**: Dashboard Admin → Productos → + Nuevo Producto

1. Click en **"+ Nuevo Producto"**
2. Completa el formulario:
   - **Nombre** (obligatorio)
   - **Descripción**
   - **Precio** (obligatorio)
   - **Stock** (obligatorio)
   - **Tienda** (seleccionar de lista)
   - **Categoría** (obligatorio) ⚠️
   - **Proveedor** (opcional)
   - ☑️ **Es Producto Básico** (checkbox)
3. Click en **"Crear Producto"**

⚠️ **IMPORTANTE**: Desde la última actualización, **todos los productos DEBEN tener una categoría asignada**.

### 5.4 Editar Producto

1. En la lista de productos, click en **✏️ Editar**
2. Modifica los campos necesarios
3. Click en **"Actualizar"**

### 5.5 Eliminar Producto

1. Click en **🗑️ Eliminar**
2. Confirma la acción
3. El producto será eliminado

---

## 6. Módulo de Categorías

### 6.1 Ver Categorías (Admin)

**Ruta**: Dashboard Admin → Categorías

La tabla muestra:
- **ID**: Identificador único
- **Imagen**: Vista previa
- **Nombre**: Nombre de la categoría
- **Descripción**: Descripción breve
- **Estado**: Activa/Inactiva
- **Acciones**: Editar/Eliminar

### 6.2 Crear Categoría (Admin)

1. Click en **"+ Nueva Categoría"**
2. Completa el formulario:
   - **Nombre** (obligatorio)
   - **Descripción**
   - **Imagen** (URL o subir archivo)
   - **Slug** (se genera automáticamente)
   - ☑️ **Activa** (checkbox)
3. Click en **"Crear"**

💡 **Tip**: El slug se genera automáticamente desde el nombre. Por ejemplo:
- Nombre: "Productos de Limpieza"
- Slug: "productos-de-limpieza"

### 6.3 Editar Categoría

1. Click en **✏️** en la fila de la categoría
2. Modifica los campos
3. Click en **"Guardar"**

### 6.4 Desactivar Categoría

⚠️ **No puedes eliminar** una categoría si tiene productos asignados.

Opciones:
1. **Reasignar productos** a otra categoría
2. **Desactivar** la categoría (marca como inactiva)

---

## 7. Módulo de Pedidos

### 7.1 Crear Pedido (Cliente)

**Ruta**: Catálogo → Agregar productos al carrito

1. Navega por el catálogo
2. Click en **"Agregar al carrito"** en productos deseados
3. Revisa tu carrito (icono 🛒 en la barra superior)
4. Click en **"Realizar Pedido"**
5. Completa información:
   - Método de pago
   - Dirección de entrega
   - Notas adicionales
6. Click en **"Confirmar Pedido"**

### 7.2 Ver Mis Pedidos

**Ruta**: Dashboard → Mis Pedidos

Verás una lista con:
- **#ID**: Número de pedido
- **Fecha**: Cuándo se creó
- **Total**: Monto total
- **Estado**: Pendiente/En proceso/Completado/Cancelado
- **Acciones**: Ver detalles

### 7.3 Detalles de Pedido

Click en un pedido para ver:
- 📋 **Productos** incluidos
- 💰 **Subtotales** por producto
- 🚚 **Estado** actual
- 📄 **Factura** asociada (si existe)
- 📍 **Dirección** de entrega

### 7.4 Seguimiento de Pedido

Estados posibles:
1. 🟡 **Pendiente**: Pedido creado, esperando confirmación
2. 🔵 **En Proceso**: Pedido confirmado, en preparación
3. 🟢 **Completado**: Pedido entregado
4. 🔴 **Cancelado**: Pedido cancelado

---

## 8. Módulo de Facturas

### 8.1 Generación Automática

✨ **Las facturas se generan AUTOMÁTICAMENTE** al crear un pedido.

No necesitas hacer nada, el sistema:
1. Crea el pedido
2. Genera la factura
3. Asigna un número único
4. La vincula al pedido

### 8.2 Ver Mis Facturas

**Ruta**: Dashboard → Facturas

Lista de facturas con:
- **#Factura**: Número único
- **Fecha**: Fecha de emisión
- **Pedido**: Pedido asociado
- **Total**: Monto total
- **Estado**: Pagada/Pendiente
- **Acciones**: Ver/Descargar

### 8.3 Descargar Factura PDF

1. En la lista de facturas, click en **📄 Descargar PDF**
2. Si el PDF no está generado:
   - Verás mensaje: "Generando PDF..."
   - Espera unos segundos
   - Intenta de nuevo
3. El PDF se descargará automáticamente

### 8.4 Detalles de Factura

Click en una factura para ver:
- 📋 **Datos del cliente**
- 🏪 **Datos de la tienda**
- 📦 **Productos** facturados
- 💰 **Subtotal**, **IVA**, **Total**
- 📅 **Fecha de emisión**

---

## 9. Panel Administrativo

### 9.1 Acceso

**Ruta**: Dashboard Admin (solo para usuarios con rol Admin)

### 9.2 Tabs Disponibles

#### 📊 Dashboard
- Resumen general del sistema
- Estadísticas clave
- Gráficos de ventas

#### 👥 Usuarios
- Listar todos los usuarios
- Crear nuevo usuario
- Editar permisos
- Desactivar usuarios

#### 📦 Productos
- Gestión completa de productos
- Asignación de categorías
- Control de inventario

#### 🏪 Tiendas
- Gestión de tiendas
- Asignar administradores
- Configuración de tiendas

#### 🏷️ Categorías
- CRUD completo de categorías
- Activar/Desactivar
- Gestión de imágenes

#### 📋 Pedidos
- Ver todos los pedidos
- Actualizar estados
- Gestión de entregas

### 9.3 Funciones Administrativas

#### Crear Usuario
1. Tab **Usuarios** → **+ Nuevo Usuario**
2. Completa:
   - Nombre, Email, Contraseña
   - Rol (Cliente/Proveedor/Admin/Logística)
   - Permisos especiales
3. **Guardar**

#### Gestionar Inventario
1. Tab **Productos**
2. Editar producto
3. Actualizar campo **Stock**
4. **Guardar**

#### Cambiar Estado de Pedido
1. Tab **Pedidos**
2. Click en pedido
3. Seleccionar nuevo estado
4. **Actualizar**

---

## 10. Preguntas Frecuentes

### ❓ ¿Cómo recupero mi contraseña?

1. En la página de login, click en **"¿Olvidaste tu contraseña?"**
2. Ingresa tu correo electrónico
3. Recibirás un email con instrucciones
4. Sigue el enlace para restablecer

### ❓ ¿Por qué no puedo crear un producto sin categoría?

Desde la última actualización, **todos los productos DEBEN tener una categoría**. Esto ayuda a:
- Mejor organización
- Búsqueda más eficiente
- Navegación por categorías

Si no existe la categoría que necesitas, contacta a un administrador.

### ❓ ¿Cómo sé si mi pedido fue procesado?

1. Recibirás un **email de confirmación**
2. La **factura se genera automáticamente**
3. Puedes ver el estado en **"Mis Pedidos"**

### ❓ ¿Puedo cancelar un pedido?

Sí, pero solo si está en estado **"Pendiente"**:
1. Ve a **Mis Pedidos**
2. Click en el pedido
3. **Cancelar Pedido**

Si ya está "En Proceso", contacta a soporte.

### ❓ ¿Dónde encuentro mi factura?

Las facturas se generan automáticamente:
1. **Dashboard** → **Facturas**
2. O en los detalles del pedido

### ❓ ¿Cómo actualizo mi perfil?

1. Click en tu **nombre** (esquina superior derecha)
2. **Mi Perfil**
3. Edita la información
4. **Guardar cambios**

### ❓ ¿El sistema funciona en móvil?

Sí, PREXCOL es **totalmente responsive** y funciona en:
- 💻 Desktop
- 📱 Móviles
- 📱 Tablets

### ❓ ¿Cómo contacto a soporte?

- 📧 Email: soporte@prexcol.com
- 📞 Teléfono: +57 300 123 4567
- 💬 Chat en vivo (botón en esquina inferior derecha)

---

## 🎯 Atajos de Teclado

| Atajo | Acción |
|-------|--------|
| `Ctrl + K` | Búsqueda rápida |
| `Ctrl + H` | Abrir ayuda |
| `Ctrl + P` | Ver perfil |
| `Esc` | Cerrar modal |
| `F1` | Este manual |

---

## 📞 Soporte Técnico

### Horarios de Atención
- Lunes a Viernes: 8:00 AM - 6:00 PM
- Sábados: 9:00 AM - 1:00 PM

### Canales de Contacto
- 📧 **Email**: soporte@prexcol.com
- 📞 **Teléfono**: +57 300 123 4567
- 💬 **Chat**: Disponible en la plataforma
- 🌐 **Documentación**: http://localhost:8000/api/docs/

---

## 📝 Notas de Versión

### Versión 2.0 (Diciembre 2025)
✅ **Categorías obligatorias** para productos  
✅ **Facturación automática** al crear pedidos  
✅ **Navegación por categorías** mejorada  
✅ **Botón de ayuda** en todas las vistas  
✅ **Manual de usuario** integrado  

### Versión 1.0 (Noviembre 2025)
- Lanzamiento inicial del sistema

---

**© 2025 PREXCOL - Todos los derechos reservados**

*Este manual se actualiza constantemente. Última actualización: Diciembre 2025*
