entidad: mesas 
columna     tipo                    nulo        restricción                 descripcion
numero      NUMBER GENERATED        NO          PK                          identificador y numero unico de la mesa .
            BY DEFAULT AS 
            IDENTITY (NOCACHE)
capacidad   NUMBER                  NO          ninguna                     cantidad maxima de comensales 
activa      NUMBER(1)               NO          CHECK (activa IN (0,1))     1 si la mesa está operativa, 0 si está inactiva.


entidad: categorias_plato 
columna         tipo                    nulo        restricción               descripcion
id_categoria    NUMBER GENERATED        NO          PK                        indicador unico de la categoria.
                BY DEFAULT AS 
                IDENTITY (NOCACHE)
nombre          VARCHAR2(100)           NO          UNIQUE                    Nombre de la categoría (ej. Entradas, Fondos).


entidad: platos
columna         tipo                    nulo        restricción                 descripcion
codigo          VARCHAR2(20)            NO          PK                          Código alfanumérico único del plato.
nombre          VARCHAR2                NO          ninguna                     Nombre del plato.
id_categoria    NUMBER                  NO          FK a categorias_plato       Categoría a la que pertenece el plato.
precio          NUMBER(10,2)            NO          CHECK (precio >= 0)         Valor del plato.
disponiBLE      NUMBER(1)               NO          CHECK (disponible IN (0,1)) 1 si hay stock, 0 si está agotado.

entidad: pedidos (Entidad Principal) 
columna         tipo                        nulo        restricción                 descripcion
id_pedido       NUMBER GENERATED            NO          PK                          Identificador único del pedido. 
                BY DEFAULT AS 
                IDENTITY (NOCACHE)
numero_mesa     NUMBER                      NO          FK a mesas                  Mesa a la que se le asigna el pedido.
garzon          VARCHAR2(100)               NO          ninguna                     Nombre del garzón que atiende la mesa.
fecha           TIMESTAMP WITH TIME ZONE    NO          ninguna                     Fecha y hora exacta de creación del pedido.
propina         NUMBER(10,2)                NO          CHECK (propina >= 0)        Monto de propina asociada al pedido.
total           NUMBER(10,2)                NO          CHECK (total >= 0)          Sumatoria total de los platos + propina.
estado          VARCHAR2(20)                NO          CHECK (abierto, en_cocina,  Estado de avance del pedido.
                                                        servido, pagado, anulado)

entidad: detalle_pedido 
columna             tipo                    nulo        restricción                     descripcion
id_pedido           NUMBER                  NO          PK / FK a pedidos               Pedido al que pertenece el detalle. 
codigo_plato        VARCHAR2(20)            NO          PK / FK a platos                Plato solicitado.
cantidad            NUMBER                  NO          CHECK (cantidad > 0)            Cantidad de porciones solicitadas.
precio_unitario     NUMBER(10,2)            No          CHECK (precio_unitario >= 0)    Precio histórico del plato al momento de pedir.
observacion         VARCHAR2(255)           SI          Ninguna                         Notas para la cocina (ej. "Sin cebolla").