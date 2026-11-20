# Proyecto Final - Restaurante Sabor Porteño (G06)

Este proyecto consiste en una API hexagonal construida con Django, Oracle y React para la gestión de mesas, platos y pedidos.

## Integrantes y Reparto de Entidades (Anexo A)
* **Vicente Sepúlveda:** Responsable de todas las entidades (`pedidos`, `detalle_pedido`, `mesas`, `categorias_plato`, `platos`) y la configuración total de la base de datos.
* **Benjamin Baeza:** Apoyo en creacion de tablas y organizacion.

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




## Avance Semana 2: Capas Hexagonales de Entidades Maestras

Se implementó la arquitectura hexagonal de adentro hacia afuera dentro de la aplicación `restaurante`, respetando estrictamente la **Regla de Dependencia** (el núcleo de negocio no depende de Django ni de Oracle):

* **Capa de Dominio (`restaurante/domain/`):**
  * **Entidades (`entities.py`):** Modelos puros en Python (`@dataclass`) para las 5 tablas del sistema (`Mesa`, `CategoriaPlato`, `Plato`, `Pedido` y `DetallePedido`).
  * **Puertos (`repositories.py`):** Interfaces abstractas (`ABC`) que definen los contratos de persistencia para las 5 entidades.
  * **Excepciones (`exceptions.py`):** Excepciones personalizadas de negocio (`EntidadNoEncontradaError`, `RegistroDuplicadoError`, `BorradoProtegidoError` y `ReglaNegocioInvalidaError`).
* **Capa de Aplicación (`restaurante/application/use_cases/`):**
  * Casos de uso CRUD completos para las 3 entidades maestras (**Mesas**, **Categorías de Plato** y **Platos**).
  * Validación de reglas de negocio, control de registros duplicados y **borrado protegido** (impide eliminar mesas con pedidos, categorías con platos o platos incluidos en detalles de pedido).
* **Capa de Infraestructura (`restaurante/infrastructure/`):**
  * **Modelos ORM (`models.py`):** Mapeo contra Oracle FreeSQL con `managed = False` y `CompositePrimaryKey` en `detalle_pedido`.
  * **Repositorios (`repositories.py`):** Implementaciones concretas (`DjangoMesaRepository`, `DjangoCategoriaPlatoRepository`, `DjangoPlatoRepository`) que traducen entre modelos ORM y entidades de dominio.