-- Datos para mesas
INSERT INTO mesas (capacidad, activa) VALUES (2, 1);
INSERT INTO mesas (capacidad, activa) VALUES (4, 1);
INSERT INTO mesas (capacidad, activa) VALUES (6, 1);
INSERT INTO mesas (capacidad, activa) VALUES (8, 0);

-- Datos para categorias_plato
INSERT INTO categorias_plato (nombre) VALUES ('Entradas');
INSERT INTO categorias_plato (nombre) VALUES ('Fondos');
INSERT INTO categorias_plato (nombre) VALUES ('Postres');
INSERT INTO categorias_plato (nombre) VALUES ('Bebestibles');

-- Datos para platos
INSERT INTO platos (codigo, nombre, id_categoria, precio, disponible) VALUES ('ENT-01', 'Ceviche Mixto', 1, 8500.00, 1);
INSERT INTO platos (codigo, nombre, id_categoria, precio, disponible) VALUES ('FON-01', 'Lomo a lo Pobre', 2, 12900.00, 1);
INSERT INTO platos (codigo, nombre, id_categoria, precio, disponible) VALUES ('FON-02', 'Paila Marina', 2, 11500.00, 1);
INSERT INTO platos (codigo, nombre, id_categoria, precio, disponible) VALUES ('POS-01', 'Leche Asada', 3, 4500.00, 1);
INSERT INTO platos (codigo, nombre, id_categoria, precio, disponible) VALUES ('BEB-01', 'Jugo Natural Piña', 4, 3500.00, 0);

-- Datos para pedidos
INSERT INTO pedidos (numero_mesa, garzon, propina, total, estado) VALUES (1, 'Juan Pérez', 0, 8500.00, 'abierto');
INSERT INTO pedidos (numero_mesa, garzon, propina, total, estado) VALUES (2, 'María Soto', 1290.00, 12900.00, 'servido');
INSERT INTO pedidos (numero_mesa, garzon, propina, total, estado) VALUES (3, 'Juan Pérez', 0, 0, 'anulado');
INSERT INTO pedidos (numero_mesa, garzon, propina, total, estado) VALUES (4, 'Carlos Tapia', 1600.00, 16000.00, 'pagado');

-- Datos para detalle_pedido
INSERT INTO detalle_pedido (id_pedido, codigo_plato, cantidad, precio_unitario, observacion) VALUES (1, 'ENT-01', 1, 8500.00, 'Sin cebolla');
INSERT INTO detalle_pedido (id_pedido, codigo_plato, cantidad, precio_unitario, observacion) VALUES (2, 'FON-01', 1, 12900.00, 'Carne a punto');
INSERT INTO detalle_pedido (id_pedido, codigo_plato, cantidad, precio_unitario, observacion) VALUES (4, 'FON-02', 1, 11500.00, NULL);
INSERT INTO detalle_pedido (id_pedido, codigo_plato, cantidad, precio_unitario, observacion) VALUES (4, 'POS-01', 1, 4500.00, NULL);

COMMIT;