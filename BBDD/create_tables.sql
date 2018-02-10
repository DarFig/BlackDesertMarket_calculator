CREATE database IF NOT EXISTS bdocalculator;
use bdocalculator;

CREATE TABLE IF NOT EXISTS precio(
  id int unsigned AUTO_INCREMENT PRIMARY key,
  minimo int unsigned,
  maximo int unsigned,
  precio1 int unsigned,
  precio2 int unsigned,
  precio3 int unsigned,
  precio4 int unsigned
);

CREATE TABLE IF NOT EXISTS proceso(
  id int unsigned AUTO_INCREMENT PRIMARY key,
  nombre varchar(40)
);

CREATE TABLE IF NOT EXISTS objeto(
  id int unsigned AUTO_INCREMENT PRIMARY key,
  nombre varchar(40),
  id_precio int unsigned,
  index(id_precio),
  foreign key (id_precio) references precio (id) on delete cascade on update no action
);


CREATE TABLE IF NOT EXISTS receta(
  id int unsigned AUTO_INCREMENT PRIMARY key,
  nota varchar(300),
  resultado int unsigned,
  index(resultado),
  foreign key (resultado) references objeto (id) on delete cascade on update no action,
  id_proceso int unsigned,
  index(id_proceso),
  foreign key (id_proceso) references proceso (id) on delete cascade on update no action
);

CREATE TABLE IF NOT EXISTS ingrediente(
  id int unsigned AUTO_INCREMENT PRIMARY key,
  id_receta int unsigned,
  index(id_receta),
  foreign key (id_receta) references receta (id) on delete cascade on update no action,
  id_objeto int unsigned,
  index(id_objeto),
  foreign key (id_objeto) references objeto (id) on delete cascade on update no action,
  cantidad int unsigned

);


