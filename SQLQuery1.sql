alter database empleados modify name=Pubs
drop database Pubs
drop database estudios
drop database Llaves
use master
create database factura
use factura
create table clientes(
id int primary key,
nombre varchar(60),
estado bit
)
create table articulos(
id int primary key,
nombre varchar(60),
precio decimal(9,2)
)
create table ordenes(
id int primary key,
fecha date,
id_cliente int foreign key references clientes(id)
)
alter authorization on database:: factura to sa
create table articulos_ordenes(
id int primary key,
cantidad tinyint,
id_ordenes int foreign key references ordenes(id),
id_articulos int foreign key references articulos(id)
)

