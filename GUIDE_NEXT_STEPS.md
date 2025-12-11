# 🚀 PREXCOL: Sistema Finalizado y Optimizado

Este repositorio contiene la versión estable y autocurativa del sistema PREXCOL.

## 🛠️ Nuevas Características del Sistema de Arranque

Se ha reescrito completamente el sistema de inicio (`scripts\start_prexcol.bat`) para ser robusto a fallos y fácil de usar.

### Principales Mejoras:
1.  **Auto-Reparación (Self-Healing)**: 
    *   Si faltan dependencias, las instala.
    *   Si el entorno virtual se corrompe, lo destruye y lo recrea automáticamente.
    *   Si la base de datos no conecta, intenta arrancar el servicio PostgreSQL y reintenta.
2.  **Caché Inteligente**: 
    *   Ya no pierde tiempo instalando `pip` o `npm` si nada ha cambiado. El inicio es hasta 10x más rápido.
3.  **Interfaz Gráfica**:
    *   Barras de progreso visuales.
    *   Menú interactivo al final para ver usuarios de prueba o crear administradores.
4.  **Resiliencia**:
    *   Autodetecta errores de `Pillow`/imágenes y los corrige al vuelo.
    *   Compatible con Python 3.13/3.14 gracias a ajustes dinámicos de versiones.

## 🚦 Cómo Iniciar

Simplemente ejecuta:
```bash
.\scripts\start_prexcol.bat
```
(O usa el acceso directo si lo creaste).

## 👥 Usuarios de Prueba

Al finalizar la carga, el script te ofrecerá un menú donde podrás ver esta tabla:

| Rol | Correo | Contraseña |
|-----|--------|------------|
| **Super Admin** | `admin@prexcol.com` | `admin123` |
| **Store Manager** | `manager@store.com` | `manager123` |
| **Cliente** | `user@example.com` | `user123` |

## 📦 Gestión del Repositorio

Para subir este proyecto a un **NUEVO** repositorio remoto:

1. Crear un repositorio vacío en GitHub/GitLab.
2. Ejecutar en la terminal de este proyecto:

```bash
# Eliminar el remoto anterior (si existe)
git remote remove origin

# Agregar el nuevo remoto
git remote add origin <URL_DE_TU_NUEVO_REPO.git>

# Subir cambios
git add .
git commit -m "chore: major upgrade to startup system with self-healing capabilities"
git push -u origin main
```
