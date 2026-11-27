# Bitácora del Proyecto — Restaurante "Sabor Porteño"

* **Grupo:** G06
* **Integrantes:** Vicente Alfonso Sepúlveda Quintanilla, Benjamín
* **Sede:** INACAP Sede Renca
* **Stack:** Django 5.2 LTS + Oracle Database 26ai (FreeSQL) + SQLite

---

## Semana 1: Configuración Base y Modelo Relacional
* **Vicente Sepúlveda:**
  * Inicialización del proyecto Django y configuración dual de bases de datos (`default` en SQLite y `negocio` en Oracle FreeSQL).
  * Creación de `NegocioRouter` para aislar las consultas y bloquear migraciones sobre Oracle.
  * Creación del esquema DDL (`01_crear_tablas.sql`) con las 5 tablas (`mesas`, `categorias_plato`, `platos`, `pedidos`, `detalle_pedido`).
* **Benjamín:**
  * Elaboración del Modelo Entidad-Relación (notación Chen) y revisión de reglas de integridad y restricciones `CHECK`.

---

## Semana 2: Capas Hexagonales de Entidades Maestras
* **Vicente Sepúlveda:**
  * Implementación de entidades puras y puertos separados por archivo para `Mesa`, `Pedido` y `DetallePedido`.
  * Implementación de modelos `managed = False` y repositorios concretos separados por tabla contra Oracle FreeSQL.
  * Creación de excepciones propias del restaurante en `restaurante/application/exceptions.py`.
* **Benjamín:**
  * Implementación de entidades puras, puertos, modelos y repositorios separados por archivo para `CategoriaPlato` y `Plato`.
  * Validación de duplicados y borrado protegido en casos de uso de entidades maestras.

---

## Correcciones e Incidentes Resueltos
* **Rotación de credenciales (Commit `56db7c1`):** Se detectó exposición de `.env` en el historial temprano; se limpió el historial de Git, se renovó la sesión/clave en Oracle FreeSQL y se aseguró la exclusión en `.gitignore`.
* **Refactorización por tabla:** Se dividieron entidades, puertos, modelos y repositorios en archivos individuales por tabla dentro de sus respectivas carpetas.
* **Higiene de repositorio y localización:** Se eliminaron archivos compilados `.pyc` y `.vscode` del rastreo de Git, y se configuró `LANGUAGE_CODE = 'es-cl'` y `TIME_ZONE = 'America/Santiago'` en `settings.py`.
## Semana 3: Casos de Uso Transaccionales, API REST CRUD y Seguridad (HttpOnly + CSRF)

### Arquitectura y Seguridad Implementada
- **Transacciones atómicas multi-base:** Implementación de repositorios concretos y casos de uso para `pedidos` y `detalle_pedido` utilizando explícitamente `transaction.atomic(using="negocio")` para asegurar integridad sobre Oracle Database y evitar abrir transacciones en SQLite (`default`).
- **Inyección de dependencias (`infrastructure/di.py`):** Centralización de funciones factory para desacoplar las vistas HTTP de las implementaciones concretas del ORM.
- **Capa de Adaptadores (`restaurante/adaptadores/`):** Desarrollo de API REST con Django REST Framework empleando serializadores desacoplados (`serializers.Serializer`) sobre entidades puras del dominio y traducción centralizada de excepciones de negocio a códigos HTTP (`400`, `404`, `409`).
- **Autenticación y Control de Acceso:** Implementación de inicio de sesión JWT almacenado en cookie `HttpOnly` con validación CSRF (`CookieJWTAuthentication`) sobre SQLite (`default`), junto con permisos por grupos (`Administrador` y `Garzon`).

### Distribución de Trabajo del Equipo
- **Vicente Sepúlveda:** Excepciones de aplicación, repositorios y casos de uso transaccionales (`pedidos` y `detalle_pedido`), contenedor `di.py`, autenticación `HttpOnly` + CSRF, permisos por rol, manejo global de errores HTTP (`http_errors.py`), CRUD de `mesas` y `pedidos`, e integración de rutas en `adaptadores/urls.py`.
- **Benjamín:** Serializadores y vistas CRUD completas de `categorias_plato`, `platos` y `detalle_pedido` (subidos mediante GitHub Desktop).