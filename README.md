# 🚀 PREXCOL - Sistema de Gestión de Productos y Pedidos

[![Version](https://img.shields.io/badge/version-2.0-blue.svg)](https://github.com/santi18melo/Prex-.-Col)
[![Django](https://img.shields.io/badge/Django-5.0.4-green.svg)](https://www.djangoproject.com/)
[![React](https://img.shields.io/badge/React-18-blue.svg)](https://reactjs.org/)
[![License](https://img.shields.io/badge/license-MIT-orange.svg)](LICENSE)

## 📋 Descripción

PREXCOL es un sistema integral de gestión de productos, pedidos y facturación diseñado para facilitar las operaciones comerciales. El sistema incluye gestión de categorías, productos, pedidos, facturación automática y múltiples roles de usuario.

### ✨ Características Principales

- 🏷️ **Gestión de Categorías**: Sistema de categorías obligatorias para productos
- 📦 **Gestión de Productos**: CRUD completo con imágenes y control de inventario
- 🛒 **Sistema de Pedidos**: Creación y seguimiento de pedidos
- 📄 **Facturación Automática**: Generación automática de facturas al crear pedidos
- 👥 **Gestión de Usuarios**: Múltiples roles (Admin, Cliente, Proveedor, Logística)
- 🔐 **Autenticación JWT**: Sistema seguro de autenticación
- 📱 **Responsive Design**: Funciona en desktop, tablet y móvil
- 🆘 **Ayuda Integrada**: Botón de ayuda en todas las vistas

---

## 🚀 Inicio Rápido

### Requisitos Previos

- **Python** 3.10 o superior
- **Node.js** 16 o superior
- **PostgreSQL** 13 o superior (opcional, usa SQLite por defecto)
- **Git**

### Instalación Automática (Recomendado)

#### Windows

```bash
# 1. Clonar el repositorio
git clone https://github.com/santi18melo/Prex-.-Col.git
cd Prex-.-Col

# 2. Ejecutar script de inicio
cd scripts
.\start_prexcol.bat
```

El script automáticamente:
- ✅ Crea el entorno virtual de Python
- ✅ Instala dependencias del backend
- ✅ Instala dependencias del frontend
- ✅ Ejecuta migraciones de base de datos
- ✅ Inicia ambos servidores (backend y frontend)

### Instalación Manual

#### Backend (Django)

```bash
# 1. Crear entorno virtual
cd src/backend
python -m venv venv

# 2. Activar entorno virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar variables de entorno
copy .env.example .env
# Editar .env con tus configuraciones

# 5. Ejecutar migraciones
python manage.py migrate

# 6. Crear usuarios de prueba (recomendado)
python create_test_users.py

# 7. Iniciar servidor
python manage.py runserver
```

#### Frontend (React)

```bash
# 1. Navegar a frontend
cd src/frontend

# 2. Instalar dependencias
npm install

# 3. Iniciar servidor de desarrollo
npm run dev
```

---

## 🌐 Acceso al Sistema

Una vez iniciados ambos servidores:

- **Frontend**: http://localhost:5175
- **Backend API**: http://localhost:8000
- **Admin Panel**: http://localhost:8000/admin
- **Documentación**: http://localhost:8000/api/docs/

### Credenciales de Prueba

Usuarios disponibles para probar todos los dashboards:

```
👨‍💼 Admin (Acceso total):
Email: admin@example.com
Password: admin123
Dashboard: /dashboard-admin

👤 Cliente (Compras):
Email: cliente@example.com
Password: cliente123
Dashboard: /dashboard-cliente

🏭 Proveedor (Productos):
Email: proveedor@example.com
Password: proveedor123
Dashboard: /dashboard-proveedor

🚚 Logística (Entregas):
Email: logistica@example.com
Password: logistica123
Dashboard: /dashboard-logistica

💼 Vendedor (Ventas):
Email: vendedor@example.com
Password: vendedor123
Dashboard: /dashboard-vendedor
```

📋 **Ver detalles completos:** [CREDENCIALES_USUARIOS_PRUEBA.md](docs/CREDENCIALES_USUARIOS_PRUEBA.md)

---

## 📁 Estructura del Proyecto

```
PREXCOL/
├── src/
│   ├── backend/              # Django Backend
│   │   ├── apps/
│   │   │   ├── usuarios/     # Gestión de usuarios
│   │   │   ├── productos/    # Gestión de productos
│   │   │   ├── categorias/   # Gestión de categorías ✨ NUEVO
│   │   │   ├── detalles_pedido/ # Facturas ✨ NUEVO
│   │   │   ├── ventas/       # Gestión de ventas
│   │   │   ├── pagos/        # Gestión de pagos
│   │   │   └── notificaciones/ # Sistema de notificaciones
│   │   ├── backend/          # Configuración principal
│   │   ├── middleware/       # Middleware personalizado
│   │   ├── services/         # Servicios compartidos
│   │   └── manage.py
│   │
│   └── frontend/             # React Frontend
│       ├── src/
│       │   ├── components/   # Componentes reutilizables
│       │   ├── pages/        # Páginas principales
│       │   ├── context/      # Context API
│       │   ├── services/     # Servicios API
│       │   ├── routes/       # Configuración de rutas
│       │   └── styles/       # Estilos globales
│       └── package.json
│
├── docs/                     # Documentación completa
│   ├── MANUAL_USUARIO_COMPLETO.md  # Manual de usuario ✨ NUEVO
│   ├── INICIO_RAPIDO.md      # Guía de inicio rápido
│   ├── RESUMEN_AJUSTES_PRUEBAS.md  # Resumen de cambios ✨ NUEVO
│   └── _build/html/          # Documentación Sphinx
│
├── scripts/                  # Scripts de utilidad
│   ├── start_prexcol.bat     # Inicio automático (Windows)
│   └── verify_dependencies.bat
│
└── README.md                 # Este archivo
```

---

## 🔧 Tecnologías Utilizadas

### Backend
- **Django** 5.0.4 - Framework web
- **Django REST Framework** - API REST
- **Simple JWT** - Autenticación JWT
- **PostgreSQL** - Base de datos (producción)
- **SQLite** - Base de datos (desarrollo)
- **Celery** - Tareas asíncronas
- **Redis** - Cache y broker de Celery

### Frontend
- **React** 18 - Librería UI
- **React Router** - Navegación
- **Context API** - Gestión de estado
- **Axios** - Cliente HTTP
- **CSS Moderno** - Estilos con variables

---

## 📚 Documentación

### Para Usuarios
- 📖 [**Manual de Usuario Completo**](docs/MANUAL_USUARIO_COMPLETO.md) - Guía completa paso a paso
- 🚀 [**Inicio Rápido**](docs/INICIO_RAPIDO.md) - Instalación y configuración
- 📊 [**Guía de Pruebas**](docs/GUIA_PRUEBAS_COMPLETAS.md) - Testing del sistema

### Para Desarrolladores
- 🏗️ [**Arquitectura**](docs/arquitectura.rst) - Diseño del sistema
- 📐 [**Diagramas UML**](docs/diagramas/INDEX_DIAGRAMAS.md) - Diagramas del sistema
- 🔧 [**Scripts Disponibles**](docs/SCRIPTS_DISPONIBLES.md) - Comandos útiles
- 📦 [**Dependencias**](docs/DEPENDENCIAS.md) - Gestión de dependencias
- 🚢 [**Deployment**](docs/deployment.rst) - Guías de despliegue

### Documentación Técnica
- 📄 [**API Documentation**](http://localhost:8000/api/docs/) - Documentación interactiva
- 🗄️ [**Esquema de BD**](docs/ESQUEMA_BD_ACTUALIZADO.txt) - Estructura de base de datos
- ✅ [**Resumen de Ajustes**](docs/RESUMEN_AJUSTES_PRUEBAS.md) - Últimos cambios

---

## 🆕 Novedades en v2.0

### Categorías Obligatorias
- ✅ Todos los productos **DEBEN** tener una categoría asignada
- ✅ Slug automático generado desde el nombre
- ✅ Permisos: Admin para crear/editar, público para leer
- ✅ Navegación "Categories First" en el catálogo

### Facturación Automática
- ✅ Facturas generadas automáticamente al crear pedidos
- ✅ Número de factura único
- ✅ Generación de PDF asíncrona
- ✅ Permisos: Ver solo facturas propias (o todas si admin)

### Botón de Ayuda Global
- ✅ Botón flotante en **TODAS** las vistas
- ✅ Acceso rápido al manual de usuario
- ✅ Enlaces a documentación y soporte
- ✅ Atajos de teclado integrados

---

## 🧪 Testing

### Ejecutar Tests del Backend

```bash
cd src/backend

# Todos los tests
python manage.py test

# Tests específicos
python manage.py test apps.categorias
python manage.py test apps.detalles_pedido

# Con verbosidad
python manage.py test --verbosity=2

# Test de integración
python test_integration.py
```

### Resultados Esperados

```
✅ 6/6 tests pasados
✅ Categorías: Crear, listar, permisos
✅ Facturas: Generación automática, listado, permisos
✅ Productos: Categoría obligatoria
```

---

## 🚀 Despliegue

### Producción

Ver guías detalladas en:
- [Deployment a Render](docs/DEPLOY_RENDER.md)
- [Deployment a Netlify](docs/GUIA_DEPLOY_NETLIFY.md)

### Variables de Entorno

Configurar en `.env`:

```env
# Django
SECRET_KEY=tu-secret-key-aqui
DEBUG=False
ALLOWED_HOSTS=tu-dominio.com

# Base de Datos
DATABASE_URL=postgresql://user:password@host:5432/dbname

# Email
EMAIL_HOST_USER=tu-email@gmail.com
EMAIL_HOST_PASSWORD=tu-app-password

# Frontend
FRONTEND_URL=https://tu-frontend.netlify.app

# Celery
CELERY_BROKER_URL=redis://localhost:6379/0
```

---

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📞 Soporte

### Ayuda en la Aplicación
- 🆘 Click en el botón de ayuda flotante (esquina inferior derecha)
- 📖 Accede al manual de usuario completo
- ⌨️ Usa `F1` para abrir la ayuda rápida

### Contacto
- 📧 **Email**: soporte@prexcol.com
- 📞 **Teléfono**: +57 300 123 4567
- 🌐 **Documentación**: http://localhost:8000/api/docs/
- 💬 **Issues**: [GitHub Issues](https://github.com/santi18melo/Prex-.-Col/issues)

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

---

## 👥 Equipo

Desarrollado por el equipo PREXCOL

---

## 🙏 Agradecimientos

- Django Community
- React Community
- Todos los contribuidores del proyecto

---

## 📊 Estado del Proyecto

```
✅ Backend: Totalmente funcional
✅ Frontend: Componentes actualizados e integrados
✅ Documentación: Completa y accesible
✅ Tests: 100% pasando
✅ Integración: Categorías y Facturas completamente integradas
```

**Estado**: ✨ **LISTO PARA PRODUCCIÓN** ✨

---

**Última actualización**: Diciembre 2025  
**Versión**: 2.0  
**Mantenido por**: PREXCOL Team
