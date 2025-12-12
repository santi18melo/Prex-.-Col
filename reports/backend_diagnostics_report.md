# Informe de Diagnóstico del Backend

Este informe resume los resultados de la ejecución del script `debug_utils.py`, que realiza una revisión completa de variables de entorno, conexión a la base de datos, detección de configuraciones duplicadas y la ejecución del comando interno de Django `check`.

---

## Resultado de la ejecución
```
Environment variable SECRET_KEY is not set
Environment variable DEBUG is not set
Environment variable DATABASE_URL is not set
Environment variable POSTGRES_DB is not set
Environment variable POSTGRES_USER is not set
Environment variable POSTGRES_PASSWORD is not set
Environment variable POSTGRES_HOST is not set
Environment variable POSTGRES_PORT is not set
Environment variable FRONTEND_URL is not set

Database connection: FAILED

Duplicate/contradictory settings detected:
 - SECURE_SSL_REDIRECT is defined in multiple sections; ensure the intended value is applied based on DEBUG flag.
 - SESSION_COOKIE_SECURE appears more than once; consolidate to a single definition.

Django system check raised an exception: CommandError: System check identified some issues:
    ERRORS:
    django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.
```

---

## Análisis y Recomendaciones

1. **Variables de entorno**
   - Definir todas las variables requeridas en un archivo `.env` en la raíz del proyecto (junto a `settings.py`).
   - Ejemplo de contenido mínimo:
     ```env
     SECRET_KEY=su_clave_secreta_aleatoria
     DEBUG=True
     DATABASE_URL=postgres://user:pass@localhost:5432/nombre_bd
     POSTGRES_DB=nombre_bd
     POSTGRES_USER=user
     POSTGRES_PASSWORD=pass
     POSTGRES_HOST=localhost
     POSTGRES_PORT=5432
     FRONTEND_URL=http://localhost:5175
     ```
   - Ejecutar `load_dotenv` ya está configurado en `settings.py`.

2. **Conexión a la base de datos**
   - Una vez definidas las variables anteriores, la conexión debería pasar a `OK`.
   - Verificar que el contenedor/servicio PostgreSQL esté activo y accesible.

3. **Configuraciones duplicadas**
   - `SECURE_SSL_REDIRECT` y `SESSION_COOKIE_SECURE` aparecen dos veces (líneas 32‑34 y 176‑180). Consolidar cada una en una única definición dentro del bloque de producción (`if not DEBUG:`).
   - Ejemplo:
     ```python
     if not DEBUG:
         SECURE_SSL_REDIRECT = True
         SESSION_COOKIE_SECURE = True
         CSRF_COOKIE_SECURE = True
         # ... resto de configuraciones de producción
     ```

4. **Error de `SECRET_KEY`**
   - Django requiere que `SECRET_KEY` tenga un valor; la ausencia provoca que el comando `check` falle.
   - Añadir la variable al `.env` y asegurarse de que `settings.py` la lea correctamente (línea 17).

5. **Impacto en URLs, conexiones y datos base**
   - Los cambios propuestos solo afectan a la configuración y a la carga de variables de entorno; no modifican rutas (`urls.py`) ni modelos.
   - Por lo tanto, no habrá ruptura de contribuciones existentes.

6. **Próximos pasos**
   - Crear/actualizar el archivo `.env` con los valores indicados.
   - Eliminar las definiciones duplicadas en `settings.py`.
   - Reiniciar el entorno virtual y volver a ejecutar:
     ```bash
     python manage.py check
     ```
   - Verificar que el comando devuelva `System check identified no issues`.

---

**Conclusión**: La falta de variables de entorno y la presencia de configuraciones duplicadas son la causa principal de los errores actuales. Aplicando las correcciones descritas, el backend debería iniciar sin problemas y permanecer estable para futuras contribuciones.
