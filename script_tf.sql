DROP DATABASE IF EXISTS bd_trabajofinal;
CREATE DATABASE bd_trabajofinal CHARACTER SET utf8mb4;
USE bd_trabajofinal;

CREATE TABLE tipo_empleado (id_tipoEmp VARCHAR(10) NOT NULL, 
tipo VARCHAR(20) NOT NULL , PRIMARY KEY (id_tipoEmp));

CREATE TABLE area (id_area VARCHAR(10) NOT NULL, 
area VARCHAR(20) NOT NULL , PRIMARY KEY (id_area));

CREATE TABLE empleado (id_emp VARCHAR(10) NOT NULL, 
nombre VARCHAR(20) NOT NULL , apellido VARCHAR(20) NOT NULL, 
id_tipoEmp VARCHAR(10) NOT NULL , PRIMARY KEY (id_emp));

CREATE TABLE usuario (id_usuario VARCHAR(10) NOT NULL, 
user VARCHAR(20) NOT NULL , pass VARCHAR(20) NOT NULL, 
id_emp VARCHAR(10) NOT NULL , id_area VARCHAR(10) NOT NULL, 
PRIMARY KEY (id_usuario), UNIQUE (id_emp));

CREATE TABLE `tipo_documento` (`id_tipoDoc` VARCHAR(10) NOT NULL , 
`tipo` VARCHAR(20) NOT NULL , PRIMARY KEY (`id_tipoDoc`));

CREATE TABLE `bd_trabajofinal`.`tipo_clave` (`id_tipoClave` VARCHAR(10) NOT NULL , 
`tipo` VARCHAR(20) NOT NULL , PRIMARY KEY (`id_tipoClave`));

CREATE TABLE `documento` (`id_doc` VARCHAR(10) NOT NULL , 
`emisor` VARCHAR(20) NOT NULL , 
`receptor` VARCHAR(20) NOT NULL , 
`proveido` VARCHAR(20) NOT NULL , 
`motivo` VARCHAR(50) NOT NULL , 
`palabra_clave` VARCHAR(10) NOT NULL , 
`tipo_documento` VARCHAR(10) NOT NULL , PRIMARY KEY (`id_doc`));

CREATE TABLE `movimiento` (`id_mov` VARCHAR(10) NOT NULL , 
`fecha` DATE NOT NULL DEFAULT CURRENT_TIMESTAMP , 
`tipo_mov` VARCHAR(20) NOT NULL , 
`id_usuario` VARCHAR(10) NOT NULL , 
`id_doc` VARCHAR(10) NOT NULL , PRIMARY KEY (`id_mov`));



ALTER TABLE empleado ADD CONSTRAINT R1 FOREIGN KEY (id_tipoEmp) REFERENCES tipo_empleado(id_tipoEmp) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE usuario ADD CONSTRAINT R2 FOREIGN KEY (id_area) REFERENCES area(id_area) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE usuario ADD CONSTRAINT R3 FOREIGN KEY (id_emp) REFERENCES empleado(id_emp) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `documento` ADD FOREIGN KEY (`palabra_clave`) REFERENCES `tipo_clave`(`id_tipoClave`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `documento` ADD FOREIGN KEY (`tipo_documento`) REFERENCES `tipo_documento`(`id_tipoDoc`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `movimiento` ADD FOREIGN KEY (`id_usuario`) REFERENCES `usuario`(`id_usuario`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `movimiento` ADD FOREIGN KEY (`id_doc`) REFERENCES `documento`(`id_doc`) ON DELETE CASCADE ON UPDATE CASCADE;


/*------------------------------------*/

INSERT INTO area (id_area, area) 
VALUES ('A1', 'SECRETARÍA'), ('A2', 'SISTEMAS');

INSERT INTO tipo_empleado (id_tipoEmp, tipo) 
VALUES ('TE1', 'JEFE'), ('TE2', 'EMPLEADO');

INSERT INTO empleado (id_emp, nombre, apellido, id_tipoEmp) 
VALUES ('E1', 'ALEX', 'FLORES', 'TE2'), ('E2', 'ANDRÉ', 'CASTILLO', 'TE2')

INSERT INTO `usuario` (`id_usuario`, `user`, `pass`, `id_emp`, `id_area`) 
VALUES ('U1', 'alex', 'alex', 'E1', 'A1'), ('U2', 'andre', 'andre', 'E2', 'A1');

INSERT INTO `empleado` (`id_emp`, `nombre`, `apellido`, `id_tipoEmp`) 
VALUES ('E3', 'MICHEL', 'BAÑARES', 'TE2')

INSERT INTO `tipo_documento` (`id_tipoDoc`, `tipo`) 
VALUES ('TD1', 'FÏSICO'), ('TD2', 'VIRTUAL') ;

INSERT INTO `tipo_clave` (`id_tipoClave`, `tipo`) 
VALUES ('C1', 'NORMATIVA'), ('C2', 'SOLICITUD') ;

INSERT INTO `documento` (`id_doc`, `emisor`, `receptor`,`proveido`, `motivo`,`palabra_clave`, `tipo_documento`) 
VALUES ('DOC1', 'Perez', 'Alex Flores', 'SISTEMAS', 'Solicitud de entrevista', 'C2','TD1'),
('DOC2', 'Jorge', 'Alex Flores', 'VENTAS', 'Solicitud de entrevista', 'C2','TD1');

/* SELECT * FROM usuario WHERE user = "andre"; */