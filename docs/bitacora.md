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