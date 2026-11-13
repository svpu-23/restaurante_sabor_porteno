# Proyecto Final - Restaurante Sabor Porteño (G06)

Este proyecto consiste en una API hexagonal construida con Django, Oracle y React para la gestión de mesas, platos y pedidos.

## Integrantes y Reparto de Entidades (Anexo A)
* **Vicente Sepúlveda:** Responsable de todas las entidades (`pedidos`, `detalle_pedido`, `mesas`, `categorias_plato`, `platos`) y la configuración total de la base de datos.
* **[Nombre de tu compañero]:** Apoyo general.

## Avance Semana 1
* Diseño del Modelo Entidad-Relación y el Diccionario de Datos (ubicados en `docs/`).
* Ejecución de los scripts SQL nativos de Oracle (`01_crear_tablas.sql` y `02_datos_ejemplo.sql`) en FreeSQL.
* Creación del proyecto Django aislando la aplicación limpia.
* Configuración del entorno virtual protegiendo las credenciales con `.env`.
* Implementación del Router de base de datos (`routers.py`) para separar las tablas internas en SQLite de las del negocio en Oracle.
* Comprobación exitosa de la conexión a la base de datos Oracle 26ai.

## Instrucciones de Instalación

1. Clonar el repositorio y entrar a la carpeta:
   ```cmd
   git clone <URL_DE_TU_REPOSITORIO>
   cd restaurante_sabor_porteno

Crear y activar el entorno virtual:
python -m venv entorno
.\entorno\Scripts\activate

Instalar las dependencias:
pip install -r requirements.txt

Configurar las credenciales:
Copiar el archivo .env.example como .env y rellenar los datos del esquema FreeSQL (usando el puerto 1521).

comprobar conexion base de datos:
python manage.py check --database negocio