CREATE database IF NOT EXISTS bdoMarket;
use bdoMarket;

CREATE TABLE IF NOT EXISTS objeto(
  id int unsigned AUTO_INCREMENT PRIMARY key,
  nombre varchar(40)
  id_precio int unsigned,
  index(id_precio),
  foreign key(id_precio) reference precio (id) on delete cascade on update no action
);

CREATE TABLE IF NOT EXISTS proceso(
  id int unsigned AUTO_INCREMENT PRIMARY key,
  nombre varchar(40)
);

CREATE TABLE IF NOT EXISTS receta(
  id int unsigned AUTO_INCREMENT PRIMARY key,
  nota varchar(300),
  resultado int unsigned,
  index(resultado),
  foreign key(resultado) reference objeto (id) on delete cascade on update no action,
  id_proceso int unsigned,
  index(id_proceso),
  foreign key(id_proceso) reference proceso (id) on delete cascade on update no action
);

CREATE TABLE IF NOT EXISTS ingrediente(
  id int unsigned AUTO_INCREMENT PRIMARY key,
  id_receta int unsigned,
  index(id_receta),
  foreign key(id_receta) reference receta (id) on delete cascade on update no action,
  id_objeto int unsigned,
  index(id_objeto),
  foreign key(id_objeto) reference objeto (id) on delete cascade on update no action,
  cantidad int unsigned

);

CREATE TABLE IF NOT EXISTS precio(
  id int unsigned AUTO_INCREMENT PRIMARY key,
  minimo int unsigned,
  maximo int unsigned,
  precio1 int unsigned,
  precio2 int unsigned,
  precio3 int unsigned,
  precio4 int unsigned
);
