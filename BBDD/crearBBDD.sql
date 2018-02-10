-- entrar inicialmente a mysql desde la carpeta con el script con: sudo mysql -u root -p
-- luego ejecutar este script con: source ./crearBBDD.sql
-- salir con: exit;
-- apartir de ahora se puede trabajar en la base sin el root con:
-- mysql -u bdocalculator -p'bdocalculator' 'bdocalculator'
CREATE DATABASE bdocalculator;
GRANT USAGE ON bdocalculator.* TO bdocalculator@localhost IDENTIFIED BY 'bdocalculator';
GRANT ALL PRIVILEGES ON bdocalculator.* TO bdocalculator@localhost;
FLUSH PRIVILEGES;
