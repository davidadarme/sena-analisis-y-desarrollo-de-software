use pubs
create table empleados(
id_usuario int primary key identity(1,1),-- identity sirve para que la tabla incremente 
nombre varchar(30)
)
insert into empleados (nombre) values ('luis')-- para agregar un dato a la tabla
select*from empleados-- sirve para ver como va la tabla
insert into empleados (nombre) values ('david')
drop table empleados
truncate table empleados--

create table vehiculos(
patente char(6)not null,
tipo char(4),
hora_llegada time not null,
hora_salida time,
primary key(patente,hora_llegada)--referenciar dos llaves en un campo
)
drop table vehiculos