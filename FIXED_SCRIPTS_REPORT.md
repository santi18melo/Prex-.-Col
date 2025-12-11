# Reporte de Corrección de Escenarios (.bat)

Se han analizado y corregido los archivos de inicio (scripts .bat) para asegurar que funcionen correctamente independientemente de desde dónde se ejecuten (directorio raíz o carpeta `scripts`) y que apunten a los puertos correctos.

## Resumen de Cambios

### 1. `scripts\start_prexcol.bat` (Script Principal)
- **Estado Anterior**: Usaba rutas relativas que fallaban si el script se ejecutaba desde la carpeta `scripts`.
- **Correcciones**:
  - Se actualizaron todas las rutas para usar `%~dp0..` (referencia absoluta al directorio padre del script).
  - Se aseguró que el puerto del frontend sea **5175** (coincidiendo con `vite.config.js`).
  - Se corrigió la ruta de activación del entorno virtual y localizadores de logs.

### 2. `scripts\start_prexcol_fixed.bat`
- **Estado Anterior**: 
  - Usaba el puerto **5173** (incorrecto, Vite usa 5175).
  - Usaba `%CD%` que dependía de la carpeta actual del usuario, causando errores de "ruta no encontrada".
- **Correcciones**:
  - Cambiado puerto a **5175**.
  - Implementado uso de `%~dp0` para rutas robustas.

### 3. `scripts\start_simple.bat`
- **Estado Anterior**: Rutas incorrectas como `cd backend` en lugar de `cd src\backend`.
- **Correcciones**:
  - Reescrito para usar la estructura correcta `src\backend` y `src\frontend`.
  - Rutas absolutas dinámicas para evitar errores de "The system cannot find the path specified".

### 4. `scripts\setup_project.bat`
- **Estado Anterior**: Intentaba acceder a `frontend` direcrtamente.
- **Correcciones**:
  - Apunta correctamente a `..\src\frontend`.

## Recomendación
Para iniciar el proyecto, puede usar cualquiera de los siguientes comandos desde la carpeta raíz o `scripts`:

- **Completo (con Celery):** `.\scripts\start_prexcol.bat`
- **Simple (solo Django + React):** `.\scripts\start_simple.bat`

El sistema ahora debería iniciar correctamente abriendo **http://localhost:5175/**.
