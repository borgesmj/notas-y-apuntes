## Tema 1.1: Introducción
:arrow_up: [ir al inicio](./README.md#tabla-de-contenidos)

* [Introducción](#tema-11-introducción)
* 1.1 [¿Qué significa SQL?](#qué-significa-sql)
* 1.2 [Select](#select)
* 1.3 [FROM](#from)
* Seleccionando datos
* 2.1 [Seleccionando todas las columnas de una tabla](#12-seleccionando-todas-las-columnas-de-una-tabla)
* 2.2 [Seleccionando una columna de la tabla](#13-seleccionando-una-columna-de-la-tabla)
* 2.3 [Seleccionando múltiples columnas de una tabla](#14-seleccionando-múltiples-columnas-de-una-tabla)
* 2.4 [Asignando un alias a una columna con "AS"](#16--asignando-un-alias-a-una-columna-con-as)
* 2.5 [Asignando un alias a varias columnas con "AS"](#17-asignando-un-alias-a-varias-columnas-con-as)
* 2.6 [Asignando un alias con AS y comillas dobles](#18-asignando-un-alias-con-as-y-comillas-dobles)

### ¿Qué significa SQL?
SQL viene de Structured Query Language (Lenguaje Estructurado de Consultas); es un lenguaje de programación que se utiliza para comunicarse y administrar bases de datos. SQL es un estándar para manipular datos almacenados en sistemas de gestión de bases de datos relacionales (relational database management systems - RDBMS), así como para el procesamiento de flujos en sistemas de gestión de flujos de datos relacionales (in a relational data stream management system - RDSMS). Fue desarrollado por primera vez en la década de 1970 por IBM.

> Una base de datos relacional representa una colección de tablas relacionadas

SQL consiste en varios componentes, cada uno con su único propósito en comunicación de bases de datos:

* Consultas: Es el componente que permite recuperar datos de una base de datos. La sentencia SELECT es la más utilizada para este fin.
* Lenguaje de definición de datos ( Data Definition Language - DDL): Permite crear, modificar o eliminar bases de datos y sus objetos relacionados, como tablas, vistas, etc. Los comandos incluyen:
  - [CREATE TABLE](./15-tablas.md#nuestra-primera-tabla)
  - CREATE INDEX
  - CREATE VIEW
  - [ALTER](./15-tablas.md#actualizar-una-tabla)
  - [DROP](./15-tablas.md#borrar-una-tabla)
  - TRUNCATE
* Lenguaje de manipulación de datos ( Data manipulation Language - DML): Permite gestionar datos dentro de objetos de bases de datos. Estos comandos incluyen:
  - [SELECT](./#select)
  - [INSERT](./13-insercion-de-registros.md#añadir-un-registro-en-una-tabla)
  - [DELETE](./14-borrado-y-modificacion-de-registros.md#borrar-todos-los-registros-de-una-tabla)
  - [UPDATE](./14-borrado-y-modificacion-de-registros.md#editar-registros)
* Lenguaje de control de datos ( Data control Language - DCL): Incluye comandos como GRANT y REVOKE, que tratan principalmente de derechos, permisos y otras tareas de gestión a nivel de control para el sistema de base de datos.

**Tipos de  datos**
* Numéricos:
  - Integer: valor entero
  - Numeric (n,m): numero de hasta 18 dígitos (con decimales) donde **n** representa el total de dígitos admitidos y **m** el numero de posiciones decimales.
  - Decimal (n.m): igual que numeric.
  - Float: npumero de coma flotante
* Alfanumáricos:
  - Char(n): almacena de 1 a 255 caracteres fijo.
  - varchar(n): datos de cadena de tamañp variable
* Fecha:
  - Date: almacena fechas con tema, mes y año
  - datetime: almacena fechas con fecha y hora
* Logicos:
  - BIT: tipo bit. Se aplica logica booleana
  - Boolean: cero => false. Distinto de cero => true.

SQL viene en muchas formas, como bases de datos Oracle, Microsoft SQL Server y MySQL. A pesar de sus muchas diferencias, todas las bases de datos SQL manejan los mismos comandos.

Una de las acciones que mas se requieren en SQL es consular los datos de una tabla. Esto lo podemos hacer con la instrucción `Select`

### `Select`
La sentencia `SELECT` se utiliza en SQL para seleccionar datos específicos de una base de datos. En otras palabras, se utiliza para seleccionar de la base de datos lo que se desea mostrar. La sintaxis de la sentencia SELECT es bastante sencilla:

#### Sintaxis:
Asi luce nuestro comando `Select`

```sql
SELECT column1, column2 ...
FROM table_name
```
### `FROM`
La clausula `FROM` en SQL especifica las tablas donde la busqueda debe ser hecha. Es una parte integral de la declaracion `SELECT` y sus variantes, como `SELECT INTO` y `SELECT WHERE`. `FROM` puede ser usado para unir tablas tambien. 

Normalmente, FROM va seguido de una lista delimitada por espacios de las tablas en las que se va a ejecutar la operación SELECT. Si necesita extraer datos de varias tablas, separe cada tabla con una coma.

Aqui hay unos ejemplos:
#### Ejemplo 1
Si tenemos una tabla llamada `employees` podemos seleccionar todos la informacion de los empleados utilizando:

```sql
SELECT *
FROM employees
```

#### Ejemplo 2: Seleccionando desde multiples tablas
Si tenemos multiples tablas, digase `employees` y `departaments` y queremos seleccionar la infoirmacion de ambos, podemos hacer lo siguiente:

```sql
SELECT employees.name, departments.department 
FROM employees, departments 
WHERE employees.dept_id = departments.dept_id;
```

En este ejemplo, la clausula `FROM` está seguida por dos tablas `employees` y `departments`. `employees.name` y `departments.name` indica que estamos seleccionando la columna `name` desde la tabla `employees` y la columna `department` desde la tabla `departments`


### 1.2 Seleccionando todas las columnas de una tabla
Si queremos seleccionar todas las columnas de una tabla, podemos usar el `*` asi:

```sql
SELECT * FROM table_name
```
### 1.3 Seleccionando una columna de la tabla
En este ejercicio se tiene una tabla llamado usuarios que tiene las columnas nombre, apellido, email y telefono.

Selecciona sólo los nombres de la tabla usuarios.

```sql
SELECT nombre
from usuarios
```

### 1.4 Seleccionando múltiples columnas de una tabla
Supongamos que tenemos una tabla llamada productos con las columnas 'nombre', 'precio', 'cantidad' y 'proveedor'. Selecciona sólo el nombre, precio y el proveedor

```sql
SELECT nombre, precio, proveedor FROM productos
```

### 1.6  Asignando un alias a una columna con "AS"
Se tiene una tabla llamada usuarios con las columnas nombre, apellido, email y teléfono. Selecciona todos los nombres bajo el alias "cliente"

```sql
SELECT nombre as cliente from usuarios
```

### 1.7 Asignando un alias a varias columnas con "AS"
Cambia el nombre de la columna 'nombre' a 'nombre_usuario' y el nombre de la columna 'apellido' a 'apellido_usuario' en la tabla usuarios.

```sql
select nombre as nombre_usuario, apellido as apellido_usuario from usuarios
```
Otro ejemplo:
```sql
SELECT e.name, d.department 
FROM employees AS e, departments AS d
WHERE e.dept_id = d.dept_id;
```
En este ejemplo, las tablas `employees` y `departments` son llamadas `e` y `d`respectivamente.

### 1.8 Asignando un alias con AS y comillas dobles

Selecciona el nombre y el email de los usuarios de la tabla usuarios, y asigna el nombre 'Correo electrónico' a la columna 'email'.

```sql
select nombre, email as "Correo electrónico" from usuariosF
```