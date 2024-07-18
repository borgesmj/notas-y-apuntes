
# Aprendiendo SQL
Notas tomadas del [**curso interactivo de Desafío LATAM**](https://sqlinteractivo.desafiolatam.com/cursos/1) e información tomada de [roadmap.sh](https://roadmap.sh/sql)

Este contenido estará estructurado acorde al contenido de Desafío LATAM y se refuerza con la información del roadmap.sh

> Nota rápida: siempre tener en cuenta el [orden de las clausulas](./#orden-de-clausulas)


## Tabla de contenidos

| DIA                           | Enlace                                  |
|-------------------------------|-----------------------------------------|
| Tema 1: Conceptos básicos      | [ir](.#tema-1-introduccion)           |
| Tema 2: Seleccionando filas     | [ir](.#tema-2-seleccionando-filas)    |
| Tema 3: Ordenando Resultados   | [ir](.#tema-3-ordenando-resultados)   |
| Tema 4: Limit                  | [ir](.#tema-4-limit)                  |
| Tema 5: Operaciones con string | [ir](.#tema-5-operaciones-con-string) |
| Tema 6: Operaciones con fechas | [ir](.#tema-6-operaciones-con-fechas) |
| Tema 7: Funciones de agregacion | [ir](.#tema-7-funciones-de-agregacion) |
| Tema 8: Distinct | [ir](.#tema-8-distinct) |
| Tema 9: Introducción a grupos | [ir](.#tema-9-introducción-a-grupos) |
| Tema 10: HAVING | [ir](.#tema-10-having) |
| Tema 11: Subconsultas | [ir](.#tema-11-subconsultas) |
| Tema 12: Combinacion de consultas | [ir](.#tema-12-combinacion-de-consultas) |
| Tema 13: Insercion de registros | [ir](.#tema-13-insercion-de-registros) |
| Tema 14: Borrado y modificación de registros | [ir](.#tema-14-Borrado-y-modificación-de-registros) |
| Tema 15: Tablas | [ir](.#tema-15-tablas) |
| Tema 16: Restricciones | [ir](.#tema-16-restricciones) |
| Tema 17: Consultas en multiples tablas | [ir](.#tema-17-consultas-en-multiples-tablas) |
| Tema 18: Tipos de join | [ir](.#tema-18-Tipos-de-join) |
| Tema 19: Cardinalidad | [ir](.#tema-19-Cardinalidad)
| Operadores | [ir](.#operadores) |


## Tema 1.1: Introducción
:arrow_up: [ir al inicio](.#tabla-de-contenidos)
### ¿Qué significa SQL?
SQL viene de Structured Query Language (Lenguaje Estructurado de Consultas); es un lenguaje de programación que se utiliza para comunicarse y administrar bases de datos. SQL es un estándar para manipular datos almacenados en sistemas de gestión de bases de datos relacionales (relational database management systems - RDBMS), así como para el procesamiento de flujos en sistemas de gestión de flujos de datos relacionales (in a relational data stream management system - RDSMS). Fue desarrollado por primera vez en la década de 1970 por IBM.

> Una base de datos relacional representa una colección de tablas relacionadas

SQL consiste en varios componentes, cada uno con su único propósito en comunicación de bases de datos:

* Consultas: Es el componente que permite recuperar datos de una base de datos. La sentencia SELECT es la más utilizada para este fin.
* Lenguaje de definición de datos ( Data Definition Language - DDL): Permite crear, modificar o eliminar bases de datos y sus objetos relacionados, como tablas, vistas, etc. Los comandos incluyen:
  - [CREATE TABLE](./#nuestra-primera-tabla)
  - CREATE INDEX
  - CREATE VIEW
  - [ALTER](./#actualizar-una-tabla)
  - [DROP](./#borrar-una-tabla)
  - TRUNCATE
* Lenguaje de manipulación de datos ( Data manipulation Language - DML): Permite gestionar datos dentro de objetos de bases de datos. Estos comandos incluyen:
  - [SELECT](./#select)
  - [INSERT](./#añadir-un-registro-en-una-tabla)
  - [DELETE](./#borrar-todos-los-registros-de-una-tabla)
  - [UPDATE](./#editar-registros)
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
## Tema 2: Seleccionando filas

:arrow_up: [ir al inicio](.#tabla-de-contenidos)

SQL provee una clausula WHERE que es usada basicamente para filtrar los registros. Si la condicion especificada en la clausula WHERE se cumple, entonces solo se muestra los valores especificios de la tabla. Debes usar la clasusula WHERE para filtrar los registros y traer los registros necesarios.

### Where
> La clasusula WHERE no solo se usa en SELECT, tambien es usado en UPDATE, DELETE, etc. 

Por ejemplo, disponemos de una llamada productos con las columna "precio", podemos recuperar todas las filas que tengan el precio mayor a 100

```sql
SELECT * from productos WHERE precio > 100
```

Un detalle importante es que las clausulas tienen un orden
1. SELECT
2. FROM
3. WHERE

Si cambiamos el orden, podemos tener un error de sintaxis

Se tiene una tabla llamada productos, con las columnas id, nombre, precio y descuento. Selecciona todos los registros cuyo descuento sea mayor a 10.

```sql
select * from productos where descuento > 10
```
Se tiene una tabla llamada productos, con las columnas id, nombre, precio y descuento.

```sql
select * from productos where precio > 200
```
### Utilizando el operador mayor o igual que

Selecciona todos los registros de la tabla productos en los que el valor de la columna 'precio' sea mayor o igual a 50.

Si mostraras sólo los productos con precio a mayor a 50, se mostaría la Lámpara de escritorio?

```sql
select * from productos where precio >= 50
```

#### Utilizando el operador menor que

Se tiene una tabla usuarios con las columnas id, nombre, apellido, email y telefono. Selecciona todas los registros de la tabla usuarios donde el valor de la columna id sea menor a 3.

```sql
select * from usuarios where id < 3
```

#### Utilizando el operador menor o igual que en una condicion
Selecciona todos los registros de la tabla productos en los que el valor de la columna 'precio' sea menor o igual a 100.
```sql
select * from productos where precio <= 100
```
#### Seleccionando multiples filas bajo una condición
Selecciona el nombre, precio y cantidad de la tabla productos cuya cantidad sea mayor a 6.

```sql
select nombre, precio, cantidad from productos where cantidad > 6
```

#### Seleccionando filas bajo una condición de igualdad
Selecciona el nombre del usuario de la tabla usuarios con id igual a 2
```sql
select nombre from usuarios where id = 2
```

#### Seleccionando filas bajo una condición de igualdad (tipo de dato string)
Selecciona todas las filas de la tabla productos donde el nombre del producto sea 'Pantalón'.
```sql
select * from productos where nombre = 'Pantalón'
```
#### Seleccionando filas bajo una condición de igualdad (tipo de dato string) parte 2
Es importante recordar que al trabajar con strings, la comparación es sensible a mayúsculas y minúsculas. Por lo tanto, 'Camiseta' y 'camiseta' se considerarán diferentes valores en la comparación. Si deseamos realizar una comparación sin considerar la distinción entre mayúsculas y minúsculas, se pueden utilizar funciones o cláusulas específicas proporcionadas por el motor de base de datos.

Selecciona todos los productos de la tabla productos que tengan el nombre 'Silla de Oficina'.

Puedes probar con 'c' y observar que no obtendrás ningún resultado.

```sql
select * from productos where nombre = "Silla de Oficina"
```
#### Seleccionando filas bajo una condición de igualdad (tipo de dato booleano true)

Hasta el momento hemos trabajado con dos tipos de datos: números enteros, como el precio del producto, y strings, como 'Camiseta'. En este ejercicio introduciremos el tipo de dato Boolean, el cual puede guardar como valor verdadero o falso, TRUE o FALSE.

Supongamos que tenemos una tabla de productos con una columna 'destacado' de tipo booleano que indica si un producto está destacado o no. Para seleccionar todos los productos que están marcados como destacados, podemos usar la siguiente consulta:

```sql
SELECT * FROM productos WHERE destacado = true;
```

Adicionalmente se pueden ocupar los valores 1 y 0 en lugar de las palabras reservadas true o false, por ejemplo la siguiente consulta es identica a la anterior.

```sql
SELECT * FROM productos WHERE destacado = 1;
```
Se tiene una tabla de usuarios con los campos id, nombre, apellido, email, teléfono y status. La columna status es de tipo booleano.

Selecciona todos los usuarios de la tabla usuarios cuyo status es activo.

```sql
select * from usuarios where status = 1
```

#### Seleccionando filas bajo una condición de igualdad (tipo de dato booleano false)
Selecciona todos los productos de la tabla productos que no están destacados.
```sql
select * from productos where destacado = 0
```

#### Utilizando dos condiciones con operador "and"
Se tiene una tabla de usuarios con los campos id, nombre, apellido, email y teléfono.

Selecciona todos los usuarios cuyo nombre es 'María' y su email es 'mariagarcia@hotmail.com' de la tabla de usuarios.

```sql
Select *
from usuarios
where nombre = "María" and email = "mariagarcia@hotmail.com"
```
#### Utilizando dos condiciones con operador "and" parte 2
Se tiene una tabla llamada productos que tiene los campos id, nombre, agotado y precio. La columna precio es de tipo Integer mientras que la columna agotado es de tipo Boolean.

Selecciona los productos de la tabla productos que estén agotados y tengan un precio mayor a 100.
```sql
select *
from productos
where agotado = 1 and precio > 100
```
#### Utilizando operador "OR"
Se tiene una tabla productos con los campos id, nombre, precio y descuento. El campo precio y el campo descuento son de tipo integer.

Selecciona todos los productos cuyo precio sea mayor a 1000 o su descuento sea igual a 20.

```sql
select *
from productos
where precio > 1000 or descuento = 20
```
#### Utilizando dos condiciones con operador "or"
Se tiene una tabla clientes con los campos id, nombre, ciudad y saldo. La ciudad es de tipo texto, el saldo es número entero.

Selecciona aquellos clientes de la tabla clientes que sean de la ciudad 'Madrid' o que su saldo sea negativo.

```sql
select *
from clientes
where ciudad = "Madrid" or saldo < 0
```

#### Seleccionando una fecha
En SQL, DATE es un tipo de datoque guarda la fecha. No guarda informacion de tiempo. El formato de la fecha es "YYYY-MM-DD". POr ejemplo, "2022-01-01". SQL provee distintas funciones para manipular fechas:

Sobre las fechas podemos hacer distinto tipo de operaciones, pero primero aprenderemos a utilizarlas para filtrar. Por ejemplo, podemos obtener todos los productos de una tabla cuya fecha sea mayor o igual al primero de enero de 2022

`SELECT * FROM productos WHERE fecha_de_creación >= '2022-01-01';` 

Ejercicio
Se tiene una tabla de productos con los campos id, nombre, precio y fecha_de_creación. El campo fecha_de_creacion es de tipo Date.

Selecciona todos los productos de la tabla productos que fueron creados después de '2021-05-01'.

```sql
SELECT *
FROM PRODUCTOS
WHERE fecha_de_creación > '2021-05-01'
```

### Seleccionando datos entre dos valores con "between"
Se tiene la tabla productos con los campos id, nombre y stock. Dentro de los registros hay 5 productos con distintos stocks como se muestra a continuación:

| *ID* | +Nombre*   | +STOCK* |
|------|------------|---------|
| 1    | Producto A | 10      |
| 2    | Producto B | 25      |
| 3    | Producto C | 30      |
| 4    | Producto D | 40      |
| 5    | Producto E | 50      |

Selecciona todos los productos cuyo stock se encuentre entre 20 y 30.

```sql
select *
from productos
where stock between 20 and 30
```

### Seleccionando filas con "like"
Supongamos que queremos buscar todos los usuarios cuyo nombre empiece con la letra 'J' en la tabla de usuarios. Podemos hacer esto utilizando la siguiente consulta:
`SELECT * FROM usuarios WHERE nombre LIKE 'J%'`

En esta consulta, estamos utilizando el operador LIKE para buscar todos los nombres de usuarios que comiencen con la letra 'J'.

El símbolo '%' es un comodín que representa cualquier cantidad de caracteres adicionales. En este caso, estamos utilizando '%' después de la letra 'J' para indicar que queremos buscar cualquier nombre que comience con 'J' y tenga cualquier número de caracteres adicionales después de ella.

Ejercicio
Se tiene una tabla usuarios con los campos id, nombre, apellido, email y teléfono. El campo nombre es de tipo texto.

Se pide seleccionar todos los usuarios cuyo apellido empiece con 'Ma'

```sql
select *
from usuarios
where apellido like "Ma%"
```

### Seleccionando con comodin al principio
Supongamos que queremos buscar todos los usuarios cuyo nombre termine con la letra 's' en la tabla de usuarios. Podemos hacer esto utilizando la siguiente consulta:

`SELECT * FROM usuarios WHERE nombre LIKE '%s'`
Ejercicio
Selecciona todos los usuarios de la tabla usuarios cuyo nombre termine con la letra 'o'
```sql
select *
from usuarios
where nombre like "%o"
```

### Seleccionando registros sin valores nulos

Algunos registros pueden tener valores nulos para algunos de sus campos. Por ejemplo, podríamos tener una tabla de usuarios con nombres y emails pero no tener todos los nombres de cada uno de los registros como ilustra la siguiente tabla.

| *ID* | +Nombre*    | *email*               |
|------|-------------|-----------------------|
| 1    | Juan Perez  | juan.perez@email.com  |
| 2    | María Gomez | maria.gomez@email.com |
| 3    |             | carlos.temaz@mail.com  |
| 4    |             | ana.torres@email.com  |
| 5    | Luis Mendez | luis.mendez@email.com |

PAra seleccionar todos los valores no nulos utilizamos `IS NOT NULL`
Por ejemplo, en la tabla usuarios previamente mostrada podemos seleccionar todos los nombres no nulos utilizando `SELECT * FROM empleados WHERE nombre IS NOT NULL`;

Esto nos devolverá todos los usuarios cuyo nombre no sea nulo.

| *ID* | +Nombre*    | *email*               |
|------|-------------|-----------------------|
| 1    | Juan Perez  | juan.perez@email.com  |
| 2    | María Gomez | maria.gomez@email.com |
| 5    | Luis Mendez | luis.mendez@email.com |

Ejercicio
Se tiene una tabla productos con id, nombre, precio y descuento, siendo descuento de tipo integer.

Selecciona todos los registros de la tabla productos cuyo campo descuento no sea nulo.

```sql
SELECT *
FROM productos
where descuento is not null
```

### Seleccionando registros con valores nulos

Se tiene una tabla usuarios con id, nombre, apellido, email y teléfono

Selecciona todos los usuarios que no tengan un email registrado en la tabla de usuarios.

```sql
select *
from usuarios
where email is null
```
## Tema 3: Ordenando resultados
:arrow_up: [ir al inicio](.#tabla-de-contenidos)
### Ordenando filas
En este ejercicio aprenderemos a ordenar las filas de una tabla SQL y para estoi estutemaremos una nueva clausula llamada *ORDER BY*
La clasusula *order by* en SQL es usada para ordernar los resultados de una declaracion SELECT in orden ascendente o descendente. El comando ordena por defecto de maera ascendente, siq ueremos ordenar de manera descendente debemos usar la palabra clave `desc`


#### Sintaxis para orden ascendente
```sql
Select column1, column2
from table_name
order by column1, column2, asc
```

#### Sintaxis para orden desscendente
```sql
Select column1, column2
from table_name
order by column1, column2, desc
```

Ejercicio:
Ordena los registros de la tabla usuarios por el campo 'nombre'
```sql
select * from usuarios order by nombre
```
### Ordenando filas asc explicito
Ejercicio
En este ejercicio se tiene una tabla usuarios con los campos id, nombre, apellido, email y teléfono. Se te pide ordenar los registros de la tabla 'usuarios' por el campo 'nombre' en orden ascendente.
```sql
select * from usuarios order by nombre asc
```

### Ordenando filas desc
Ejercicio
Se tiene una tabla productos con los campos id, nombre, precio y stock. Selecciona sólo los precios de la tabla 'productos' ordenados de forma descendente.
```sql
select precio from productos order by precio desc
```

### Ordenando filas con valores nulos
Ordena la tabla empleados por la columna 'salario' de manera ascendente.
```sql
select * from empleados order by salario asc
```

### Ordenando con nulos al final
Con NULLS FIRST se muestran los nulos primeros y con NULLS LAST se muestran al final

Ejercicio
Dada una tabla productos con las columnas 'id', 'nombre' y 'precio' con los siguientes registos.

| ID | NOMBRE     | PRECIO |
|----|------------|--------|
| 1  | Producto 1 | 100    |
| 2  | Producto 2 | NULL   |
| 3  | Producto 3 | 50     |
| 4  | Producto 4 | NULL   |
| 5  | Producto 5 | 200    |

Ordena las filas de la tabla en función del precio de forma ascendente. Asegúrate de que las filas con valores nulos en la columna 'precio' aparezcan al final de la lista ordenada.

```sql
select * from productos order by precio asc nulls last
```
### Combinaciones de orden

En algunas situaciones vamos a querer ordenar en función de múltiples columnas. Por ejemplo, si queremos obtener una lista de todos los productos ordenados por su stock y luego por su color, podemos seleccionar todos los campos de la tabla y ordenarlos primero por el campo stock y luego por el campo color de la siguiente manera:

```SELECT * FROM productos ORDER BY stock ASC, color ASC```

Ejercicio
Se tiene la tabla empleados con la siguiente información:

| ID | NOMBRE         | SALARIO |
|----|----------------|---------|
| 1  | Juan Pérez     | 4800    |
| 2  | María López    | 5500    |
| 3  | Pedro García   | 5500    |
| 4  | Ana Martínez   | 5500    |
| 5  | Luis Rodríguez | 4800    |

Selecciona una lista de todos los empleados ordenados por su salario y por su nombre.
```sql
select * from empleados order by salario asc, nombre asc
```

### Combinaciones de orden asc y desc
Se tiene la tabla productos con la siguiente información:

| ID | NOMBRE     | STOCK | COLOR  |
|----|------------|-------|--------|
| 1  | Silla      | 10    | Rojo   |
| 2  | Mesa       | 5     | Verde  |
| 3  | Lámpara    | 15    | Azul   |
| 4  | Escritorio | 8     | Blanco |
| 5  | Estantería | 12    | Negro  |

Selecciona todos los registros de la tabla 'productos' y ordénalos primero por 'stock' de forma descendente y luego por 'color' de forma ascendente.
```
select * from productos order by stock desc, color asc
```

## Tema 4: Limit
:arrow_up: [ir al inicio](.#tabla-de-contenidos)
### Limitando la cantidad de resultados
La cláusula LIMIT se utiliza para limitar la cantidad de resultados devueltos por una consulta. Esto es útil cuando sólo necesitamos ver una cierta cantidad de registros en lugar de todos los registros que cumplan con la condición de la consulta.

Por ejemplo, si queremos obtener sólo los primeros 5 registros de una tabla, podemos usar la cláusula LIMIT de la siguiente manera:

```
SELECT * FROM tabla LIMIT 5
```

La clausula LIMIT se agrega al final de la consulta.

Ejercicio:

Selecciona los primeros 3 usuarios de la tabla de usuarios.

```
select * from usuarios limit 3
```

### Obtener los primeros alumnos con mejor nota
En SQL, la combinación de las cláusulas ORDER BY y LIMIT nos permite obtener el valor o valores máximos de una columna en una tabla. 

Una vez que hemos ordenado los registros, podemos utilizr la clausula LIMIT para limiatr la cantidad de resultados obtenidos, por ejemplo:

```
Select * from notas order by nota desc limit 3
```

Que corresponde a los tres mejores alumnos de la tabla notas

Ejercicio:

Se tiene una tabla de puntajes con las columnas id y puntaje. Utiliza lo aprendido para obtener el puntaje más alto de la tabla utilizando ORDER BY y LIMIT

```
select puntaje from puntajes order by puntaje desc limit 1
```

### Obtener el nombre del concierto con más entradas vendidas

Se tiene una base de datos con la tabla conciertos en la cual se almacena información sobre cada concierto, incluyendo el nombre del concierto y la cantidad de entradas vendidas. Los datos dentro de la base de datos corresponden a la siguiente tabla.

| NOMBRE_CONCIERTO | ENTRADAS_VENDIDAS |
|------------------|-------------------|
| Concierto A      | 150               |
| Concierto B      | 200               |
| Concierto C      | 180               |
| Concierto D      | 250               |

Encuentra el nombre del concierto que ha vendido la mayor cantidad de entradas (utiliza ORDER BY y LIMIT).

```
SELECT nombre_concierto, entradas_vendidas 
FROM conciertos 
ORDER BY entradas_vendidas DESC 
LIMIT 1
```
## Tema 5: Operaciones con string

:arrow_up: [ir al inicio](.#tabla-de-contenidos)

### Transformando un string en mayusculas
Para transformar un string a mayusculas en [*SQLITE*](https://www.sqlite.org/) podemos utilizar la funcion UPPER()
UPPER() es una funcion de cadena incorporada en SQL. Como lo sugiere su nombre, es unada para convertir todas las letras en una cadena especificada a mayusculas
La sintaxis de la funcion es la siguiente:

```
UPPER(string)
```

Ejercicio
Se tiene una tabla de usuarios con las columnas nombre, apellido, email y teléfono.

Selecciona los emails de la tabla usuarios con el alias email_upper. Todos los emails deben ser mostrados en mayúsculas.

```
SELECT UPPER(email) as email_upper FROM usuarios
```

### Trasformando un string a minúsculas
La funcion LOWER() es una funcion incorporada en que transforma todos los caracteres en mayusculas a minusculas, puede resultar muy util al realizar operaciones de búsqueda o comparaciones que nos e distinguen entre mayusculas o minusculas.

Ejercicio
Se tiene una tabla de usuarios con los campos id, nombre, e email. El campo email es de tipo texto y contiene algunas mayúsculas, lo que puede ocasionar errores en la base de datos.

Selecciona los emails de la tabla usuarios con el alias email_lower. Todos los emails deben ser mostrados en minúsculas.

```
select lower(email) as email_lower
from usuarios
```

### Quitando los espacios en blanco de un string
En SQLite la función TRIM() se utiliza para eliminar los espacios en blanco iniciales y finales de un string.

Por ejemplo, si tenemos una tabla de productos con una columna 'nombre' que contiene espacios en blanco al inicio y final de cada nombre, podemos utilizar la siguiente consulta para quitar esos espacios:

```SELECT TRIM(nombre) FROM productos;```

Esto nos devolverá los nombres de los productos sin los espacios en blanco al inicio y final.

Ejercicio
Se tiene una tabla de usuarios con las columnas nombre, apellido, email y teléfono. Los nombres y correos poseen espacios en blanco tanto al inicio como al final de su valor. Utiliza la función TRIM() para seleccionar los nombres e emails y quitar los espacios en blanco.

```
select trim(nombre), trim(email) from usuarios
```

### Combinando funciones
En SQL podemos combinar funciones. Veamos un ejemplo combinando LOWER y TRIM:

```
SELECT LOWER(TRIM(email)) as email_limpios from usuarios;
```

Esta consulta selecciona los correos electronicos de la tablka 'usuarios', los convierte a minusculas y elimina cualquier espacio adicional alrededor de ellos.

Ejercicio:
Se tiene una tabla de usuarios con las columnas nombre, apellido, email y teléfono. Los nombres, apellidos y correos poseen espacios en blanco tanto al inicio como al final y algunos de ellos tienen mayúsculas.

Utiliza lo aprendido para seleccionar los nombres, emails y apellidos, limpiando cada uno de estos campos. Para que el resultado sea correcto debes ocupar los alias nombre_limpio, apellido_limpio e email_limpio respectivamente.

```
select lower(trim(nombre)) as nombre_limpio, lower(trim(apellido)) as apellido_limpio, lower(trim(email)) as email_limpio
from usuarios
```

### Obteniendo el largo de un string
En SQL LENGTH es una funcion incorporada que te permite encontrar la cantidad de caracteres de una cadena o la longitud de una cadena

```
LENGTH(string)
```

Por ejemplo, si queremos obtener la longituf del nombre de todos los usuarios en la tabla 'usuarios' podriamos utilzar la siguiente consulta

```
SELECT nombre, LENGTH(nombre) FROM usuarios;
```

Ejercicio:
Selecciona el largo del apellido de todos los usuarios en la tabla usuarios.

```
select length(apellido) from usuarios
```

### Obteniendo el nombre mas largo de la tabla
Ejercicio:
Se tiene una tabla usuarios con las columnas nombre, apellido, email y teléfono.

Utiliza lo aprendido para seleccionar el largo de los 3 correos más largos de la tabla. La columna resultante debe mostrar sólo el largo (cantidad de caracteres) de estos correos.

```
select length(email) from usuarios order by length(email) desc limit 3
```

### Ordenando todos los datos y la funcion
Ejercicios
Se tiene una tabla usuarios con las columnas nombre, apellido, email y teléfono.

Utiliza lo aprendido para seleccionar los 3 correos más largos de la tabla. El resultado debe mostrar dos columnas: una con los emails y otra con sus largos respectivos.

```
SELECT email, length(email) 
FROM usuarios 
ORDER BY length(email) DESC 
LIMIT 3
```

### Concatenar strings
CONCAT es una funcion de SQL que te permite concatenar o unir dos o mas cadenas de caracteres. Esto es extremadamente util siempre que necesites combinar  texto de varias columnas en una sola.

La sintaxis de CONCAT es bastante simple:

```
CONCAT (string1, string2, ..., string_n)
```

Esta funcion acepta como entrada cualquier numero de argumentos de cadena desde dos hasta tantos como sea necesario y devuelve una nueva cadena que es el resultado de todas las cadenas de entradas unidas.

Un ejemplo de consulta de concatenacion seria la siguiente:

```
SELECT nombre || ' ' || apellido AS nombre_completo FROM empleados;
```

En esta consulta, estamos concatenando el nombre y el apellido de cada empleado, separados por un espacio, y utilizando el alias 'nombre_completo' para la nueva columna creada

Ejercicio
Supongamos que tienes una tabla llamada productos con los campos 'producto', 'marca' y 'precio'. Selecciona una lista de todos los productos con su nombre, seguido de un guion ("-"), y su marca. Asigna el alias 'marca_producto' a la columna creada.

```
select producto ||'-' ||marca as marca_producto from productos
```

> En SQL, ambas formas de concatenar strings son válidas, pero dependen del sistema de gestión de bases de datos que estés utilizando.
CONCAT (string1, string2, ..., string_n): Esta es la función de concatenación estándar que se utiliza en muchos sistemas de gestión de bases de datos, como MySQL, SQL Server, PostgreSQL, etc. En esta función, se proporcionan los strings que se desean concatenar como argumentos separados por comas.
Ejemplo:
```
SELECT CONCAT(nombre, ' ', apellido) AS nombre_completo FROM empleados;
```
> SELECT nombre || ' ' || apellido AS nombre_completo FROM empleados;: Esta sintaxis con doble barra vertical (||) es específica de algunos sistemas de gestión de bases de datos, como Oracle y SQLite. Se utiliza para concatenar strings.
Ejemplo:
```
SELECT nombre || ' ' || apellido AS nombre_completo FROM empleados;
```
> Ambas formas de concatenación hacen esencialmente lo mismo: combinan los valores de los campos especificados en una sola cadena. La diferencia principal radica en la sintaxis específica del sistema de gestión de bases de datos que estés utilizando.

### Seleccionando caracteres de un string con SUBSTR
LA funcion SQL SUBSTRING se utiliza para extraer una parte de una cadena, donde puede especificar ña posicion inicial y la longitud del texto. Esta funcion puede resultar muy beneficiosa cuando solo necesitas una parte especifica de una cadena

Sintaxis:
```
SUBSTRING(string, start, length)
```

Ejercicio
Se tiene una tabla usuarios con las columnas id, nombre, apellido, email y teléfono. Utiliza la función SUBSTR para seleccionar las tres primeras letras del apellido de cada usuario en la tabla 'usuarios'. Asigna el nombre 'primeras_letras' a la columna creada.

```
select substring(apellido, 1, 3) as primeras_letras
from usuarios
```
### Seleccionando caracteres
Se tiene una tabla de usuarios con las columnas nombre y apellido. Utilizando la función SUBSTR(), selecciona 3 caracteres del apellido de María, partiendo desde el segundo caracter. Asigna el alias 'tres_caracteres_del_apellido' a la columna creada.

```
select substring(apellido, 2, 3) as tres_caracteres_del_apellido
from usuarios
where nombre = 'María'
```


## Tema 6: Operaciones con fechas

:arrow_up: [ir al inicio](.#tabla-de-contenidos)

En SQL, DATE  es un tipo de dato que almacena la fecha. NO ALMACENA EL INFORMACION DEL TIEMPO. EL formato de la fecha es: 'YYYY-MM-DD', por ejemplo: '2022-01-01'
SQL provee de varias funciones para manipular fechas.
SQL provee de muchas funciones para manejar la fecha:

### Obteniendo la fecha de hoy 
con la funcion `DATE()` podemos obtener la fecha de hoy, por ejemplo podemos utilizar la clausula `WHERE`  para obtener los registros del tema de hoy.

```
SELECT * FROM usuarios WHERE fecha_registro = DATE();
```

Tambien es posible indicar explicitamente a la funcion que la fecha deseada es la de hoy:

```
SELECT * FROM usuarios WHERE fecha_registro = DATE('now')
```

Ejercicio
Se tiene una tabla llamada tareas con las siguientes columnas: "id" (identificador único), "descripcion" (descripción de la tarea) y "fecha_limite" (fecha límite para completar la tarea).

Obtén la descripción de todas las tareas que tengan fecha_limite igual a la fecha actual .

```
SELECT descripcion from tareas where fecha_limite = date()
```

### Obteniendo la fecha de mañana
En SQL es posible obtener fechas futuras.  En SQLite lo podemos lograr pasando un segundo argumento a la función DATE. Esto suena complicado pero es mas sencillo de lo que parece:

```
DATE('now', '1 day')
```

En este ejemplo estamos sumando 1 tema a la fecha actual (now). Si queremos sumar mas temas, por ejemplo 5 temas utilizaremos `Date('now', '5 day')`. Tambien es posible sumar semamas, meses, con:

2semanas: `DATE('now', '2 week')`
3 meses: `DATE('now', '3 month')`

Ejercicio
Se tiene una tabla de tareas con los campos id, descripcion y fecha_limite. Se pide seleccionar todos los campos de las tareas que tienen como fecha límite el día de mañana.

```
select * from tareas where fecha_limite = date('now', '1 day')
```

### Obteniendo la fecha de ayer
De la misma manera que buscamos la fecha de mañana, solo que con un numero negativo
```
DATE('now', '-1 day')
```
Ejercicio
Supongamos que tenemos una tabla llamada ganancias con las columnas "id" (identificador único), "fecha" (fecha de registro) y "monto" (ganancia del día).

Muestra el monto correspondiente al día de ayer.

```
select monto from ganancias where fecha = DATE('now', '-1 day')

```

### Extraccion del año
Para ciertos reportes es muy probable que nos pidan extraer informacin de una fecha, como por ejemplo. el año que se hizo una transaccion
Analicemos el siguiente escenario
Se tiene la tabla _ventas_ con la siguiente informacion

| ID_VENTA | MONTO | FECHA_VENTA |
|----------|-------|-------------|
| 1        | 200   | 2010-01-15  |
| 2        | 150   | 2011-02-20  |
| 3        | 300   | 2012-03-10  |
| 4        | 250   | 2013-04-05  |
| 5        | 100   | 2014-05-25  |
| 6        | 350   | 2015-06-18  |
| 7        | 400   | 2015-07-22  |
| 8        | 180   | 2015-08-09  |
| 9        | 220   | 2018-09-30  |
| 10       | 275   | 2019-10-11  |

Nos piden mostrar toda la información de la tabla y adicionalmente agregar una columna con el año de la venta.

```
SELECT *, strftime('%Y', fecha_venta) as año_venta FROM ventas 
```

El resultado de esta consulta será el siguiente

| ID_VENTA | MONTO | FECHA_VENTA | AÑO_VENTA |
|----------|-------|-------------|-----------|
| 1        | 200   | 2010-01-15  | 2010      |
| 2        | 150   | 2011-02-20  | 2011      |
| 3        | 300   | 2012-03-10  | 2012      |
| 4        | 250   | 2013-04-05  | 2013      |
| 5        | 100   | 2014-05-25  | 2014      |
| 6        | 350   | 2015-06-18  | 2015      |
| 7        | 400   | 2015-07-22  | 2015      |
| 8        | 180   | 2015-08-09  | 2015      |
| 9        | 220   | 2018-09-30  | 2018      |
| 10       | 275   | 2019-10-11  | 2019      |


Para mostrar los resultados de este tipo de funciones, es necesario asignar un nombre a la nueva columna, ya que, de lo contrario, la columna resultante mantendrá el nombre de "strftime('%Y', fecha_venta)", lo cual resultaría en una denominación poco legible para un informe

Ejercicio
Dada una tabla ventas con las columnas monto y fecha_venta, crea una consulta que muestre únicamente el monto y el año de la venta. La columna que muestre el año de la venta debe llamarse año_venta

```
select monto, strftime('%Y', fecha_venta) as año_venta from ventas
```


### Extracción del mes

En este caso, para obtener el mes, pasamos %m como argumento a la función strftime.

Ejercicio
Dada la tabla ventas previamente presentada con las columnas monto y fecha_venta, crea una consulta que muestre una tabla con el monto, el mes de la venta y el año de la venta, en ese mismo orden. La columna para el mes de la venta debe llamarse mes_venta y aquella para el año de la venta debe llamarse año_venta

```
select monto, strftime('%m', fecha_venta) as mes_venta, strftime('%Y', fecha_venta) as año_venta from ventas
```

### Extraccion del mes y año
Ejercicio
Dada la tabla ventas con las columnas monto y fecha_venta, crea una consulta que muestre las siguientes dos columnas:

* Monto
* El mes y año de la fecha de venta. Esta columna debe llamarse año_mes

| ID_VENTA | MONTO | FECHA_VENTA |
|----------|-------|-------------|
| 1        | 200   | 2010-01-15  |
| 2        | 150   | 2011-02-20  |
| 3        | 300   | 2012-03-10  |
| 4        | 250   | 2013-04-05  |
| 5        | 100   | 2014-05-25  |
| 6        | 350   | 2015-06-18  |
| 7        | 400   | 2015-07-22  |
| 8        | 180   | 2015-08-09  |
| 9        | 220   | 2018-09-30  |
| 10       | 275   | 2019-10-11  |

```
select monto, strftime('%Y-%m', fecha_venta) as año_mes from ventas
```

### Extracciones y where

Previamente aprendimos a filtrar utilizando como parámetro una fecha. Ahora utilizaremos lo aprendido para filtrar fechas de un año o mes en específico.

Se tiene la tabla ventas con la siguiente información:

| ID_VENTA | MONTO | FECHA_VENTA |
|----------|-------|-------------|
| 1        | 200   | 2010-01-15  |
| 2        | 150   | 2011-02-20  |
| 3        | 300   | 2012-03-10  |
| 4        | 250   | 2013-04-05  |
| 5        | 100   | 2014-05-25  |
| 6        | 350   | 2015-06-18  |
| 7        | 400   | 2015-07-22  |
| 8        | 180   | 2015-08-09  |
| 9        | 220   | 2018-09-30  |
| 10       | 275   | 2019-10-11  |

Nos piden mostrar todas las ventas del año 2012. Para esto utilizaremos la función strftime para extraer el año de las fechas, y luego filtraremos por el año indicado:

```
SELECT * FROM ventas WHERE strftime('%Y', fecha_venta) = '2012';
```

Ejercicio
Dada una tabla ventas con las columnas monto y fecha_venta, selecciona toda la información de las ventas del 2015

```
select * from ventas where strftime('%Y', fecha_venta) = '2015'
```
## Tema 7: Funciones de agregacion
:arrow_up: [ir al inicio](.#tabla-de-contenidos)

### El mayor valor de una columna
En SQL hay funciones que nos permiten ejecutar operaciones sobre un conjunto de resultados. Estas reciben el nombre de **funciones de agregacion**

En este ejercicio trabajaremos con la funcion `MAX()` la cual nos permite encontrar el valor mas alto del campo que especifiquemos.
Se puede utiizar para tipos de datos de columnas numericos, caracteres y fecha. Si hay valores nulos, no son tomados para comparacion.

Sintaxis
```
SELECT MAX(column_name)
FROM table_name
where condition;
```

Por ejemplo:

Se tiene una tabla llamada empleados con los siguientes datos:

| EMAIL                   | NOMBRE         | EDAD | SUELDO |
|-------------------------|----------------|------|--------|
| juan.perez@workmail.com | Juan Pérez     | 30   | 50,000 |
| maria.gonzalez@corp.com | Maria González | 25   | 55,000 |
| john.doe@techplace.org  | John Doe       | 40   | 60,000 |
| francisco@startup.io    | Francisco      | 22   | 45,000 |

Podemos encointrar el salario mas alto utilizando:

```
SELECT MAX(salario) FROM empleados
```

> Cuando usamos funciones de agregacion, no podemos seleccionar directamente otros elementos de la misma tabla. Por ejemplo, `SELECT email, MAX(salario) FROM empleados;` arrojaria un error ya que estariamos selecionando email junto a la funcion. Pero no te preocupes, ya que aprenderemos como hacerlo apropiadamente cuando veamos la clausula _group by_ mas adelante

Ejercicio:
Utilizando los mismos datos previos selecciona la mayor edad de la tabla empleados

Tip: Aunque en SQL es válido escribir tanto MAX (columna) como MAX(columna), el corrector de ejercicios considerará la primera opción como incorrecta debido al espacio adicional. Por lo tanto, escribe la función sin espacios.

```
select max(edad)
from empleados
```

### El menor valor de una columna
`MIN` es una funcion agregada que se usa para retornar el valor mas pequeño en una columna seleccionada. 


Ejercicio
Utilizando la tabla empleados, encuentra el menor sueldo presente.

| EMAIL                   | NOMBRE         | EDAD | SUELDO |
|-------------------------|----------------|------|--------|
| juan.perez@workmail.com | Juan Pérez     | 30   | 50,000 |
| maria.gonzalez@corp.com | Maria González | 25   | 55,000 |
| john.doe@techplace.org  | John Doe       | 40   | 60,000 |
| francisco@startup.io    | Francisco      | 22   | 45,000 |

```
SELECT MIN(sueldo)
FROM empleados
```

### Suma de elementos de una columna
Hasta el momento hemos estutemado dos funciones de agregacion:
* MAX()
* MIN()

En este ejercicio introduciremos la funcion de agregacion `SUM()`.
LA funcion `SUM()` en SQL es usada para calcular la suma de una columna. Esta funcion nos permite sumar una columna de numeros en una tabla SQL.

La sintaxis de `SUM()` es:

```
SELECT SUM(column_name) FROM table_name
```

> Es importante tener en cuenta que la colunma donde se aplique `SUM()` debe tener solo valores numericos, de lo contrario, la consulta puede generar error o un resultado inesperado.


Ejercicio:

Utilizando la tabla empleados, encuentra la suma de todos los sueldos.

| EMAIL                   | NOMBRE         | EDAD | SUELDO |
|-------------------------|----------------|------|--------|
| juan.perez@workmail.com | Juan Pérez     | 30   | 50,000 |
| maria.gonzalez@corp.com | Maria González | 25   | 55,000 |
| john.doe@techplace.org  | John Doe       | 40   | 60,000 |
| francisco@startup.io    | Francisco      | 22   | 45,000 |


```
select sum(sueldo) from empleados
```

### Promedipo de una columna
La funcion en SQL `AVG()` es una funcion de agregacion, que retorna el valor promedio de una columna numerica. Esta funcion calcula la suma de valores en una columna y lo divide por el conteo de esos valores.

Ejercicio
Utilizando la tabla empleados, encuentra el promedio de todos los sueldos.

| EMAIL                   | NOMBRE         | EDAD | SUELDO |
|-------------------------|----------------|------|--------|
| juan.perez@workmail.com | Juan Pérez     | 30   | 50,000 |
| maria.gonzalez@corp.com | Maria González | 25   | 55,000 |
| john.doe@techplace.org  | John Doe       | 40   | 60,000 |
| francisco@startup.io    | Francisco      | 22   | 45,000 |


```
select AVG(sueldo) from empleados
```

### Contando elementos en una tabla

`COUNT()` es una funcion en SQL que retorna el numero de filas que coincide con un criterio especifico. Esencialmente la funcion `COUNT()` es usado para cuando necesitamos saber el recuento de un registro en la columna de determinada tabla.

Hay dos tipos de funciones COUNT: `COUNT(*)` y `COUNT(column)`

Ejercicio:
Encuentra la cantidad de registros (cantidad de filas) que tiene la tabla empleados.

| EMAIL                   | NOMBRE         | EDAD | SUELDO |
|-------------------------|----------------|------|--------|
| juan.perez@workmail.com | Juan Pérez     | 30   | 50,000 |
| maria.gonzalez@corp.com | Maria González | 25   | 55,000 |
| john.doe@techplace.org  | John Doe       | 40   | 60,000 |
| francisco@startup.io    | Francisco      | 22   | 45,000 |

```
select count(*) from empleados
```

### Ejercicio 1: Funciones de agregacion con where

Las funciones de agregación se pueden combinar con las claúsulas previamente estutemadas. Simplemente tenemos que respetar el orden establecido de las claúsulas.

A la hora de extraer datos de base de datos será muy común que utilicemos las funciones de agregación en conjunto con where.

```
SELECT AVG(columna1) FROM tabla WHERE columna2 < valor
```

Ejercicio
Utilizando la tabla empleados, calcula la suma de sueldos de todas las personas mayores a 27 años

| EMAIL                   | NOMBRE         | EDAD | SUELDO |
|-------------------------|----------------|------|--------|
| juan.perez@workmail.com | Juan Pérez     | 30   | 50,000 |
| maria.gonzalez@corp.com | Maria González | 25   | 55,000 |
| john.doe@techplace.org  | John Doe       | 40   | 60,000 |
| francisco@startup.io    | Francisco      | 22   | 45,000 |


```
select SUM(sueldo) from empleados where edad > 27
```

### Ejercicio 2: Funciones de agregacion con Where
Ejercicio
Utilizando la tabla empleados, calcula el promedio de los sueldos de todas las personas que ganan más de 50,000

| EMAIL                   | NOMBRE         | EDAD | SUELDO |
|-------------------------|----------------|------|--------|
| juan.perez@workmail.com | Juan Pérez     | 30   | 50,000 |
| maria.gonzalez@corp.com | Maria González | 25   | 55,000 |
| john.doe@techplace.org  | John Doe       | 40   | 60,000 |
| francisco@startup.io    | Francisco      | 22   | 45,000 |


```
select AVG(sueldo) from empleados where sueldo > 50000
```
### Ejercicio 3: Funciones de agregacion con where

Ejercicio
Dada la siguiente tabla empleados

| NOMBRE    | APELLIDO  | SUELDO | DEPARTAMENTO     |
|-----------|-----------|--------|------------------|
| Juan      | Pérez     | 3000   | Ventas           |
| María     | González  | 3500   | Marketing        |
| Carlos    | Rodríguez | 4000   | Tecnología       |
| Ana       | Martínez  | 2800   | Recursos Humanos |
| Luis      | García    | 3200   | Finanzas         |
| Carmen    | López     | 3100   | Administración   |
| José      | Hernández | 2900   | Operaciones      |
| Francisco | Martín    | 3400   | Legal            |
| Laura     | Sánchez   | 3300   | Compras          |
| Antonio   | Díaz      | 3600   | Producción       |
| Sofía     | Ruiz      | 2750   | Ventas           |
| Jorge     | Vargas    | 3900   | Tecnología       |
| Elena     | Castro    | 3050   | Marketing        |
| Pedro     | Ortega    | 3150   | Finanzas         |


Calcula cuantas personas trabajan en el area de marketing

```
select count(*) from empleados where departamento = 'Marketing'
```

### Ejercicio 4: Funciones de agregacion con where

Dada la siguiente tabla empleados

| NOMBRE    | APELLIDO  | SUELDO | DEPARTAMENTO     |
|-----------|-----------|--------|------------------|
| Juan      | Pérez     | 3000   | Ventas           |
| María     | González  | 3500   | Marketing        |
| Carlos    | Rodríguez | 4000   | Tecnología       |
| Ana       | Martínez  | 2800   | Recursos Humanos |
| Luis      | García    | 3200   | Finanzas         |
| Carmen    | López     | 3100   | Administración   |
| José      | Hernández | 2900   | Operaciones      |
| Francisco | Martín    | 3400   | Legal            |
| Laura     | Sánchez   | 3300   | Compras          |
| Antonio   | Díaz      | 3600   | Producción       |
| Sofía     | Ruiz      | 2750   | Ventas           |
| Jorge     | Vargas    | 3900   | Tecnología       |
| Elena     | Castro    | 3050   | Marketing        |
| Pedro     | Ortega    | 3150   | Finanzas         |

Calcula cuantas personas trabajan en total en las areas de finanzas y marketing

```
select count(*) from empleados where departamento = "Marketing" or departamento = "Finanzas"
```
### Conteo de condiciones con string

Ejercicio
Se tiene la tabla usuarios con la siguiente información:

| ID | NOMBRE | APELLIDO | EMAIL                    | TELEFONO |
|----|--------|----------|--------------------------|----------|
| 1  | Juan   | Pérez    | juanperez@gmail.com      | 555-1234 |
| 2  | María  | García   | mariagarcia@hotmail.com  | 555-5678 |
| 3  | Pedro  | López    | pedrolopez@yahoo.com     | 555-9876 |
| 4  | Lucía  | Sánchez  | luciasanchez@outlook.com | 555-5555 |
| 5  | Jorge  | Martínez | jorgemartinez@gmail.com  | 555-4321 |

Cuenta la cantidad de usuarios cuyo nombre termina con la letra 'a' en la tabla de usuarios.

```
select count(*) from usuarios where nombre like '%a' 
```
## Tema 8: Distinct

:arrow_up: [ir al inicio](.#tabla-de-contenidos)

### Seleccionar filtrando datos repetidos

En SQL la palabra clave `DISTINCT` nos permite filtrar los resultados repetidos de una consulta

Supongamos que tenemos la siguiente tabla llamada _colores_

| COLOR    |
|----------|
| Rojo     |
| Azul     |
| Verde    |
| Amarillo |
| Rojo     |
| Verde    |
| Rojo     |
| Verde    |
| Rojo     |
| Negro    |
| Blanco   |
| Rojo     |
| Azul     |
| Verde    |
| Amarillo |

Nos piden crear una conculta que nos muestre cada color una unica vez, para esto utilizamos el siguiente comando:

```
SELECT DISTINCT color AS color_unico
FROM colores
```

Ejercicio
Prueba en el editor la misma instrucción aprendida para ver cual sería el resultado de la consulta.

### Seleccionando correor unicos

Ejercicio
Dada la siguiente tabla de usuarios

| CORREO                       |
|------------------------------|
| juan.perez@empresa.com       |
| maria.gonzalez@empresa.com   |
| carlos.rodriguez@empresa.com |
| ana.martinez@empresa.com     |
| luis.garcia@empresa.com      |
| carmen.lopez@empresa.com     |
| jose.hernandez@empresa.com   |
| francisco.martin@empresa.com |
| laura.sanchez@empresa.com    |
| antonio.temaz@empresa.com     |
| juan.perez@empresa.com       |
| maria.gonzalez@empresa.com   |

Crea una consulta que nos muestre cada correo una única vez. La columa mostrada debe llamarse correo_unico

```
select distinct(correo) as correo_unico from usuarios
```

### Seleccionar distintos años

Se tiene la tabla _ventas_ con la sigguiente informaicon:

| ID_VENTA | MONTO | FECHA_VENTA |
|----------|-------|-------------|
| 1        | 200   | 2010-01-15  |
| 2        | 150   | 2011-02-20  |
| 3        | 300   | 2012-04-10  |
| 4        | 250   | 2013-04-05  |
| 5        | 100   | 2014-04-25  |
| 6        | 350   | 2015-06-18  |
| 7        | 400   | 2015-06-22  |
| 8        | 180   | 2015-06-09  |
| 9        | 220   | 2018-07-30  |
| 10       | 275   | 2019-07-11  |

Se nos ha solicitado crear una consulta que muestre los años en los que se han realizado transacciones, excluyendo repeticiones.
Como ya sabemos, [en ejercicios anteriores](.#extraccion-del-año), para obtener el año a partir de la feha de venta,podemos utilizar el siguiente codigo:


```
select strftime('%Y', fecha_venta) as año_venta from ventas
```

Sin embargo, para asegurarnos de obtener años unicos podemos agregar la clausula DISTINCT a nuestra consulta de la siguiente manera:

```
SELECT DISTINCT strftime('%Y', fecha_venta) as año_unico from ventas
```

Ejercicio: Utilizando la tabla ventas, previamente utilizada, selecciona todos los meses distintos, asignamdole a la columna el alias "mes_unico".

```
select distinct strftime('%m', fecha_venta) as mes_unico
from ventas
```

### Contar los valores distintos
Si queremos contar los valores distintos en una columna de una tabla, podemos combinar las funciones COUNT y DISTINCT de la siguiente manera `COUNT(DISTINCT columna)`

Veamos un ejemplo con la siguiente tabla empleados:

| NOMBRE    | APELLIDO  | SUELDO | DEPARTAMENTO     |
|-----------|-----------|--------|------------------|
| Juan      | Pérez     | 3000   | Ventas           |
| María     | González  | 3500   | Marketing        |
| Carlos    | Rodríguez | 4000   | Tecnología       |
| Ana       | Martínez  | 2800   | Recursos Humanos |
| Luis      | García    | 3200   | Finanzas         |
| Carmen    | López     | 3100   | Administración   |
| José      | Hernández | 2900   | Operaciones      |
| Francisco | Martín    | 3400   | Legal            |
| Laura     | Sánchez   | 3300   | Compras          |
| Antonio   | Díaz      | 3600   | Producción       |
| Sofía     | Ruiz      | 2750   | Ventas           |
| Jorge     | Vargas    | 3900   | Tecnología       |
| Elena     | Castro    | 3050   | Marketing        |
| Pedro     | Ortega    | 3150   | Finanzas         |

Podemos contar la cantidad de depetamentos unicos de la empresa con

```
SELECT COUNT(DISTINCT Departamento) FROM Empleados:
```

Ejercicio:

Se tiene la tabla usuarios con la siguiente informacion:

| ID | NOMBRE | APELLIDO | EMAIL                    | TELEFONO |
|----|--------|----------|--------------------------|----------|
| 1  | Juan   | Pérez    | juanperez@gmail.com      | 555-1234 |
| 2  | María  | García   | mariagarcia@hotmail.com  | 555-5678 |
| 3  | Pedro  | López    | pedrolopez@yahoo.com     | 555-5678 |
| 4  | Lucía  | Sánchez  | luciasanchez@outlook.com | 555-5555 |
| 5  | Jorge  | Martínez | jorgemartinez@gmail.com  | 555-5678 |


Crea una consulta que muestre los teléfonos únicos de la tabla. La columna mostrada debe llamarse telefonos_unicos

```
select count(distinct telefono) as telefonos_unicos from usuarios
```

### Contando correos únicos

Ejercicio
Dada la siguiente tabla de usuarios

| CORREO                       |
|------------------------------|
| juan.perez@empresa.com       |
| maria.gonzalez@empresa.com   |
| carlos.rodriguez@empresa.com |
| ana.martinez@empresa.com     |
| luis.garcia@empresa.com      |
| carmen.lopez@empresa.com     |
| jose.hernandez@empresa.com   |
| francisco.martin@empresa.com |
| laura.sanchez@empresa.com    |
| antonio.temaz@empresa.com     |
| juan.perez@empresa.com       |
| maria.gonzalez@empresa.com   |

Crea una consulta para contestar cuantos correos únicos existen en la tabla. La columna resultante debe llamarse correos_cant

```
select count(distinct correo) as correos_cant from usuarios
```

### Distinct con multiples columnas
Podemos usar DISTINCT con más de una columna para obtener combinaciones únicas de esas columnas. Supongamos que tienes una tabla llamada empleados con las columnas departamento y puesto.

Para este ejemplo trabajaremos con la siguiente tabla empleados:

| ID_EMPLEADO | NOMBRE    | DEPARTAMENTO | PUESTO        |
|-------------|-----------|--------------|---------------|
| 1           | Juan      | Ventas       | Vendedor      |
| 2           | María     | Ventas       | Vendedor      |
| 3           | Carlos    | IT           | Desarrollador |
| 4           | Ana       | IT           | Desarrollador |
| 5           | Luis      | Ventas       | Gerente       |
| 6           | Carmen    | IT           | Gerente       |
| 7           | José      | IT           | Desarrollador |
| 8           | Francisco | Ventas       | Vendedor      |

uego podemos obtener todas las combinaciones únicas de Departamento y Puesto utilizando la siguiente consulta:

```
SELECT DISTINCT departamento, puesto FROM empleados;
```

Con esto obtendremos la siguiente tabla resultante.

| DEPARTAMENTO | PUESTO        |
|--------------|---------------|
| Ventas       | Vendedor      |
| IT           | Desarrollador |
| Ventas       | Gerente       |
| IT           | Gerente       |

Ejercicio
Para la siguiente tabla "productos" deseamos obtener todas las combinaciones únicas de "Categoria" y "Precio"

| NOMBRE      | CATEGORIA   | PRECIO |
|-------------|-------------|--------|
| Laptop      | Electrónica | 1000   |
| Teléfono    | Electrónica | 500    |
| Camiseta    | Ropa        | 20     |
| Pantalón    | Ropa        | 40     |
| Auriculares | Electrónica | 50     |
| Libro       | Libros      | 15     |
| Mochila     | Accesorios  | 30     |

```
SELECT DISTINCT categoria, precio
FROM productos
```
## Tema 9: Introducción a grupos
:arrow_up: [ir al inicio](.#tabla-de-contenidos)
### Agrupando valores con GROUUP BY
La clausula GROUP BY es una poderosa gherramienta en SQL que se utilizar para agrupar filas con valores identicos en una o varias columnas especificas, permitiendo realizar operaciones de agregacion en ada grupo.

Esta clausula viene dentro de la categoria de FUNCIONES DE GRUPO, asi como `count`, `sum`, `Average`, etc.

La sintaxis para GROUP BY es 
```
SELECT column1, column2
FROM table_name
GROPU BY column1, column2
```


Ejemplo:

Asumamos que tenemos una tabla llamada "sales". Esta tabla tiene tres columnas: ID, Item, y Ammount



| ID | Item | Amount |
|----|------|--------|
| 1  | A    | 150    |
| 2  | B    | 200    |
| 3  | A    | 100    |
| 4  | B    | 50     |
| 5  | A    | 200    |
| 6  | A    | 100    |
| 7  | B    | 150    |

Ejecutamos el siguiente comando de SQL

```
SELECT item, sum(Amount)
FROM sales
GROUP BY Item;
```

El codigo va a concatenar, o "agrupar" todos los items que sean los mismos a una nueva fila, aplicando la funciion SUM(). La salida será:

| Item | SUM(amount) |
|------|-------------|
| A    | 550         |
| B    | 400         |

Tenemos la siguiente tabla colores:

| COLOR    |
|----------|
| Rojo     |
| Azul     |
| Verde    |
| Amarillo |
| Naranja  |
| Morado   |
| Rosa     |
| Café     |
| Gris     |
| Negro    |
| Blanco   |
| Rojo     |
| Azul     |
| Verde    |
| Amarillo |

Podemos seleccioar los elementos unicos utilizando GROUP BY de la siguiente forma

```
SELECT color as color_unico
FROM colores
GROUP BY color
```

como resultado obtendremos


| COLOR    |
|----------|
| Amarillo |
| Azul     |
| Blanco   |
| Café     |
| Gris     |
| Morado   |
| Naranja  |
| Negro    |
| Rojo     |
| Rosa     |
| Verde    |

Ejercicio:
Dada la siguiente tabla de usuarios:

| CORREO                       |
|------------------------------|
| juan.perez@empresa.com       |
| maria.gonzalez@empresa.com   |
| carlos.rodriguez@empresa.com |
| ana.martinez@empresa.com     |
| luis.garcia@empresa.com      |
| carmen.lopez@empresa.com     |
| jose.hernandez@empresa.com   |
| francisco.martin@empresa.com |
| laura.sanchez@empresa.com    |
| antonio.temaz@empresa.com     |
| juan.perez@empresa.com       |
| maria.gonzalez@empresa.com   |

Crea una consulta que nos muestre cada correo una unica vez. La columna mostrada deberá llamarse `correo_unico`

```
SELECT correo as correo_unico
FROM usuarios
GROUP BY correo
```

### Agrupar y contar
GROUP BY es comunmente utilizada junto con funciones de agregacion como COUNT, MAX, MIN, SUM y AVG para obtener informacion resumida de un conjunto de datos

En este ejrcicio aprenderemos a agrupar y contar

Tenemos la siguiente tabla de colores

| COLOR    |
|----------|
| Rojo     |
| Azul     |
| Verde    |
| Amarillo |
| Naranja  |
| Morado   |
| Rosa     |
| Café     |
| Gris     |
| Negro    |
| Blanco   |
| Rojo     |
| Azul     |
| Verde    |
| Amarillo |


Queremos saber cuantas veces aparece cada color. esto lo podemos lograr combinando GROUP BY y la funcion de agregacion COUNT


```
SELECT color, count(color) as Repeticiones
FROM colores
GROUP BY color
```

| COLOR    | REPETICIONES |
|----------|--------------|
| Amarillo | 2            |
| Azul     | 2            |
| Blanco   | 1            |
| Café     | 1            |
| Gris     | 1            |
| Morado   | 1            |
| Naranja  | 1            |
| Negro    | 1            |
| Rojo     | 2            |
| Rosa     | 1            |
| Verde    | 2            |

Ejercicio

Dada la siguiente tabla de usuarios

| CORREO                       |
|------------------------------|
| juan.perez@empresa.com       |
| maria.gonzalez@empresa.com   |
| carlos.rodriguez@empresa.com |
| ana.martinez@empresa.com     |
| luis.garcia@empresa.com      |
| carmen.lopez@empresa.com     |
| jose.hernandez@empresa.com   |
| francisco.martin@empresa.com |
| laura.sanchez@empresa.com    |
| antonio.temaz@empresa.com     |
| juan.perez@empresa.com       |
| maria.gonzalez@empresa.com   |


Crea una consulta que nos muestre cada correo electronico una unica vez junto a la cantidad de repeticiones. LAs columnas deben llamarse correo y repeticiones

```
SELECT correo, count(correo) as repeticiones
from usuarios
group by correo
```

### Ejercitando agrupar y contar

Ejercicio
Dada la siguiente tabla empleados

| NOMBRE    | APELLIDO  | SUELDO | DEPARTAMENTO     |
|-----------|-----------|--------|------------------|
| Juan      | Pérez     | 3000   | Ventas           |
| María     | González  | 3500   | Marketing        |
| Carlos    | Rodríguez | 4000   | Tecnología       |
| Ana       | Martínez  | 2800   | Recursos Humanos |
| Luis      | García    | 3200   | Finanzas         |
| Carmen    | López     | 3100   | Administración   |
| José      | Hernández | 2900   | Operaciones      |
| Francisco | Martín    | 3400   | Legal            |
| Laura     | Sánchez   | 3300   | Compras          |
| Antonio   | Díaz      | 3600   | Producción       |
| Sofía     | Ruiz      | 2750   | Ventas           |
| Jorge     | Vargas    | 3900   | Tecnología       |
| Elena     | Castro    | 3050   | Marketing        |
| Pedro     | Ortega    | 3150   | Finanzas         |

Se pide contar cuantas personas trabajan en cada departamento. Las columnas resultantes deben llamarse departamento y cantidad_empleados

```
SELECT departamento, count(departamento) as cantidad_empleados
from empleados
group by departamento
```

### Agrupar y sumar
En este ejercicio agruparemos y sumaremos. La logica de la consulta es la misma previamente mencionada, solo cambia la funcin de agrupacion a utilizar. Por ejemplo, tenemos una tabla de pedidos con los siguientes datos:

| CLIENTE   | MONTO |
|-----------|-------|
| Cliente A | 1200  |
| Cliente A | 800   |
| Cliente B | 150   |
| Cliente C | 200   |
| Cliente B | 90    |

Si queremos calcular cuanto ha gastado cada cliente, podemos realizar la siguiente consulta:

```
SELECT Cliente, sum(Monto) as Monto_total
FROM pedidos
GrOUP BY Cliente
```

Ejercicio
Utilizando la siguiente tabla ventas e una empresa, crea una consulta que muestre cuanto vendio en total por cada categoria. Las columnas de la consulta deben llamarse categoria y monto_total

| PRODUCTO        | MONTO | CATEGORIA         |
|-----------------|-------|-------------------|
| Laptop Pro      | 1200  | Electrónicos      |
| Smartphone X    | 800   | Electrónicos      |
| Silla Ergo      | 150   | Mobiliario        |
| Mesa de Café    | 90    | Mobiliario        |
| Reloj Elegante  | 250   | Accesorios        |
| Bolso de Viaje  | 70    | Accesorios        |
| Zapatillas Run  | 100   | Ropa              |
| Camisa Casual   | 40    | Ropa              |
| Licuadora Max   | 60    | Electrodomésticos |
| Horno Compacto  | 110   | Electrodomésticos |
| Libro de Cocina | 20    | Libros            |
| Novela Misterio | 15    | Libros            |
| Audífonos Plus  | 50    | Electrónicos      |
| Lámpara Moderna | 45    | Mobiliario        |
| Laptop Pro      | 1200  | Electrónicos      |
| Silla Ergo      | 150   | Mobiliario        |
| Bolso de Viaje  | 70    | Accesorios        |
| Zapatillas Run  | 100   | Ropa              |

```
SELECT categoria as categoria, sum(monto) as monto_total
FROM ventas
group by categoria
```
### Agruopar y prometemar

Previamente aprendimos que AVG nos permite calcular el promedio de los elementos de una columna en una tabla. En este ejercicio lo utilizaremos para calcular promedios po grupo.

```
SELECT grupo, AVG(columna)
FROM tabla
GROUP BY grupo
```

Ejercicio

Dada la siguiente tabla de estutemantes


| NOMBRE_COMPLETO | NOTA |
|-----------------|------|
| Juan Pérez      | 7    |
| Juan Pérez      | 8    |
| Juan Pérez      | 6    |
| María Rodríguez | 9    |
| María Rodríguez | 7    |
| María Rodríguez | 8    |
| Carlos García   | 6    |
| Carlos García   | 5    |
| Carlos García   | 7    |
| Ana Fernández   | 8    |
| Ana Fernández   | 9    |
| Ana Fernández   | 8    |
| Luis Morales    | 7    |
| Luis Morales    | 6    |
| Luis Morales    | 5    |

Encuentra el promedio de notas de cada estutemante. Las columnas deben tener el nombre completo y promedio_notas respectivamente

Este ejercicio tiene un supuesto importante, que no hay dos estutemantes con el mismo nombre y apellido. DIscutiremos este tipo de supuestos mas adelante cuando revisemos el concepto de integridad.

```
SELECT nombre_completo, AVG(nota) as promedio_notas
FROM estutemantes
GROUP BY nombre_completo
```

### Maximo por grupo
En este ejercicio combinaremos la funcion de agregacion MAX() con GROUP BY para poder obtener el monto mas alto de cada grupo. LA sintaxis de la consulta será igual a las vistas previamente, es decir:

```
SELECT grupo. MAX(columna)
FROM tabla
GROUP BY grupo
```


Ejercicio:

Dada la siguiente tabla de ventas

| PRODUCTO        | MONTO | CATEGORIA         |
|-----------------|-------|-------------------|
| Laptop Pro      | 1200  | Electrónicos      |
| Smartphone X    | 800   | Electrónicos      |
| Silla Ergo      | 150   | Mobiliario        |
| Mesa de Café    | 90    | Mobiliario        |
| Reloj Elegante  | 250   | Accesorios        |
| Bolso de Viaje  | 70    | Accesorios        |
| Zapatillas Run  | 100   | Ropa              |
| Camisa Casual   | 40    | Ropa              |
| Licuadora Max   | 60    | Electrodomésticos |
| Horno Compacto  | 110   | Electrodomésticos |
| Libro de Cocina | 20    | Libros            |
| Novela Misterio | 15    | Libros            |
| Audífonos Plus  | 50    | Electrónicos      |
| Lámpara Moderna | 45    | Mobiliario        |
| Laptop Pro      | 1200  | Electrónicos      |
| Silla Ergo      | 150   | Mobiliario        |
| Bolso de Viaje  | 70    | Accesorios        |
| Zapatillas Run  | 100   | Ropa              |

Crea una consulta para calcular el monto mas alto por cada categoria. La tabla resultante debe tener dos columnas: categoria y monto_mas_alto

```
SELECT categoria, max(monto) as monto_mas_alto
FROM ventas
group by categoria
```
### Minimo por grupo
En este ejercicio combinaremos la funcion MIN() con GROUP BY para obtener el monto mas bajo de cada grupo. La sintaxis de la consulta será igual a las vistas previamente, es decir:

```
SELECT grupo, MIN(columna) FROM tabla GROPU BY grupo
```

Ejercicio:

Dada la tabla *ventas*

| PRODUCTO        | MONTO | CATEGORIA         |
|-----------------|-------|-------------------|
| Laptop Pro      | 1200  | Electrónicos      |
| Smartphone X    | 800   | Electrónicos      |
| Silla Ergo      | 150   | Mobiliario        |
| Mesa de Café    | 90    | Mobiliario        |
| Reloj Elegante  | 250   | Accesorios        |
| Bolso de Viaje  | 70    | Accesorios        |
| Zapatillas Run  | 100   | Ropa              |
| Camisa Casual   | 40    | Ropa              |
| Licuadora Max   | 60    | Electrodomésticos |
| Horno Compacto  | 110   | Electrodomésticos |
| Libro de Cocina | 20    | Libros            |
| Novela Misterio | 15    | Libros            |
| Audífonos Plus  | 50    | Electrónicos      |
| Lámpara Moderna | 45    | Mobiliario        |
| Laptop Pro      | 1200  | Electrónicos      |
| Silla Ergo      | 150   | Mobiliario        |

Crea una consulta para calcular el monto mas bajo por cada grupo. La tabla resultante debe tener dos columnas `categoria` y `monto_mas_bajo`

```
SELECT categoria, min(monto) AS monto_mas_bajo 
FROM ventas
GROUP BY categoria
```

### Funciones de agregacion y fechas
A la hora de construir informes, frecuentemente necesitaremos entregar informacion agrupada en un periodo de tiempo. Para lograr esto, utilizaremos una combinacion de GROUP BY con la funciuon strftime.

Tenemos la tabla *ventas* con la siguiente informacion:

| ID_VENTA | MONTO | FECHA_VENTA |
|----------|-------|-------------|
| 1        | 200   | 2010-01-15  |
| 2        | 150   | 2011-02-20  |
| 3        | 300   | 2012-03-10  |
| 4        | 250   | 2012-04-05  |
| 5        | 100   | 2014-05-25  |
| 6        | 350   | 2015-06-18  |
| 7        | 400   | 2015-07-22  |
| 8        | 180   | 2015-08-09  |
| 9        | 220   | 2018-09-30  |
| 10       | 275   | 2018-10-11  |

Se nos solicita determinar el monto total de ventas por año. Para resolverlo, tenemos qye agrupar por fecha y sumar los montos de la siguiente manera:

```
SELECT sum(monto), strftime("%Y"), fecha_venta AS año 
FROM ventas 
GROUP BY strftime("%Y", fecha_venta)
```


Ejercicio:
Utilizando esta nueva tabla de ventas

| ID_VENTA | MONTO | FECHA_VENTA |
|----------|-------|-------------|
| 1        | 200   | 2010-01-15  |
| 2        | 150   | 2010-02-20  |
| 3        | 300   | 2010-02-10  |
| 4        | 250   | 2010-04-05  |
| 5        | 100   | 2010-04-25  |
| 6        | 350   | 2010-04-18  |
| 7        | 400   | 2010-06-22  |
| 8        | 180   | 2010-06-09  |
| 9        | 220   | 2010-09-30  |
| 10       | 275   | 2010-10-11  |


Calcule el total de venta por mes El nombre de las columnas resultantes será "suma_ventas" y "mes" respectivamente.


```
SELECT sum(monto) as suma_ventas, strftime("%m", fecha_venta) as mes
FROM ventas
GROUP BY strftime("%m", fecha_venta)
```

### Ejercitando funciones de agregacion con fechas

Se tiene una tabla llamada _inscripciones_ con distintas fechas de inscrpciones de un usuario a un sitio web

| FECHA_INSCRIPCION |
|-------------------|
| 2022-01-15        |
| 2022-01-20        |
| 2022-02-10        |
| 2022-02-05        |
| 2022-03-25        |
| 2022-03-18        |
| 2022-04-22        |
| 2022-04-09        |
| 2022-05-30        |
| 2022-05-11        |
| 2022-06-19        |
| 2022-06-29        |
| 2022-07-12        |
| 2022-07-21        |
| 2022-08-08        |
| 2022-08-17        |
| 2022-09-13        |
| 2022-09-26        |
| 2022-10-14        |
| 2022-10-28        |

Cuenta cuantos usuarios se registraron cada mes. Las columnas resultantes deben llamarse "mes" y "cantidad_usuarios"

```
SELECT strftime("%m", fecha_inscripcion) as mes,  COUNT(Fecha_Inscripcion) AS cantidad_usuarios
FROM inscripciones
GROUP BY strftime("%m", fecha_inscripcion)
```

### Agrupando sin indicar el nombre de las columnas
Cuando se trata de agrupar datos e una consulta SQL, existe una forma de evitar la redundancia de la clausula SELECT. POr ejemplo, considera la siguiente consulta

```
SELECT stfrtime("%Y", fecha_venta) as año_venta, sum(monto) from ventas group by strftime("%Y", fecha_venta)
```

Podemos simplificarla de la siguiente manera

```
SELECT strftime("%Y", fecha_venta) AS año, SUM(monto)
FROM ventas
GROUP BY 1
```

En esta notacion se interpreta como "agrupa por el primer criterio". TAmbien es posible aplicar esta sintaxis en la clausula ORDEB BY

```
SELECT strftime("%Y", fecha_venta) AS año, SUM(monto)
FROM ventas 
GROUP BY 1
ORDER BY 1

```

De esta manera podemos lograr la agrupacion y ordenamiento sin repetir la expresion de la clausula SELECT

Ejercicio:
Dada la siguiente tabla de usuarios

| CORREO                       |
|------------------------------|
| juan.perez@empresa.com       |
| maria.gonzalez@empresa.com   |
| carlos.rodriguez@empresa.com |
| ana.martinez@empresa.com     |
| luis.garcia@empresa.com      |
| carmen.lopez@empresa.com     |
| jose.hernandez@empresa.com   |
| juan.perez@empresa.com       |
| carmen.lopez@empresa.com     |
| maria.gonzalez@empresa.com   |
| juan.perez@empresa.com       |
| maria.gonzalez@empresa.com   |

Crea una consulta que nos muestre cada correo una unica vez, acompañado del momento de veces que se repite. Las columnas deben llevar los nombres "correo" "repeticiones", respectivamente y deben estar ordenados alfabeticamente

```
SELECT correo, count(correo) as repeticiones
FROM usuarios
GROUP BY 1
ORDER BY 1 asc
```

### Agrupando por multiples columnas
En SQL es posible agrupas por multipes columnas utilizando la siguiente sintaxis

```
SELECT columna1, columna2 funcion_agrupado(columna3)
FROM tabla
GROUP BY columna1, columna2
```

Y como aprendimos en el ejerciio anterior, tambien podemos escribir la consulta de la siguiente manera:

```
SELECT columna1, columna2, funcion_agrupado(columna3)
FROM tabla
GROUP BT 1, 2
```

Ejercicio
Tenemos la siguiente tabla estutemantes

| CORREO                  | MATERIA     | NOTA |
|-------------------------|-------------|------|
| estutemante1@ejemplo.com | Matemáticas | 8.5  |
| estutemante2@ejemplo.com | Matemáticas | 9.0  |
| estutemante3@ejemplo.com | Matemáticas | 7.5  |
| estutemante1@ejemplo.com | Ciencias    | 8.0  |
| estutemante2@ejemplo.com | Ciencias    | 9.5  |
| estutemante3@ejemplo.com | Ciencias    | 7.0  |
| estutemante1@ejemplo.com | Historia    | 8.7  |
| estutemante2@ejemplo.com | Historia    | 9.2  |
| estutemante3@ejemplo.com | Historia    | 7.8  |

Calcula el promedio de cada estutemante en cada materia. LAs columnas deben llamarse correo, materi y promedio_notas

```
SELECT correo, materia, AVG(nota) as promedio_notas
FROM estutemantes
group by 1,2
```
## Tema 10: HAVING

:arrow_up: [ir al inicio](.#tabla-de-contenidos)

### Introduccion a `HAVING`
`HAVING` es una clausula de SQL que nos permite filtrar conjuntos de resultados en una clausula `GROUP BY`.  Se utiliza para mencionar condiciones sobre grupos que se seleccionan. En otras palabras, HAVING se utiliza principalmente con la clausula GROUP BY para filtrar los resultados que devuelve un GROUP BY

Es similar a una clausula WHERE,pero opera sobre los resultados de una agrupacion. La clausula WHERE condiciona las columnas, mientras que la clausula HAVING condiciona los grupos creaod por la clausula GROUP BY.

HAVING se emplea para filtrar los resultados de una consulta que involucra funciones agregadas. EN otras palabras, HAVING permite aplicar condiciones de filtrado a los resultados de funciones como COUNT, MIN, MAX, SUM y AVG despues de que se han agrupado los datos con la clausula GROUP BY

Por ejemplo, si tenemos la siguiente tabla de inscripciones:

| FECHA_INSCRIPCION |
|-------------------|
| 2022-01-15        |
| 2022-01-20        |
| 2022-02-10        |
| 2022-02-05        |
| 2022-03-25        |
| 2022-03-18        |
| 2022-04-22        |
| 2022-04-09        |
| 2022-05-30        |
| 2022-05-11        |
| 2022-06-19        |
| 2022-06-29        |
| 2022-07-12        |
| 2022-07-21        |
| 2022-08-08        |
| 2022-08-17        |
| 2022-09-13        |
| 2022-09-26        |
| 2022-10-14        |
| 2022-10-28        |

Nos piden crear un reporte mostrando los meses y la cantidad de inscruitos pero solo donde haya 2 o mas inscritos

```
SELECT strftime("%m", Fecha_Inscripcion) as mes, count(fecha_inscripcion) as cantidad_usuarios
FROM inscripciones
GROUP BY strftime("%m", Fecha_Inscripcion)
HAVING cantidad_usuarios > 2
```

En esta consulta, primero utilizamos GROUP BY para agrupar por mes. Luego utilizamos la funcion de COUNT(Fecha_Inscripcion) ára contar la cantidad de inscritps. Despues de haber agrupado los datos y calculado el total de inscritos, aplicamos la clausula HAVING para filtrar los resultados

Ejercicio:
Crea un reporte mostrando los meses y la cantidad de inscritos pero solo donde haya 1 inscrito. Las columnas deben llamarse mes y cantidad_usuarios, respectivamente.

```
SELECT strftime("%m", fecha_inscripcion) as mes, count(fecha_inscripcion) as cantidad_usuarios
FROM inscripciones
GROUP BY 1
HAVING cantidad_usuarios == 1
```

### Buscando duplicados
Uno de los usos mas recurrentes de HAVING es buscar duplicados. POr ejemplo, dada una tabla de correos, ver cuales estan mas de una vez

Ejercicio

Se tiene la tabla correos_corporativos

| CORREO                       |
|------------------------------|
| juan.perez@empresa.com       |
| maria.gonzalez@empresa.com   |
| carlos.rodriguez@empresa.com |
| ana.martinez@empresa.com     |
| luis.garcia@empresa.com      |
| carmen.lopez@empresa.com     |
| jose.hernandez@empresa.com   |
| francisco.martin@empresa.com |
| laura.sanchez@empresa.com    |
| antonio.temaz@empresa.com     |
| juan.perez@empresa.com       |
| maria.gonzalez@empresa.com   |

Muestra los correos que aparezcan en mas de una ocasion. LA tabla debe tener dos culumnas, una llamada correo y otra llamada cunta_correos que muestra la cantidad de repeticiones correspondiente a cada correo:

```
SELECT correo, count(correo) as cuenta_correos
FROM correos_corporativos
GROUP BY correo
HAVING cuenta_correos > 1
```

### HAVING y cuenta
Ejercicio
Dada la siguiente tabla empleados

| NOMBRE    | APELLIDO  | SUELDO | DEPARTAMENTO     |
|-----------|-----------|--------|------------------|
| Juan      | Pérez     | 3000   | Ventas           |
| María     | González  | 3500   | Marketing        |
| Carlos    | Rodríguez | 4000   | Tecnología       |
| Ana       | Martínez  | 2800   | Recursos Humanos |
| Luis      | García    | 3200   | Finanzas         |
| Carmen    | López     | 3100   | Administración   |
| José      | Hernández | 2900   | Operaciones      |
| Francisco | Martín    | 3400   | Legal            |
| Laura     | Sánchez   | 3300   | Compras          |
| Antonio   | Díaz      | 3600   | Producción       |
| Sofía     | Ruiz      | 2750   | Ventas           |
| Jorge     | Vargas    | 3900   | Tecnología       |
| Elena     | Castro    | 3050   | Marketing        |
| Pedro     | Ortega    | 3150   | Finanzas         |

Crea una consulta que muestre la cantidad de usuarios y el departamento en donde haya mas de un empleado. Las columnas deben llamarse cantidad_de_usuarios y departamento, respectivamente.

```
select count(departamento) AS CANTIDAD_DE_USUARIOS, departamento
FROM empleados
GROUP BY 2
HAVING cantidad_de_usuarios > 1
```

### Having y promedio
Ejercicio
Se tiene la siguiente tabla notas

| EMAIL               | NOTAS |
|---------------------|-------|
| Alumno1@ejemplo.com | 90    |
| Alumno1@ejemplo.com | 50    |
| Alumno1@ejemplo.com | 30    |
| Alumno2@ejemplo.com | 90    |
| Alumno2@ejemplo.com | 20    |
| Alumno3@ejemplo.com | 80    |
| Alumno2@ejemplo.com | 50    |
| Alumno3@ejemplo.com | 30    |
| Alumno3@ejemplo.com | 10    |

Crea una consulta para determinar cuales son los estutemantes que aprobaron. El criterio de aprobacion es promedio_de_notas >= 50

LAs columnas a mostrar deben ser email y promedio_notas

```
SELECT email, AVG(notas) as promedio_notas
from notas
GROUP BY 1
HAVING promedio_notas >= 50
```

### Having y Order
Una vez qye hemos agrupado datos utilizando la clausula GROUP BY, es comun que necesitemos ordenar estos grupos segun algun criterio especifico. POr lo general, queremos ordenar los grupos en funcion de alguna metrica agregada, como la suma, el conteo, el promedio, etc. Para hacer esto, utilizamos la clausula ORDER BY junto con las funciones de agregacion.

El orden de las clausulas en una sonculta debe ser la siguiente:

```
| ORDEN | CLAUSULA | DESCRIPCIÓN                                                    |
|-------|----------|----------------------------------------------------------------|
| 1     | SELECT   | Especifica las columnas que se deben retornar en el resultado. |
| 2     | FROM     | Especifica las tablas de las cuales se extraerán los datos.    |
| 3     | WHERE    | Filtra registros antes de cualquier agregación o agrupación.   |
| 4     | GROUP BY | Agrupa registros por una o más columnas.                       |
| 5     | HAVING   | Filtra registros después de la agregación.                     |
| 6     | ORDER BY | Ordena los registros retornados por una o más columnas.        |
| 7     | LIMIT    | Limita el número de registros retornados.                      |
```

Ejercicio

Dada la siguiente tabña **ventas** , escribe una consulta SQL para obtener los productos que se han vendido en una cantidad total mayor a 1000, ordenados en orden descendente de cantidad vendida

| PRODUCTO | CANTIDAD |
|----------|----------|
| A        | 500      |
| B        | 2000     |
| C        | 300      |
| D        | 1500     |
| E        | 700      |
| A        | 600      |
| B        | 800      |
| C        | 1200     |
| D        | 400      |
| E        | 300      |

La tabla resultante debe tener dos columnas "producto" y "cantidad_total"

```
SELECT producto, sum(cantidad) as cantidad_total
from ventas
GROUP BY 1
HAVING cantidad_total > 1000
ORDER BY cantidad_total desc
```


### Having y Orden 2
Ejercicio
Supongamos que tiene una tabla de empleados con los siguientes datos:

| ID_EMPLEADO | NOMBRE | DEPARTAMENTO | SALARIO |
|-------------|--------|--------------|---------|
| 1           | Juan   | Ventas       | 3000    |
| 2           | Maria  | Marketing    | 3500    |
| 3           | Carlos | Ventas       | 4000    |
| 4           | Ana    | Marketing    | 2800    |
| 5           | Luis   | Ventas       | 3200    |

Tu tarea es escribir una consulta SQL que regrese los departamentos cuyo salario promedio es mayor a 3000, ordenados de mayor a menor salario promedio. Los resultados deben mostrar el nombre del departamento y el salario promedio, con los nombres de las columnas como departamento y salario_promedio, respectivamente

```
SELECT departamento, AVG(salario) as salario_promedio
FROM empleados
GROUP BY 1
HAVING salario_promedio > 3000
ORDER BY salario_promedio desc
```

RESULTADO

| DEPARTAMENTO | SALARIO_PROMEDIO |
|--------------|------------------|
| Ventas       | 3400             |
| Marketing    | 3150             |

## Tema 11: Subconsultas

:arrow_up: [ir al inicio](.#tabla-de-contenidos)

### Instroduccion a subconsultas
Las subconsultas, tambien conocidas como "subqueries", nos permiten utilizar los resultados de una consulta dentro de otra consulta.
En SQL, una subconculta es una consulta integrada dentro de otra consulta SQL. Alternativamente, ouede llamarla _consulta anidada_ o _interna_. La consulta contenedora a menudo se denomina _consulta externa_. LAs subconsultas se utilizan para recuperar datos que se utilizarán en la consulta principal como condicion oara restringir aun mas los datos que se recuperarán.

Las subconsultas se pueden utilizar en varias partes de una consulta, que incluyen
* SELECT clause
* FROM clause
* WHERE clause
* GROUP BY clause
* HAVING clause

SINTAXIS:
En general, la sintaxis se ouede escribir como:
```
SELECT column_name [, column_name]
FROM   table1 [, table2 ]
WHERE  column_name OPERATOR
   (SELECT column_name [, column_name]
   FROM table1 [, table2 ]
   [WHERE]
```

### Tipos de subconsultas
* Subconsulta Escalar: devuelve un valor único.
  Una subconsulta escalar es una consulta que devuelve exactemente una columna con un unnico valor. Este tipo de subconsulta se puede utilizar en cualquier lugar de su SQL donde se permitan expresiones
  Sintaxis:
  ```
  SELECT column_name [, column_name ]
    FROM   table1 [, table2 ]
    WHERE  column_name operator
           (SELECT column_name [, column_name ]
            FROM table_name 
            WHERE condition);
  ```
  Ejemplo:
  ```
  SELECT name 
  FROM student 
  WHERE roll_id = (SELECT roll_id FROM student WHERE name='John');
  ```
* Subconsulta de fila: devuelve una sola fila o varias filas de dos o mas valores.
  Las subconsultas de filas se utilizaan para devolver una o mas filas a la consulta de seleccion SQL. Sin embargo, la subconsulta deuelve varias columnas y filas, por lo tanto no se puede usar directamente donde se utilizarn expresiones escalares.
  Sintaxis:
  ```
  SELECT column_name [, column_name ]
    FROM   table1 [, table2 ]
    WHERE  (column_name [, column_name ])
          IN (SELECT column_name [, column_name ]
              FROM table_name 
              WHERE condition);
  ```
  Ejemplo:
  ```
  SELECT * FROM student 
  WHERE (roll_id, age)=(SELECT MIN(roll_id),MIN(age) FROM student);
  ```
* Subconsulta de columna: devuelve un valor de una sola columna que es mas de una fila y una columna
  Las subconsultas de columnas se utilizan para devolver una o mas columnas a la consulta de seleccion SQL externa. Se utilizan cuando se espera que la subconsulta devuelva mas de una columna a la consulta principal.
  Sintaxis:
  ```
  SELECT column_name [, column_name ]
    FROM   table1 [, table2 ]
    WHERE  (SELECT column_name [, column_name ]
            FROM table_name 
            WHERE condition);
  ```
  Ejemplo:
  ```
  SELECT name, age FROM student 
  WHERE name=(SELECT name FROM student);
  ```
* Subconsulta de tabla: devuelve mas de una fila y mas de una columna.
  Las subconsultas de tabla se utilizan en la clausula FROM y devuelven una tabla que se puede utilizar como referencia de tabla en una declaracion SQL. Resultan utiles cuando desea realizar operaciones como unir varias tablas, unir datos de multiples fuentes, etc.
  Sintaxis:
  ```
  SELECT column_name [, column_name ]
    FROM
        (SELECT column_name [, column_name ]
         FROM   table1 [, table2 ])
    WHERE  condition;
  ```
  Ejemplo:
  ```
  SELECT name, age 
  FROM student 
  WHERE (name, age) IN (SELECT name, age FROM student);
  ```

Veamos un ejemplo practico:

Dada la tabla **Empleados**

| NOMBRE    | APELLIDO  | SUELDO | DEPARTAMENTO     |
|-----------|-----------|--------|------------------|
| Juan      | Pérez     | 3000   | Ventas           |
| María     | González  | 3500   | Marketing        |
| Carlos    | Rodríguez | 4000   | Tecnología       |
| Ana       | Martínez  | 2800   | Recursos Humanos |
| Luis      | García    | 3200   | Finanzas         |
| Carmen    | López     | 3100   | Administración   |
| José      | Hernández | 2900   | Operaciones      |
| Francisco | Martín    | 3400   | Legal            |
| Laura     | Sánchez   | 3300   | Compras          |
| Antonio   | Díaz      | 3600   | Producción       |
| Sofía     | Ruiz      | 2750   | Ventas           |
| Jorge     | Vargas    | 3900   | Tecnología       |
| Elena     | Castro    | 3050   | Marketing        |
| Pedro     | Ortega    | 3150   | Finanzas         |

Se nos pide seleccionar a todas las personas que ganan sobre el promedio.

Este tipo de preguntas podemos contestarlas utilizando subconsultas

La idea para contestar esto es la siguiente:

1. Calculamos el promedio `SELECT AVG(sueldo) FROM empleados`
2. Seleccionamos todos los empleados cuyo  sueldo es mayor a la consulta anterior `SELECT * FROM empleados WHERE sueldo > (SELECT AVG(sueldo) FROM empleados)`
3. 
Ejercicio:
Utilizando los mismos datos de la tabla **Empleados**, selecciona todos los registros cuyo sueldo sea menor o igual al promedio

```
SELECT * 
FROM empleados 
WHERE sueldo <= (SELECT AVG(sueldo) FROM empleados)
```

### Subconsultas y Where parte 1
Dentro de las subconsultas, podemos utilizar las mismas clausulas que hemos aprendido hasta ahora, como la clausula WHERE. Esto significa que podemos aplicar la clausula WHERE tanto dentro de la subconsulta como fuera de ella.

Ejercicio:

Dada la siguiente tabla **empleados**

| NOMBRE    | APELLIDO  | SUELDO | DEPARTAMENTO     |
|-----------|-----------|--------|------------------|
| Juan      | Pérez     | 3000   | Ventas           |
| María     | González  | 3500   | Marketing        |
| Carlos    | Rodríguez | 4000   | Tecnología       |
| Ana       | Martínez  | 2800   | Recursos Humanos |
| Luis      | García    | 3200   | Finanzas         |
| Carmen    | López     | 3100   | Administración   |
| José      | Hernández | 2900   | Operaciones      |
| Francisco | Martín    | 3400   | Legal            |
| Laura     | Sánchez   | 3300   | Compras          |
| Antonio   | Díaz      | 3600   | Producción       |
| Sofía     | Ruiz      | 2750   | Ventas           |
| Jorge     | Vargas    | 3900   | Tecnología       |
| Elena     | Castro    | 3050   | Marketing        |
| Pedro     | Ortega    | 3150   | Finanzas         |

Selecciona  toda la informacion de los registros que sean mayores al promedio del departamentod de finanzas

Tip:
* Se pide el promedio exclusivamente del departamento de finanzas por lo que no jhay necesidad de agrupar los datos.
* Para este tipo de problema, usualmente hay mas de una solucion.


```
SELECT * 
FROM empleados 
WHERE sueldo > (SELECT AVG(sueldo) FROM empleados where departamento = "Finanzas")
```

### Subconsultas y where parte 2
Ejercicio

| NOMBRE    | APELLIDO  | SUELDO | DEPARTAMENTO     |
|-----------|-----------|--------|------------------|
| Juan      | Pérez     | 3000   | Ventas           |
| María     | González  | 3500   | Marketing        |
| Carlos    | Rodríguez | 4000   | Tecnología       |
| Ana       | Martínez  | 2800   | Recursos Humanos |
| Luis      | García    | 3200   | Finanzas         |
| Carmen    | López     | 3100   | Administración   |
| José      | Hernández | 2900   | Operaciones      |
| Francisco | Martín    | 3400   | Legal            |
| Laura     | Sánchez   | 3300   | Compras          |
| Antonio   | Díaz      | 3600   | Producción       |
| Sofía     | Ruiz      | 2750   | Ventas           |
| Jorge     | Vargas    | 3900   | Tecnología       |
| Elena     | Castro    | 3050   | Marketing        |
| Pedro     | Ortega    | 3150   | Finanzas         |

Utilizando los datos de la tabla **empleados** selecciona todos los empleados cuyo sueldo sea mayotr al empleado que tiene el mayor sueldo del departamento de finanzas

```
SELECT * 
FROM empleados 
WHERE sueldo > (SELECT MAX(sueldo) FROM empleados WHERE departamento = "Finanzas")
```

### Subconsultas y where parte 3
Ejercicio
Se tiene la tabla notas

| EMAIL               | NOTAS |
|---------------------|-------|
| Alumno1@ejemplo.com | 90    |
| Alumno1@ejemplo.com | 50    |
| Alumno1@ejemplo.com | 30    |
| Alumno2@ejemplo.com | 90    |
| Alumno2@ejemplo.com | 20    |
| Alumno3@ejemplo.com | 80    |
| Alumno2@ejemplo.com | 50    |
| Alumno3@ejemplo.com | 30    |
| Alumno3@ejemplo.com | 10    |

Seleccionando todos los registros superiores al promedio de nota

```
SELECT * 
FROM notas 
WHERE notas > (SELECT AVG(notas) FROM notas)
```

### Subconsultas con **IN**
El operador IN es un operador muy util en subconsultas. PAra entenderlo, primero probaremos una consulta sencilla utilizandolo directamente sin subconsultas.

| PAÍS           | CÓDIGO TELÉFONO |
|----------------|-----------------|
| Argentina      | +54             |
| Brasil         | +55             |
| Chile          | +56             |
| Colombia       | +57             |
| España         | +34             |
| Estados Unidos | +1              |
| México         | +52             |

Queremos seleccionar todos los codigos de Argentina, Brasil, Chile o Colombia. UNa forma de abordar el problema seria combinar todas las opciones con where y multiples operadores _or_. Otra opcion es utilizando el operador IN de la siguiente manera:

```
SELECT *
FROM paises
WHERE pais IN ('Argentina', 'Brasil', 'Chile', 'Colombia')
```

De la misma forma podemos hacer una consulta como la siguiente

```
SELECT *
FROM table
WHERE pais IN (SELECT * from otra tabla)
```

Operador IN en subconsultas:

Se tiene la siguiente tabla de estutemantes

| ESTUDIANTE_ID | NOMBRE |
|---------------|--------|
| 1             | Juan   |
| 2             | María  |
| 3             | Pedro  |
| 4             | Ana    |

y la tabla de notas

| ESTUDIANTE_ID | PROMEDIO_NOTAS |
|---------------|----------------|
| 1             | 85             |
| 2             | 65             |
| 3             | 49             |
| 4             | 38             |

Se nos pide mostar los nombres de todas las personas que tengan un promedio de notas menor que 50.

1. Seleccionamos los IDs de la tabla notas con promedio_notas <= 50
2. Seleccionamos los nombres de la tabla _estutemantes_ cuyo id este dentro de la subconsulta anterior


```
SELECT nombre from estutemantes
WHERE estutemante_id IN (SELECT estutemante_id from notas where promedio_notas <= 50)
```

Ejercicio
Se tiene una tabla estutemantes con un código y un nombre

| ESTUDIANTE_ID | NOMBRE |
|---------------|--------|
| 1             | Juan   |
| 2             | María  |
| 3             | Pedro  |
| 4             | Ana    |

Y se tiene una tabla _promedios_ con el codigo dek estutemante y su promedio de notas

| ESTUDIANTE_ID | PROMEDIO_NOTAS |
|---------------|----------------|
| 1             | 85             |
| 2             | 65             |
| 3             | 49             |
| 4             | 38             |

Muestra los nombres de todos los estutemantes que tengan un promedio denotas sobre 50.

Tip:
1. No necesitas agrupar ni prometemar ni contar.
2. Hay mas de una forma de resolver este ejercicio, no te adelantes a joins e intenta resolverlo utilizando subqueries.


```
SELECT nombre
FROM estutemantes
WHERE estutemante_id IN (SELECT estutemante_id from promedios where promedio_notas > 50)
```

### Subconsultas con IN parte 2
Ejercicio
Se tiene la tabla Libros

| LIBRO_ID | NOMBRE               |
|----------|----------------------|
| 1        | La Odisea            |
| 2        | Cien Años de Soledad |
| 3        | El Principito        |
| 4        | Moby Dick            |

Y se tiene la tabla **valoraciones**

| LIBRO_ID | VALORACION_PROMEDIO |
|----------|---------------------|
| 1        | 4.5                 |
| 2        | 4.7                 |
| 3        | 4.2                 |
| 4        | 3.9                 |

Crea una consulta que muestren todos los titulos con valoracion promedio > 4. La columna resultante debe llamarse nombres_seleccionados

```
SELECT nombre as nombres_seleccionados
FROM libros
Where libro_id IN (SELECT libro_id FROM valoraciones WHERE valoracion_promedio > 4)
```

### Subconsultas con IN parte 3

Ejercicio

Se tiene una tabla de **pacientes**

| PACIENTE_ID | NOMBRE  |
|-------------|---------|
| 1           | Roberto |
| 2           | Carmen  |
| 3           | Luisa   |
| 4           | Esteban |

Se tiene una tabla de consultas

| PACIENTE_ID | FECHA_CONSULTA |
|-------------|----------------|
| 1           | 2023-05-10     |
| 2           | 2023-05-15     |
| 3           | 2023-05-20     |
| 4           | 2023-05-25     |

Se pide obtener los nombres de todos los pacientes que tuvieron su última consulta antes del 16 de mayo de 2023. La columna se debe llamar nombres_pacientes.

```
SELECT nombre as nombres_pacientes
FROM pacientes
WHERE paciente_id IN (SELECT paciente_id FROM consultas WHERE strftime(fecha_consulta) < "2023-05-16")
```

### Subconsultas en el FROM
Las subconsultas tambien conocidas como "subqueries", nos permiten utilizar los resultados de una consulta dentro de otra consulta. En los ejercicios enteriores utilizamos las subconsultas dentro de la clausula WHERE, peri tambien es posible utilizarlas dene otras clausulas. En este ejercicio abordaremos como utilizarla dentro del FROM

Una subconsulta en el FROM tiene la siguiente forma

```
SELECT *
FROM (
    SELECT  * FROM tabla1
)
```

En este caso, no parece tan util ya que simplemente estamos seleccionando lo mismo, pero veamos un caso donde sis eria necesario.

Se tiene la tabla _ventas_ que tiene el codigo del vendedor y el monto de cada venta realizada. Nos piden saber cuanto ses el promedio total vendido

| EMPLEADO_ID | MONTO |
|-------------|-------|
| 1           | 100   |
| 1           | 150   |
| 2           | 200   |
| 2           | 250   |
| 3           | 300   |
| 3           | 350   |
| 4           | 400   |

Para esto necesitanis sumar los montos por vendedor y liego sobre estos resultados sacamos el promedio de las ventas.

```
SELECT AVG(total_venta) as promedio_ventas
FROM (
    SELECT empleado_id; sum(monto) as total_venta
    FROM ventas
    GROUP BY empleado_id
)
```

¿Como llegamos a esto?
Si queremos saber los promedios, primero tenemos que saber los totales, para eso necesitamos sumar por empleados

```
SELECT empleado_id, SUM(monto) as total_venta
FROM ventas
GROUP BY empleado_id
```

El codigo anterior nos genera el siguiente resultado

| EMPLEADO_ID | TOTAL_VENTA |
|-------------|-------------|
| 1           | 250         |
| 2           | 450         |
| 3           | 650         |
| 4           | 400         |

Luego sacamos el promedio de los montos de esta nueva tabla

```
SELECT AVG(total_venta) as promedio_ventas
FROM (
    SELECT empleado_id, SUM(monto) as total_venta
    FROM ventas
    GROUP BY empleado_id
) 
```

Este tipo de ejercicio suele hacerse un poco mas complejo de pensar y escribir, y requiere de cierta practica dominar, por lo mismo el primer ejercicio consistirá en escribir el mismo query. Intenta hacerlo sin mirar la respuesta

Ejercicio:
Se tiene la tabla ventas que tiene el código de vendedor y el monto de la venta. Nos piden saber cuanto es el promedio total vendido. El resultado debe estar en la columna promedio_ventas

```
SELECT AVG(total_venta) as promedio_ventas
FROM (
    SELECT empleado_id, sum(monto) as total_venta
    FROM ventas
    GROUP BY empleado_id
)
```

### Subconsultas en el from parte 2
Ejercicio:
Se tiene la tabla _goles_ que registra los goles logrados por cada  jugador en distintos partidos

| JUGADOR_ID | NOMBRE | GOLES |
|------------|--------|-------|
| 1          | Juan   | 2     |
| 1          | Juan   | 1     |
| 2          | María  | 1     |
| 2          | María  | 1     |
| 3          | Pedro  | 3     |
| 4          | Ana    | 1     |

Nos piden una consulta para calcular el promedio total de goles

```
SELECT AVG(total_goles) as promedio_goles
FROM (
    SELECT jugador_id, sum(goles) as total_goles
    FROM goles
    GROUP BY jugador_id
)
```
> Recuerde que no todas las bases de datos SQL admiten todos los tipos de subconsultas. Aprender cómo y cuándo utilizar cada formulario es un aspecto esencial para crear consultas SQL efectivas.

## Tema 12: Combinacion de consultas

:arrow_up: [ir al inicio](.#tabla-de-contenidos)

### Introduccion a la clausula UNION

El operador **UNION** se utiliza para combinar el resultado de dos o mas SELECT en un solo conjunto de resultados.

La sintaxis basica de UNION es la siguiente:

```
SELECT columna1, columna2
FROM tabla1
UNION SELECT columna1, columna2
FROM tabla2
```

LAs columnas que se seleccionan en los SELECT deben tener los mismos nombres de columna, secuencia y tipos de datos.

Veamos un ejemplo:

Supongamos que tenemos dos tablas "Estutemantes" y "Profesores", que contienen una lista de apellidos e cada una. Queremos crear una lista que combine los apellidos de ambas tablas.

Estutemantes


| ID | NOMBRE | APELLIDO  |
|----|--------|-----------|
| 1  | Juan   | Rodríguez |
| 2  | María  | Sánchez   |
| 3  | Pedro  | Castillo  |

Profesores
| ID | NOMBRE  | APELLIDO |
|----|---------|----------|
| 1  | Alberto | Vargas   |
| 2  | Carla   | Garrido  |
| 3  | Diego   | Mendoza  |

Al hacer la consulta 

```
SEKECT apellido
FROM Estutemantes
UNION
SELECT apellido
FROM profesores
```

Nos dará el resultado

| APELLIDO  |
|-----------|
| Rodríguez |
| Sánchez   |
| Castillo  |
| Vargas    |
| Garrido   |
| Mendoza   |

Ejercicio:
Dada las tablas **estutemantes**

| NOMBRE |
|--------|
| Juan   |
| Maria  |
| Pedro  |

y profesores
| NOMBRE |
|--------|
| Carlos |
| Ana    |
| Luis   |

Escribe una consulta SQL para combinar los nombres de ambas tablas. LA columna resultante debe llamarse nombres

```
SELECT nombre as nombres
FROM estutemantes
UNION
Select nombre
FROM profesores
```
### Eliminar duplicados con UNION

El operador UNION se utiliza para combinar los resultados de dos o mas consultas SELECT en un solo conjunto de resultados. La principal caracteristica de UNION es que se elimina filas duplicadas del resultado final.

Ejercicio:
Se tiene la tabla uusuarios con la siguiente informacion:

| ID | NOMBRE | APELLIDO | EMAIL                    | TELEFONO |
|----|--------|----------|--------------------------|----------|
| 1  | Juan   | Pérez    | juanperez@gmail.com      | 555-1234 |
| 2  | María  | García   | mariagarcia@hotmail.com  | 555-5678 |
| 3  | Pedro  | López    | pedrolopez@yahoo.com     | 555-5678 |
| 4  | Lucía  | Sánchez  | luciasanchez@outlook.com | 555-5555 |
| 5  | Jorge  | Martínez | jorgemartinez@gmail.com  | 555-5678 |

Y la tabla clientes, con la siguiente informacion

| ID | NOMBRE | APELLIDO | EMAIL                    | TELEFONO |
|----|--------|----------|--------------------------|----------|
| 1  | Juan   | Pérez    | juanperez@gmail.com      | 555-1234 |
| 2  | María  | García   | mariagarcia@hotmail.com  | 555-5678 |
| 3  | Pedro  | López    | pedrolopez@yahoo.com     | 555-5678 |
| 4  | Lucía  | Sánchez  | luciasanchez@outlook.com | 555-5555 |
| 5  | Jorge  | Martínez | jorgemartinez@gmail.com  | 555-5678 |

Crea una consulta que nos muestre cada cprreo electronico una unica vez. LA columna mostrada debe llamarse `correos unicos`.

```
SELECT email as correos_unicos
FROM usuarios
UNION
SELECT email
FROM clientes
```

### UNION vs UNION all
En los ejercicios anteriores aprendimos que el operador UNIOON se utiliza para combinar los resultados de dos o mas SELECT en un solo conjunto de resultados, eliminando las filas duplicadas.

Si queremos obtener las filas duplicadas en el resultado, utilizaremos el operador _UNION ALL_

**tabla 1**
| NOMBRE | Edad | 
|----|--------|
| Juan | 30 |
| María | 25|
| Carlos | 40|

**tabla2**
| NOMBRE | Edad | 
|----|--------|
| Juan | 30 |
| Luis | 30|
| Carmen | 25|

Observa que juan está en ambas tablas

Podemos combinar ambas tablas utilizando UNION ALL de la siguiente forma

```
SELECT *
FROM tabla1
UNION ALL
SELECT * 
FROM tabla2
```
Como resultado obtendremos:
| NOMBRE | EDAD |
|--------|------|
| Juan   | 30   |
| Maria  | 25   |
| Carlos | 40   |
| Juan   | 30   |
| Luis   | 30   |
| Carmen | 25   |

Ejercicio:
Dadas las siguientes tablas:
empleados1


| NOMBRE | APELLIDO  | EDAD |
|--------|-----------|------|
| Juan   | Pérez     | 30   |
| María  | González  | 25   |
| Carlos | Rodríguez | 40   |

empleados2

| NOMBRE | APELLIDO | EDAD |
|--------|----------|------|
| Ana    | Martínez | 22   |
| María  | González | 25   |
| Carmen | López    | 25   |

Crea una consulta que combine ambas tablas incluyendo las  filas duplicadas:

```
SELECT  *
FROM empleados1
UNION  ALL
SELECT  *
FROM empleados2
```
### Introducción a intersección
El operador INTERSECT se utiliza para combinar dos SELECT y devolver los resultados que se encuentran en ambas consultas
Por ejemplo, si tenemos las siguientes dos tablas: clientes1 y clientes2

Tabla clientes1

|Nombre|
|-----|
|Juan|
|María|
|Carlos|
|Ana|
|Luis|

Tabla clientes2
|Nombre|
|-----|
|Ana|
|Luis|
|Pedro|
|Carmen|
|Juan|

Podemos encotrar los clientes en comun utilizando INTERSECT de la siguiente forma

```
SELECT nombre
FROM clientes1
INTERSECT
SELECT nombre
FROM clientes2 
```

Como resultado obtendremos

|Nombre|
|-----|
| Ana |
| Juan|
| Luis|

Ejercicio:
Dada las siguientes tablas: **lista1** y **lista2**, encuentra los clientes que estan en ambas listas

Lista1:
| CLIENTE |
|---------|
| Juan    |
| Maria   |
| Carlos  |
| Ana     |
| Luis    |
| Pedro   |
| Carmen  |

Lista2

| CLIENTE |
|---------|
| Ana     |
| Luis    |
| Pedro   |
| Carmen  |
| Juan    |
| María   |
| Sofia   |

```
SELECT cliente
FROM lista1
INTERSECT
SELECT cliente
FROM lista2
```

### El operador EXCEPT
El operador EXCEPT en SQL se utiliza para devolver todas las filas em la primera consulta que no estén presentes en la segunda consulta. En otras palabras, EXCEPT devuelve **SOLO LAS FILAS QUE SON PARTE DE LA PRIMERA CONSULTA PERO NO DE LA SEGUNDA CONSULTA**

Por ejemplo, si tenemos dos tablas: "tabla1" y "tabla2" que contienen los siguientes datos:

tabla1
| ID | NOMBRE |
|----|--------|
| 1  | Juan   |
| 2  | María  |
| 3  | Carlos |

tabla2
| ID | NOMBRE |
|----|--------|
| 1  | Juan   |
| 4  | Ana    |
| 5  | Luis   |

Podemos usar EXCEPT para encontrar los nombres qye estan el la tabla1  pero que no estan en la tabla 2 con la siguiente consulta

```
SELECT nombre
FROM tabla1
EXCEPT
SELECT nombre
FROM tabla2
```

Esto nos daría como resultado

|NOMBRE|
|------|
|María|
|Carlos|

Ejercicio:
Dadas las siguientes tablas: "empleados" y "gerentes" que contienen los siguientes datos:

empleados:
| ID | NOMBRE |
|----|--------|
| 1  | Juan   |
| 2  | María  |
| 3  | Carlos |
| 4  | Ana    |
| 5  | Luis   |

Gerentes:
| ID | NOMBRE |
|----|--------|
| 1  | Juan   |
| 2  | María  |

Crea una consulta que muestre los nombres de los empleados que no son gerentes:

```
SELECT nombre
FROM empleados
EXCEPT
SELECT nombre
FROM gerentes
```

## Tema 13: Insercion de registros

:arrow_up: [ir al inicio](.#tabla-de-contenidos)

### Añadir un registro en una tabla
Con SQL podemos ingresar datos nuevos a tablas ya existentes. Para lograrlo utilizaremos la instruccion **INSERT**
La declaracion INSERTes usada para añadir nuevas filas de tados a una tabla en una base de datos. Hay dos formas principales del comando INSERT:
`INSERT INTO`, si las columnas no tienen nombre, espera un set completo de columnas y `INSERT INTO table_name (column1, column2, ...)` donde solo las columnas nombradas seran llenadas con los datos.

#### Uso
1. Insertando un conjunto completo de columnas
Código de ejemplo:
```
INSERT INTO table_name
VALUES (value1, value2, ..., valueN
```

En el ejemplo arriba, necesitamos proveer valores para todas las columnas disponibles en la tabla.

2. Insercion de datos selectivo
Codigo de ejemplo
```
INSERT INTO table_name (column1, column2, ..., columnN)
VALUES (value1, value2, ..., valueN)
```
3. Insertar datos desde otra tabla
Otra forma util del comando INSERT es `INSERT INTO SELECT` que nos permite copiar datos desde otra tabla y añadirlo en la tabla que estamos trabajando.

Codigo Ejemplo:

```
INSERT INTO table1 (column1, column2, ..., columnN)
SELECT column1, column2, ..., colunN
FROM table2
WHERE condition
```
En este escenario `table2`ya deberia tener la data que necesitamos y la clausula WHERE puede ser usada para seleccionar solo aquellas filas que satisfagan esa condicion.

La isntruccion INSERT la acompañaremos de la palabra clave INTO para especificar en que tabla queremos insertar un valor, y VALUES para especificar los valores que queremos insertar.
Por ejemplo, si tenemos una tabla llamada **productos** con las columnas id, nombre y precio, podemos agregar un nuevo producto a la tabla utilizando:

```
INSERT INTO productos
VALUES (1, 'Camiseta', 2000);
```

Para cada columna en la tabla, debemos ingresar los valores correspondientes en el mismo orden en que se definen en la sentencia. Debemos utilizar comillas simples para valores de tipo de datos de texto.

Ejercicio:

Dada la **tabla usuarios** con las columnas id, nombre. apellido, email, telefono

| COLUMNA  | TIPO DE DATO |
|----------|--------------|
| id       | INTEGER      |
| nombre   | TEXT         |
| apellido | TEXT         |
| email    | TEXT         |
| telefono | TEXT         |

Crea un nuevo usuario con los siguientes datos:
* id: 7
* nombre: Lucia
* aoellido: Sanchez
* email: luciasanchez@outlook.com
* telefono: 555-5555

```
INSERT  INTO usuarios
VALUES  (7,  'Lucía',  'Sánchez',  'luciasanchez@outlook.com',  '555-5555')
```
### Añadir un registro en una tabla parte 2
Ejercicio:
Se tiene la tabla productos

| COLUMNA | TIPO    |
|---------|---------|
| id      | INT     |
| nombre  | VARCHAR |
| precio  | INT     |
| stock   | INT     |

Inserta un nuevo producto con los siguientes datos

* id: 7
* nombre: Bolso
* precio: 1000
* stock: 10

```
INSERT  INTO PRODUCTOS
VALUES  (7,  'Bolso',  1000,  10)
```

### Especificando valores nulos
A la hora de insertar datos, si hay un valor que no conocemos, o es un valor que no queremos especificar, podemos ingresar un valor nulo.

Ejemplo: Se tiene la tabla productos:

| COLUMNA | TIPO    |
|---------|---------|
| id      | INT     |
| nombre  | VARCHAR |
| precio  | INT     |
| stock   | INT     |

Podemos ingresar solo el id y el nombre con:
```
INSERT INTO productos
VALUES (1, 'camiseta', NULL, NULL)
```

Ejercicio:
Se tiene la tabla productos:

| COLUMNA | TIPO    |
|---------|---------|
| id      | INT     |
| nombre  | VARCHAR |
| precio  | INT     |
| stock   | INT     |

Inserta un nuevo producto con los diguientes datos:
* id: 7
* nombre: Bolso
* precio: 1000

```
INSERT  INTO productos
values  (7,  'Bolso',  1000,  NULL)
```

## Añadir un registro especificando columnas
A ka hora de insertar datos, es posible mencionar especificamente las columnas que se van a insertar en lugar de mencionar todos los valores en el orden en que se definen en la tabla.

Veamos un ejemplo:
Se tiene la tabla productos

| COLUMNA | TIPO    |
|---------|---------|
| id      | INT     |
| nombre  | VARCHAR |
| precio  | INT     |
| stock   | INT     |

Se pide insertar un nuevo producto con los siguientes datos, pero especificando las columnas:
* id: 7
* nombre: Bolso
* Precio: 1000
* Stock: 10

```
INSERT INTO productos
(id, precio, nombre, stock) values (7, 1000, 'Bolso', 10)
```

Una ventaja de este metodo es que no es necesario ingresar los valores en el mismo orden en que se definen en la tabla

Ejercicio:
Se tiene la tabla usuarios:

| COLUMNA  | TIPO DE DATO |
|----------|--------------|
| id       | INTEGER      |
| nombre   | TEXT         |
| apellido | TEXT         |
| email    | TEXT         |
| telefono | TEXT         |

Prueba agregando los siguientes datos a la tabla usuarios, puedes notar que tienen el orden alterado en relacion a la tabla:
* id: 7
* apellido: Sánchez
* nombre: Lucia
* telefono: 333-3333
* email: luciasanchez@outlook.com

```
INSERT  INTO USUARIOS
(ID, APELLIDO, NOMBRE, TELEFONO, EMAIL)
VALUES  (7,  'Sánchez',  'Lucía',  '333-3333',  'luciasanchez@outlook.com');
```

### Añadir un registro especificando solo algunas columnas
Otro beneficio de especificar las columnas al momento de insertar datos es que se insertaran valores nulos en las columnas no mencionadas automaticamente:

Supongamos que tenemos una tabla llamada productos:

| COLUMNA | TIPO |
|---------|------|
| nombre  | TEXT |
| precio  | INT  |
| stock   | INT  |

Podemos ingresar el producto 'Gorro', con un precio de 1000 y dejar el stock en nulo de la siguiente manera

```
INSERT INTO PRODUCTOS
(nombre, precio) VALUES ('Gorro', 1000);
```

Mas adelante aprenderemos que algunas columnas pueden tener restricciones que no permiten valores nulos

Ejercicio:
Inserta un nuevo item en la tabla productos con los siguientes datos:

* nombre: Bolso
* stock: 10

```
INSERT  INTO PRODUCTOS
(nombre, stock)  VALUES  ('Bolso',  10)
```

### Añadir fecha de hoy a un registro
Si queremos insertar la fecha actual al momento de crear un registro, podemos utilizar la funcion **CURRENT_DATE**	para obtenerla.

Ejemplo:

```
INSERT INTO USUARIOS
(nombre, fecha_creacion) VALUES ('Gonzalo', CURRENT_DATE)
```

Ejercicio:

| COLUMNA | TIPO |
|---------|------|
| nombre  | TEXT |
| precio  | INT  |
| stock   | INT  |
| fecha   | DATE |

Si tenemos la tabla productos, inserta un nuevo producto con los siguientes datos

* nombre: Bolso
* stock: 10
* fecha: CURRENT_DATE
```
INSERT  INTO PRODUCTOS
(nombre, stock, fecha)  VALUES  ('Bolso',  10,  CURRENT_DATE)
```

###  Añadiendo fecha formateada
Si queremos insertar una fecha cualquiera al momento de crear un registro, simplemente debemos hacerlo especificando la fecha en el formato esperado.
El formato de fecha es `YYYY-MM-DD`o sea, año.mes-tema, donde el año es de 4 digitos, el mes de dos digitos, y el tema de dos digitos.

Ejemplo: 
```
INSERT INTO USUARIOS
(nombre, fecha_creacion) VALUES ('Gonzalo', '2021-01-01')
```

Ejercicio:
Se tiene la tabla Productos

| COLUMNA | TIPO |
|---------|------|
| nombre  | TEXT |
| precio  | INT  |
| stock   | INT  |
| fecha   | DATE |

Inserta un nuevo producto con los siguientes datos:
* nombre: Bolso
* stock: 10
* fecha: fecha_con_formato

La fecha del producto debe ser primero de enero del 2023

```
INSERT  INTO PRODUCTOS
(nombre, stock, fecha)  VALUES  ('Bolso',  10,  '2023-01-01')
```
### Añadir multiples valores
Podemos ingresar varios registros en una tabla en una sola sentencia INSERT. Para lograrlo, debemos especificar los valores de cada registro separados por coma.
Por ejemplo, si tenemos una tabla llamada **ventas** con las columnas _producto_, _cantidad_, y _precio_ podemos agregar varios registros a la tabla usando:

```
INSERT INTO VENTAS
VALUES ('camiseta', 5, 2000), ('Pantalon', 3, 1500), ('Zapatos', 2, 3000);
```

Ejercicio:
Inserta los siguientes registros en la tabla ventas:

| PRODUCTO | CANTIDAD | PRECIO |
|----------|----------|--------|
| Gorro    | 5        | 1000   |
| Camiseta | 10       | 500    |
| Pantalón | 8        | 1500   |

```
INSERT  INTO VENTAS
VALUES
('Gorro',  5,  1000),
('Camiseta',  10,  500),
('Pantalón',  8,  1500);
```
### Crear un registro con un campo **autoincremental**

En una base de datos de SQL, es posible agilizar el proceso de insercion de datos en una tabla metemante el uso de un campo autoincremental.Este tipo de campo es especialmente util cuando se trata de gestionar indentificadores unicos, como por ejemplo, el campo de 'id' de una tabla. La caracteristica de autoincremento se logra empleando la clausula AUTOINCREMENT en la definicion del campo.
Para ilustrar este proceso, consideremos una tabla llamada "empleados" con tres colimnas "id" (autoincremental), "nombre" y "apellido". Esta es la forma en que se crea la tabla

```
CREATE TABLE EMPLEADOS
(id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, apellido TEXT)
```

Aqui hemos definido la columna "id" como un campo autoincremental utilizando la clausula AUTOINCREMENT, lo que asegura que se generará automaticamente un valor unico y creciente para cada nuevo registro.

Supongamos qye deseamos insertar un nuevo empleado en esta tabla. Podemos utilizar la siguiente consulta en SQL:

```
INSERT INTO EMPLEADOS
(nombre, apellido) VALUES ('John', 'Doe')
```

Al ejecutar esta consulta, se creara un nuevo empleado en la tabla "empleados". La columna "id" se incrementará automaticamente, mientras que los valores proporcionados para "nombre" y "apellido" seran almacenados en las columnas correspondientes. Esto garantiza que cada nuevo empleado tendrá un identificador unico y que el proceso de insercion sea mas eficiente.

Ejercicio:

Dada una tabla empleados, con las columnas id, nombre y apellido, crea un nuevo empleado con el nombre "Jane" y el apellido "Smith"

```
INSERT  INTO EMPLEADOS
(nombre, apellido)  VALUES  ('Jane',  'Smith')
```

### Añadir un registro asumiendo un valor por defecto

Al crear una tabla SQL, puedes asignar valores predeterminados a sus columnas. Esto implica que al insertar nuevos datos, si no se proporciona un valir especifico para una columna, se utilizara automaticamente el valor por defecto asignado.

Supongamos que queremos crear una tabla llamada "productos" con las siguientes columnas:

* ID: identificador unico del producto.
* Nombre: nombre del producto
* Precio: precio del producto con un valor por defecto de 10

```
CREATE TABLE productos
(ID INTEGER KEY AUTOINCREMENNT, NOMBRE TEXT, PRECIO INTEGER DEFAULT 10);
```

Si insertamos un nuevo producto solo con el nombre, se utilizará automaticamente el valor por defecto del precio.

```
INSERT INTO PRODUCTOS
(NOMBRE) VALUES ('Ejemplo Producto')
```

En este caso, el producto se insertará con el valor de 10 en la columna PRECIO.
Si deseamos insertar un producto con un precio diferente, simplemente proporcionamos el valor correspondiente

```
INSERT INTO PRODUCTOS
(NOMBRE, PRECIO) VALUES ('Otro  producto', 25)
```

Ejercicio:

Dada la tabla Usuarios con las columnas id, nombre, apellido, email, telefono, crea un nuevo usuario con los valores:

* nombre Lucía
* apellido: Sánchez
* email: luciasanchez@outlook,com
La columna telefono tiene un valor por defecto 111-1111

```
INSERT  INTO USUARIOS
(NOMBRE, APELLIDO, EMAIL)  VALUES  ('Lucía',  'Sánchez',  'luciasanchez@outlook.com')
```


## Tema 14: Borrado y modificación de registros
:arrow_up: [ir al inicio](.#tabla-de-contenidos)

### Borrar todos los registros de una tabla
En SQL la clausula DELETEnos ayuda a eliminar registros existenes de una base de datos. Sin embargo, hay que tener en cuenta que es una operacion destructiva y puede borrar permanentemente datos de nuestra base de datos.

Con la cláusula `DELETE` podemos realizar lo siguiente:
1. Borrar todas las filas
La clausula `DELETE` sin una clausula `WHERE` borra **TODAS** las filas en una tabla. **ESTA OPERACION ES IRREVERSIBLE**

```sql
DELETE FROM table_name;
```

Esta clausula borra todos los registros de la `table_name`

2. Borrar una fila en especifico
Cuando combinamos la clausula `WHERE` con la declaracion `DELETE` borra el registro en especifico que cumpla con esa condicion

```sql
DELETE FROM table_name
WHERE condition;
```

Es crucial usar `DELETE` con mucho cuidado, tiene el potencial de borrar ciertas filas importantes de la tabla o borrar la tabla por completo.

> Nota: La eliminación realizada metemante la sentencia "DELETE" es permanente y no puede deshacerse. Asegúrese siempre de tener una copia de seguridad antes de ejecutar una consulta DELETE, especialmente cuando se trata de una base de datos de producción.

Ejercicio:
Borra todos los datos de la tabla PRODUCTOS

```sql
DELETE
FROM PRODUCTOS;
```

### Borrar un registro con WHERE
La clausula WHERE se utiliza para eliminar datos de una tabla. Si queremos eliminar filas especificas en lugar de todos los datos de la tabla, podemos usar la clausula WHERE junto con la sentencia DELETE. Esto nos permite especificar una condición para determinar que filas se eliminarán.

Por ejemplo, si tenemos una tabla de productos y queremos eliminar solo aquellos productos cuyo precio sea igual a 1000, podemos usar la siguiente clausula:

```sql
DELETE
FROM productos
WHERE precio = 1000
```

Ejercicio:
Dada la tabla usuarios, con los siguientes datos:

| ID | NOMBRE | APELLIDO | EMAIL                    | TELEFONO |
|----|--------|----------|--------------------------|----------|
| 1  | Juan   | Pérez    | juanperez@gmail.com      | 555-1234 |
| 2  | María  | García   | mariagarcia@hotmail.com  | 555-5678 |
| 3  | Pedro  | López    | pedrolopez@yahoo.com     | 555-9876 |
| 4  | Lucía  | Sánchez  | luciasanchez@outlook.com | 555-5555 |
| 5  | Jorge  | Martínez | jorgemartinez@gmail.com  | 555-4321 |

Borra el usuario cuyo id sea igual a 2

```sql
DELETE
FROM USUARIOS
WHERE ID =  2
```
### Editar registros

La declaracion de SQL `UPDATE` se usa para modificar la data existente en una bse de datos. Esta declaracion es muy util cuando necesitamos cambiar los valores asignacdos a unos campos en especifico en una tabla ya existente.

La sintaxis general para usar la declaracion `UPDATE` es la siguiente

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition
```

* `table_name` es el nombre de la tabla que  vamos a modificar
* `SET` esta clausula especifica el nombre de la columna y el nuevo valor al que va a ser actualizado.
* `colum1, colum2, ...` los nombres de las columnas en la tabla
* `value1, value2, ...` los nuevos valores que queremos guardar en el registro
* `WHERE` esta clausula especifica la condicion a cumplir para identificar que fila(s) vamos a actualizar.
#### Ejemplo

Aqui hay un ejemplo que quizas podria darnos un poco mas de claridad. Para la tabla `Employee` tenemos los siguientes valores:

| EmployeeID | Name | Position | Salary |
|:----------:|:----:|:--------:|:------:|
| 1          | Jane | Manager  | 50000  |
| 2          | John | Clerk    | 30000  |
| 3          | Bob  | Engineer | 40000  |

Si queremos incrementar el salario de Bob por $5.000, usariamos:

```sql
UPDATE EMPLOYEE
SET SALARY = 45000
WHERE EMPLOYEEID = 3
```

Esto cambiaria permanentemente los datos de la tabla employee asi:

| EmployeeID | Name | Position | Salary |
|:----------:|:----:|:--------:|:------:|
| 1          | Jane | Manager  | 50000  |
| 2          | John | Clerk    | 30000  |
| 3          | Bob  | Engineer | 45000  |

> Siempre tener cuidado con la clausula `UPDATE`, si la usamos sin la clausula `WHERE` va a actualizar todas las filas de una tabla
> Por ejemplo: imaginemos que tenemos la tabla ventas con una columna llamada "total". Si queremos aumentar en un 10% el total de todas las ventas registradas en la tabla, podemos hacerlo de la siguiente  manera
```sql
UPDATE ventas
SET total = total * 1.10
```

Ejercicio:
Se tiene una tabla usuarios, con los siguientes valores

| ID | NOMBRE | APELLIDO | EMAIL                    | REGISTRADO |
|----|--------|----------|--------------------------|------------|
| 1  | Juan   | Pérez    | juanperez@gmail.com      | FALSE      |
| 2  | María  | García   | mariagarcia@hotmail.com  | FALSE      |
| 3  | Pedro  | López    | pedrolopez@yahoo.com     | FALSE      |
| 4  | Lucía  | Sánchez  | luciasanchez@outlook.com | FALSE      |
| 5  | Jorge  | Martínez | jorgemartinez@gmail.com  | FALSE      |

Edita la columna REGISTRADO para que todos los usuarios tengan valor TRUE

```sql
UPDATE USUARIOS
SET REGISTRADO =  TRUE
```

### Editar todos los registros utilizando where
Si queremos editar solamente algunas filas de nuestra tabla, podemos utilizar UPDATE en conjunto con WHERE. De esta forma, solo se modificaran los registros que cumplan con la condicion especificada. 

```sql
UPDATE nombre_tabla
SET nombre_columna = nuevo_valor
WHERE condicion
```

Supongamos que gestionamos una tabla llamada empleados que contiene informacion sobre los empleados de una empresa. Entre las columnas se encuentran `id_empleado`, `nombre`, `salario`, y `departamento`. Si deseamos aumentar el salario en un 15% solamente para los empleados que trabajan en el departamento "ventas" podríamos emplear la instrucción UPDATE junto con WHERE de la siguiente manera.

```sql
UPDATE empleados
SET salario = salario * 1.15
WHERE departamento = 'Ventas';
```

Es importante ser precavido al elegir la condicion de filtrado para tus filas. De esta manera, te aseguras de no alterar accidentalmente datos equivocados.

Ejercicio:

Se tiene la tabla usuarios con los siguientes datos:

| ID | NOMBRE | APELLIDO | EMAIL                    | TELEFONO |
|----|--------|----------|--------------------------|----------|
| 1  | Juan   | Pérez    | juanperez@gmail.com      | 555-1234 |
| 2  | María  | García   | mariagarcia@hotmail.com  | 555-5678 |
| 3  | Pedro  | López    | pedrolopez@yahoo.com     | 555-9876 |
| 4  | Lucía  | López    | luciasanchez@outlook.com | 555-5555 |
| 5  | Jorge  | Martínez | jorgemartinez@gmail.com  | 555-4321 |

Asignale el telefono 123-456 al usuario con el id 4

```sql
UPDATE usuarios
SET telefono =  '123-456'
WHERE id =  4
```

### Editar multiples columnas

En SQL es posible editar multiples columnas de un registro, utilizando la clausula SET. Para lograrlo, debemos especificar el nombre de cada columna que queremos modificar, seguido del nuevo valor que queremos asignarle.

```sql
UPDATE table
SET 
	columna1 = 'nuevo_valor',
	columna2 = 'nuevo_valor',
	columna2 = 'nuevo_valor'
WHERE
	condicion;
```

Ejercicio:

Se tiene una tabla de posts con las siguientes columnas:

| COLUMNA   | TIPO DE DATO |
|-----------|--------------|
| id        | INTEGER      |
| titulo    | TEXT         |
| contenido | TEXT         |
| autor     | TEXT         |
| fecha     | TEXT         |

Edita el post con el id 1 para que el titulo sea "Aprendiendo SQL" y el contenido "SQL es un lenguaje de programación para gestionar bases de datos relacionales"

```sql
UPDATE POSTS
SET
	titulo =  'Aprendiendo SQL',
	contenido =  'SQL es un lenguaje de programación para gestionar bases de datos relacionales'
WHERE ID =  1
```

## Tema 15: Tablas
:arrow_up: [ir al inicio](.#tabla-de-contenidos)
### Nuestra primera tabla

Hasta este punto hemos aprendido cómo realizar consultas en tablas predefinidas e incluso como insertar datos a las tablas,, pero ¿cómo creamos nuestras propias tablas?

Para crear una tabla en SQL, se utiliza la sentencia `CREATE TABLE` de la siguiente forma:



La sentencia `CREATE TABLE` en SQL es una Lenguaje de definicion de datos ( Data Definition Language (DDL)).

```sql
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype,
   ....
);
```

+  `table_name` : es el nombre de la tabla que vamos a crear
+ `column1, column2, ...` son las columnas de la tabla.
+ `datatype` es el tipo de datos para la columna, bien sea 'varchar', 'int', 'date', etc.

La sentencia `CREATE TABLE` permite definir la estructura de la tabla, incluyendo el nombre de las columnas y sus tipos de datos. Veamos un ejemplo de como crear una tabla de productos que incluye diferentes tipo de datos en las columnas:

```sql
CREATE TABLE productos (nombre text)
```

Luego, una vez creada la tabla, podemos insertar datos tal como aprendimos en ejercicios anteriores:

```sql
INSERT INTO productos
VALUES ('Ipad Pro 2022'), ('Iphone 13 Pro Max'), ('Macbook Pro 2023')
```

Ejercicio: 
Crea una tabla llamada **alumnos** que almacene una columna:

| Columna | tipo de texto  |
|--|--|
| Nombre | Texto |

Inserta un registro dentro de la tabla creada utilizando los siguientes datos:
* nombre: Lucía
> Pista: Para poder ingresar las dos queries requeridas, recuerda añadir punto y coma al final de cada una.

```sql
CREATE  TABLE alumnos (nombre text);
INSERT  INTO alumnos
VALUES  ('Lucía');
```

### Una tabla con multiples columnas

Al momento de crear una tabla podemos especificar multiples columnas, cada una con su nombre y tipo de dato. POr ejemplo, si queremos crear una tabla de productos qye incluya el nombre, descripcion y precio de cada producto, podemos hacerlo de la siguiente forma:

```sql
CREATE TABLE productos (nombre TEXT, descripcion TEXT, precio TEXT);
```

Ejercicio:
Crea una tabla llamada **alumnos** con las siguientes columnas:

|Columna  | Tipo de dato |
|--|--|
| nombre | texto |
| apellido | texto |
| telefono | texto |

Inserta un registro dentro de la tabla creada, utilizando los siguientes datos:

* nombre: Lucía
* apellido: Sánchez
* telefono: 12345678

> Pista: para poder ingresar las dos queries requeridas, recuerda añadir punto y coma al final de cada una.

```sql
CREATE  TABLE alumnos (
nombre TEXT,
apellido TEXT,
telefono TEXT
);
INSERT  INTO alumnos
VALUES  ('Lucía',  'Sánchez',  '12345678')
```
### Tablas con distintos tipos de datos

Adicionalmente a los datos de tipo texto podemos utilizar otros tipos de datos, en este ejercicio abordaremos los 3 siguientes tipos:
* integer para almacenar numeros enteros
* Boolean para almacenar valores de verdadero o falso
* DATE para almacenar fechas

Ejercicio:
Crea una tabla llamada **usuarios** con las siguientes columnas:

|Columna  | Tipo de dato |
|--|--|
| nombre | texto |
| apellido | texto |
| edad| integer |
| activo | boolean |
| nacimiento | date  |

Luego inserta un registro dentro de la tabla cerada utilizando los siguientes datos

* nombre: Lucía
* apellido: Sánchez
* edad: 25
*  activo: True
* nacimiento: 1996-01-01

> Pista: para poder ingresar las dos queries requeridas, recuerda añadir punto y coma al final de cada una.

```sql
CREATE  TABLE USUARIOS (
	NOMBRE TEXT,
	APELLIDO TEXT,
	EDAD INT,
	ACTIVO BOOLEAN,
	NACIMIENTO DATE
);
INSERT  INTO USUARIOS
VALUES  (
'Lucía',
'Sánchez',
25,
TRUE,
'1996-01-01'
)
```

### Tipos reales
Hasta el momento hemos visto los siguientes tipos de datos:
* TEXT: para almacenar texto
* INTEGER: para almacenar numeros enteros
* BOOLEAN: para almacenar valores de verdadero o falso
* DATE: para almacenar fechas.

En este ejercicio veremos el tipo de dato REAL, que permite almacenar numeros con decimales

Ejercicio
Crea una tabla llamada temperaturas con la columna `temperatura_celsius`

|Columna  | Tipo de dato |
|--|--|
| temperatura_celsius | real |

Luego inserta los siguiente registros:

| temperatura_celsius  |
|--|
| 23.4 |
| 26.5 |
| 27.1 |

> **Importante**. Para ingresar la parte decimal de los números, utiliza el punto (.) como separador decimal

```sql
CREATE  TABLE TEMPERATURAS (
temperatura_celsius FLOAT
);
INSERT  INTO TEMPERATURAS
VALUES  (
	23.4
),  (
	26.5
),  (
	27.1
)
```

### Borrar una tabla
En SQL podemos utilizar el comando **DROP  TABLE** para eliminar una tabla.

Por ejemplo, si queremos eliminar la tabla **temperaturas** que creamos en el ejercicio anterior, podemos hacerlo con la siguiente query:

```sql
DROP TABLE temperaturas;
```

Si intentamos hacer un SELECT de la tabla **temperaturas** luego de eliminarla, obtendremos un error.

Ejercicio:

En este ejercicio tendremos una tabla con datos que no nos interesan, debemos borrarla, crearla de nuevo y probarla con los datos pedidos.

Borra la tabla **temperaturas** y vuelve a crearla con las siguientes columnas:

|Columna  | Tipo de dato |
|--|--|
| ciudad | text |
| temperatura | real | 
| fecha | date| 

Luego, inserta los siguientes registros:

| CIUDAD       | TEMPERATURA | FECHA      |
|--------------|-------------|------------|
| Buenos Aires | 20.0        | 2024-01-01 |
| Buenos Aires | 21.0        | 2024-01-02 |
| Santiago     | 22.0        | 2024-01-01 |
| Santiago     | 23.0        | 2024-01-02 |

> **Importante:** para poder ingresar las queries requeridas, recuerda añadir punto y coma al final de cada una.

```sql
DROP  TABLE TEMPERATURAS;
CREATE  TABLE TEMPERATURAS (
CIUDAD TEXT,
TEMPERATURA FLOAT,
FECHA DATE
);
INSERT  INTO TEMPERATURAS
VALUES  (
	'Buenos Aires',
	20.0,
	'2024-01-01'
),  (
	'Buenos Aires',
	21.0,
	'2024-01-02'
),  (
	'Santiago',
	22.0,
	'2024-01-01'
),  (
	'Santiago',
	23.0,
	'2024-01-02'
)
```

### Actualizar una tabla

En este ejercicio aprenderemos a añadir una columna a una tabla existente. Para ello, utilizaremos la sentencia `ALTER TABLE`que nos permite modificar la definicion de una tabla.

La sintaxis para lograrlo es la siguiente:

```sql
ALTER TABLE nombre_tabla ADD COLUMN nombre_columna tipo_dato;
```
Donde tenemos que esoecificar el nombre de la tabla existente, el nombre de la columna nueva y el tipo de dato que utilizaremos.

Por ejemplo, si tenemos la tabla `personas` con las siguientes columnas: **nombre** y **apellido**, y queremos agregar la columna edad de tipo `integer` podemos hacerlo de la siguiente manera:

```sql
ALTER TABLE personas ADD COLUMN edad INTEGER
```

Ejercicio:

En este ejercicio vamos a modificar la tablla **productos** para agregar la columna **descripcion** de tipo **TEXT**.

Actualmente la tabla columna **productos ** tiene las siguientes columnas:

|Columna | Tipo de dato  |
|--|--|
|  nombre |  text |
| precio  | real |

Luego de crearla, deberas insertar los siguientes datos:

| NOMBRE    | PRECIO  | DESCRIPCION           |
|-----------|---------|-----------------------|
| Camisa    | 1000.00 | Camisa de manga corta |
| Pantalón  | 2000.00 | Pantalón de mezclilla |
| Camisa XL | 1000.00 | Camisa de manga larga |

> **Importante:** para poder ingresar las queries requeridas, recuerda añadir punto y coma al final de cada una.

```sql
ALTER  TABLE PRODUCTOS
ADD  COLUMN DESCRIPCION TEXT;
INSERT INTO PRODUCTOS
VALUES
	('Camisa',  1000.0,  'Camisa de manga corta'),
	('Pantalón',  2000.0,  'Pantalón de mezclilla'),
	('Camisa XL',  1000.0,  'Camisa de manga larga')
```

## Tema 16: Restricciones
:arrow_up: [ir al inicio](.#tabla-de-contenidos)

### Introduccion a restricciones
Al crear tablas, podemos añadir restricciones (en ingles **constraints**) a las columnas para evitar que se ingresen datos que no cumplan ciertas condiciones.
> son usados para especificar reglas para la  data en una tabla. Las restricciones son usadas para limitar el tipo de data que puede ir dentro de una tabla. Esto asegura la presicion y fiabilidad de la data en una tabla.

#### NOT NULL
Asegura que a la columna no se le pueda añadir un valor nulo.
En este ejercicio, aprenderemos la restriccion `NOT NULL` que impide valores nulos en una columna. POr ejemplo, al crear una tabla de personas con nombre y apellido, podemos hacer que el nombre sea obligatorio (no nulo) y el apellido opcional.

Para lograrlo, crearemos la tabla de la siguiente forma:

```sql
CREATE TABLE personas (
    nombre TEXT NOT NULL,
    apellido TEXT
)
```

Para agregar una restriccion, simplemente debemos especificarla con la columna

Para indicar las restricciones, utilizaremos una columna adicional llamada **Cnstrains**, en nuestros temagramas. Ejemplo con la tabla **personas**

| COLUMN   | DATA TYPE | CONSTRAINTS |
|----------|-----------|-------------|
| nombre   | TEXT      | NOT NULL    |
| apellido | TEXT      |             |

Pongamos a prueba nuestra restriccion con distintas consultas y observemos los resultados

| QUERY                                                             | RESULTADO                                                       |  
|-------------------------------------------------------------------|-----------------------------------------------------------------|
| ```INSERT INTO personas (nombre, apellido) VALUES ('Juan', 'Pérez');``` | Funciona                                                        |  
| ```INSERT INTO personas (nombre, apellido) VALUES (NULL, 'Pérez');```   | No funciona, error: NOT NULL constraint failed: personas.nombre | 
| ```INSERT INTO personas (apellido) VALUES ('Pérez');```                 | No funciona, error: NOT NULL constraint failed: personas.nombre | 

En resumen: en esta tabla que acabamos de crear podremos hacer un insert de una persona con nombre y sin apellido, pero no podremos ingresar una persona sin nombre

Ejercicio:

Crea una tabla llamada **empleados** con las siguientes columnas

| COLUMNA  | TIPO DE DATO | RESTRICCIONES |
|----------|--------------|---------------|
| nombre   | TEXT         | NOT NULL      |
| apellido | TEXT         |               |

Luego ingresa los siguientes datos:

* Nombre: Pedro
* Apellido: Perez

```sql
CREATE  TABLE EMPLEADOS (
nombre TEXT NOT  NULL,
apellido TEXT
);

INSERT  INTO EMPLEADOS (nombre, apellido)

VALUES  ('Pedro',  'Pérez')
```

### Agregar una restriccion a una tabla existente
En SQL tambien es posible agregar la restriccion a una tabla ya creada. Supongamos que tenemos la siguiente tabla **personas**
| COLUMNA  | TIPO DE DATO | RESTRICCIONES |
|----------|--------------|---------------|
| nombre   | TEXT         | 		      |
| apellido | TEXT         |               |

y queremos agregarle la restriccion NOT NULL a la columna nombre. El problema es que en SQLite no podemos agregar restricciones directamente a una tabla existente.

En otros motores de bases de datos como PostgreSQL o MySQL [si es posible agregar restricciones a tablas existentes](./#adding-not-null-to-an-existing-table).

Lo que tenemos que hacer es:
1. Crear una nueva tabla con la restriccion.
```sql
CREATE TABLE personas2(
	nombre TEXT NOT NULL,
	apellido TEXT
)
```
2. Copiar los datos de la tabla original a la nueva tabla
```sql
INSERT INTO personas2(nombre, apellido)
	SELECT nombre, apellido
	FROM personas;
```

3. Borrar la tabla original
```sql
DROP TABLE personas
```
4. Renombrar la nueva tabla con el nombre de la tabla original
```sql
ALTER TABLE personas2 RENAME TO personas;
```

Ejercicio:
Se tiene una tabla llamadas patentes, con las siguientes columnas

| COLUMNA  | TIPO DE DATO | RESTRICCIONES |
|----------|--------------|---------------|
| patente  | TEXT         | 		      |

con la siguiente información 
| PATENTE |
|---------|
| ABC123  |
| ABC124  |

Se pide agregar una restriccion de not null a la columna patente

```sql
create  table patentes2 (
patente TEXT NOT  NULL
);
INSERT  INTO patentes2(patente)
	SELECT patente
	FROM patentes;
DROP  TABLE patentes;
ALTER  TABLE patentes2 RENAME  TO patentes
```

### Borrar una restriccion
En SQLite borrar una restriccion tiene las mismas limitaciones que modificarla y el procedimiento es igual:

1. Crear una tabla sin la restriccion
2. Copiar los datos de la tabla original
3. Borrar la tabla original
4. Renombrar la nueva tabla con el nombre de la tabla original

Ejercicio:
Se tiene la tabla llamada **personas** con las siguientes columnas

| COLUMNA  | TIPO DE DATO | RESTRICCIONES |
|----------|--------------|---------------|
| nombre   | TEXT         | NOT NULL      |
| apellido | TEXT         | NOT NULL      |
| edad     | INTEGER      |               |

Se pide borrar la restricción de `NOT NULL` de las columnas nombre y apellido:

```sql
CREATE  TABLE personas2 (
nombre TEXT,
apellido TEXT,
edad INTEGER
);
INSERT  INTO personas2(nombre, apellido, edad)
SELECT nombre, apellido, edad
FROM personas;
DROP  TABLE personas;
ALTER  TABLE personas2 RENAME  TO personas;
```

###### Adding NOT NULL to an existing table
Fragmento tomado de [roadmap](https://roadmap.sh/sql)
Podemos añadir una restriccion NOT NULL  a una tabla existente, usando ela declaracion `ALTER TABLE`. Sin embargo, primero debemos **verificar que la columna no contenga valores NULL** antes de añadir la restriccion `NOT NULL`

Aui tenemos un ejemplo:
```sql
ALTER TABLE Employees
MODIFY Address varchar(255) NOT NULL;
```

Este comando va a modificar la tabla `Employees` y configurar la columna `Address` como `NOT NULL`

> Nota: en unos sistemas como PostgreSQL podemos usar el comando `ALTER TABLE` seguido por `SET NOT NULL`

### Restriccion UNIQUE
La restriccion de unicidad, o **UNIQUE** nos permite evitar duplicados en una columna especifica. Un caso muy popular de estas restricciones es evitar personas con el mismo correo electronico.

Para agregar una restriccion de UNIQUE simplemente tenemos que especificar la restriccion justo despues de especificar el tipo de dato. Por ejemplo:

```sql
CREATE TABLE personas (
	nombre text
	apellido text
	email text UNIQUE
)
```

Pongamos a prueba nuestra restriccion con distintas consultas y observemos los resultados:

| QUERY                                                                                              | FUNCIONA                                                     |
|----------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| INSERT INTO personas (nombre, apellido, email) VALUES ('Juan', 'Pérez', 'juan.perez@email.com');   | Funciona                                                     |
| INSERT INTO personas (nombre, apellido, email) VALUES ('María', 'García', 'juan.perez@email.com'); | No funciona, error: UNIQUE constraint failed: personas.email |
| INSERT INTO personas (nombre, apellido, email) VALUES ('Pedro', 'Pérez', 'pedro.perez@email.com'); | Funciona                                                     |

En resumen, en esta tabla que acabamos de crear, el correo electronico debe ser unico, no ingresar dos personas con el mismo correo electronico.

Ejercicio:

En este ejercicio, vamos a crear una tabla llamada **productos** con las siguientes columnas:

| COLUMNA | TIPO DE DATO | RESTRICCIONES |
|---------|--------------|---------------|
| nombre  | TEXT         | NOT NULL      |
| codigo  | TEXT         | UNIQUE        |
| precio  | REAL         | NOT NULL      |

Y luego vamos a ingresar los siguientes registros:

| NOMBRE    | PRECIO  | CODIGO  |
|-----------|---------|---------|
| Camisa    | 1000.00 | CAM-001 |
| Pantalón  | 2000.00 | PAN-001 |
| Camisa XL | 1000.00 | CAM-002 |

> Pista: para poder ingresar las dos queries requeridas, recuerda añadir punto y coma al final de cada una.

> Si quieres probar un insert para observar el error puedes hacerlo con el código CAM-001.

```sql
CREATE  TABLE productos (
	nombre TEXT NOT  NULL,
	precio float  NOT  NULL,
	codigo TEXT UNIQUE
);
INSERT  INTO productos
VALUES
	('Camisa',  1000.00,  'CAM-001'),
	('Pantalón',  2000.00,  'PAN-001'),
	('CAmisa XL',  1000.00,  'CAM-002');
```
#### Añadiendo una restriccion `UNIQUE` a una tabla existente

Para añadir una restriccion `UNIQUE` a una table existente debemos usar el comando `ALTER TABLE`.

Aqui la sintaxis:

```sql
ALTER TABLE table_name
ADD UNIQUE (column1, column2, ...);
```

Aqui, `table_name` es el nombre de la tabla donde vamos a definir la restriccion, y `column1`, `column2` etc, son los nobres de las columnas incluidas en la restriccion.

### Resticciones con check
Hasta ahora hemos trabajado con dos tipos de restricciones:
* NOT NULL: que permite que un valor no pueda ser nulo
* UNIQUE: que permite especificar que un valor debe ser único.

En este ejercicio aprederemos a utilizar la restriccion `CHECK`, que nos permite establecer una condicion que los valores de una columna se deben cumplir.
`CHECK`limita el rango de valores que son colocados en una columna.
Aqui la sintaxis basica

```sql
CREATE TABLE table_name (
	column1 datatype CONSTRAINT constraint_name CHECK (condition)
	column2 datatype
```

Para agregar una restriccion de CHECK, simplemente tenemos que especifcar en la definicion de la columna proporcionando la condicion que debe cumplir el valor de la columna. Por ejemplo:

```sql
CREATE TABLE empleados (
	nombre TEXT,
	salario REAL CHECK (salario > 0)
);
```
Ejercicio:
En este ejercicio vamos a crear una tabla llamada **productos** con las siguientes columnas:

| COLUMNA | TIPO DE DATO | RESTRICCIONES      |
|---------|--------------|--------------------|
| nombre  | TEXT         | NOT NULL           |
| precio  | REAL         | NOT NULL           |
| stock   | INTEGER      | CHECK (stock >= 0) |

Luego, vamos a insertar los siguientes registros:

| NOMBRE    | PRECIO  | STOCK |
|-----------|---------|-------|
| Camisa    | 1000.00 | 10    |
| Pantalón  | 2000.00 | 5     |
| Camisa XL | 1000.00 | 3     |

> Pista: para poder ingresar las dos queries requeridas, recuerda añadir punto y coma al final de cada una.

> Si quieres probar un insert para observar el error puedes hacerlo ingresando un stock negativo.

```sql
CREATE  TABLE productos (
	nombre TEXT NOT  NULL,
	precio float  NOT  NULL,
	stock integer  CHECK  (stock >=  0)
);
INSERT  INTO productos
VALUES
	('Camisa',  1000.00,  10),
	('Pantalón',  2000.00,  5),
	('Camisa XL',  1000.00,  3)
```
Si queremos aplicar `CHECK` a multiples columnas:

```sql
CREATE TABLE employees (
	ID int NOT NULL,
	Age int,
	Salary int,
	CONSTRAINT chk_person CHECK (Age >= 18 AND Salary>=0)
```
Tambien es posible usar el comando `ALTER TABLE`para añadir una restriccion  `CHECK` despues que la tabla fue creada

```sql
ALTER TABLE Employees
ADD CONSTRAINT CHK_EmployeeAge CHECK (Age >= 21 and Age <= 60)
```

### Clave Unica
La clave primaria, o en ingles **PRIMARY KEY** nos ayuda a identofocar de forma unica cada registro en una tabla. Esto lo hace impidiendo que se ingresen valores duplicados o nulos en la columna que es la clave primaria.

| ID | MONTO DE LA BOLETA | FECHA DE EMISION |
|----|--------------------|------------------|
| 1  | 10.000             | 2021-10-01       |
| 2  | 12.000             | 2021-10-02       |
| 3  | 16.000             | 2021-10-03       |

Si dijeramos que el campo **id** es la clave primaria, entonces cada registro de la tabla tiene un valor unico para el campo **id** . Este id no podria ser nulo ni podria ser el mismo que el de otro registro.

Cuando tenemos una clave primaria, tenemos certeza que podemos buscar cualquier registro en la base de datos y luego modificarlo o eliminarlo, y no habrá ningun otro registro modificado o elominado que el seleccionado. Esto nos permite cuidar la integridad de los datos.

Podemos definir una clave primaria en SQL cuando creamos o modificamos una tabla.
```sql
CREATE TABLE Employees (
	ID INT PRIMARY KEY,
	NAME TEXT,
	AGE INT,
	ADDRESS CHAR(50)
); 
```

Ejercicio:
Crea una tabla llamada POSTS con las siguientes columnas:

| COLUMN NAME | DATA TYPE | CONSTRAINTS |
|-------------|-----------|-------------|
| id          | INT       | PRIMARY KEY |
| title       | TEXT      |             |
| content     | TEXT      |             |

inserta los siguientes registros

| ID | TITLE           | CONTENT                                                 |
|----|-----------------|---------------------------------------------------------|
| 1  | Introducción    | ¡Bienvenido al mundo de la programación!                |
| 2  | Primeros Pasos  | Sumérgete en los conceptos básicos de la programación.  |
| 3  | Temas Avanzados | Explora conceptos y técnicas avanzadas en programación. |

> Pista: para poder ingresar las dos queries requeridas, recuerda añadir punto y coma al final de cada una.

> Si quieres poner a prueba la clave primaria puedes intentar insertar un id nulo o un id que ya hayas ingresado.

```sql
CREATE  TABLE POSTS (
	ID INT  PRIMARY  KEY,
	TITLE TEXT,
	CONTENT TEXT
);
INSERT  INTO POSTS
VALUES
	(1,  'Introducción',  '¡Bienvenido al mundo de la programación!'),
	(2,  'Primeros Pasos',  'Sumérgete en los conceptos básicos de la programación.'),
	(3,  'Temas Avanzados',  'Explora conceptos y técnicas avanzadas en programación.')
```

### Autoincremental
Los campos autoincrementales nos permite generar un valor unico de forma automatica, para cada registro que insertemos en una tabla

De esta forma si tenemos una tabla como la siguiente

| ID | MONTO DE LA BOLETA | FECHA DE EMISION |
|----|--------------------|------------------|
| 1  | 10.000             | 2021-10-01       |
| 2  | 12.000             | 2021-10-02       |
| 3  | 16.000             | 2021-10-03       |

Podemos ingresar un nuevo registro sin tener que especificar el valor del campo id, y la base de datos se encargará de generar un valor unico para ese campo. Para lograrlo simplemente no incluimos el campo id en la query

Ejemplo:

```sql
INSERT INTO boletas (monto_de_la_boleta, fecha_de_emision)
VALUES 
	(20.000, '2021-10-04')
```

Luego si seleccionamos todos los registros de la tabla, veremos que el campo id del nuevo registro tiene un valor unico y mayor al de los registros anteriores.

| ID | MONTO DE LA BOLETA | FECHA DE EMISION |
|----|--------------------|------------------|
| 1  | 10.000             | 2021-10-01       |
| 2  | 12.000             | 2021-10-02       |
| 3  | 16.000             | 2021-10-03       |
| 4  | 20.000             | 2021-10-04       |

Un campo definido como `INTEGER`(o INT) + `PRIMARY KEY` se convierte automaticamente en un campo autoincremental en SQLite.

Ejercicio:

Crea una tabla llamada usuarios con las siguientes columnas:

| COLUMNA        | TIPO DE DATO | RESTRICCIONES |
|----------------|--------------|---------------|
| id             | INTEGER      | PRIMARY KEY   |
| nombre         | TEXT         | NOT NULL      |
| fecha_creacion | DATE         |               |

Luego vamos a insertar los siguientes registros

| NOMBRE  | FECHA_CREACION |
|---------|----------------|
| Ana     | 2024-01-01     |
| Gonzalo | 2024-01-02     |
| Juan    | 2024-01-03     |
| María   | 2024-01-04     |

> Pista: No ingreses los ids, la base de datos se encargará de generarlos automáticamente.

```sql
CREATE  TABLE USUARIOS (
	ID INTEGER  PRIMARY  KEY,
	NOMBRE TEXT NOT  NULL,
	FECHA_CREACION DATE
);
INSERT  INTO USUARIOS (NOMBRE, FECHA_CREACION)
VALUES
	('Ana',  '2024-01-01'),
	('Gonzalo',  '2024-01-02'),
	('Juan',  '2024-01-03'),
	('María',  '2024-01-04')
```

Resultado:

| ID | NOMBRE  | FECHA_CREACION |
|----|---------|----------------|
| 1  | Ana     | 2024-01-01     |
| 2  | Gonzalo | 2024-01-02     |
| 3  | Juan    | 2024-01-03     |
| 4  | María   | 2024-01-04     |

### Autoincremental parte 2
Cuando tenemos campos autoincrementales en una tabla e insertamos un nuevo registro con valor mas alto que el de la secuencia actual, la base de datos se encarga de actualizar la secuencia para que el siguiente registro tenga un valor al del registro que acabamos de insertar. 

Por ejemplo, si tenemos una tabla con los siguientes registros:

| ID | NOMBRE  |
|----|---------|
| 1  | Ana     |
| 2  | Gonzalo |
| 3  | Juan    |

Luego insertamos un nuevo registro coin un id mayor al de la secuencuia actual:

```sql
INSERT INTO usuarios (id, nombre)
VALUES (10, 'María')
```

Y luego insertamos un nuevo registro sin especificar el id:

```sql
INSERT INTO usuarios (nombre)
VALUES ('Pedro')
```

Obtendremos la siguiente tabla

| ID | NOMBRE  |
|----|---------|
| 1  | Ana     |
| 2  | Gonzalo |
| 3  | Juan    |
| 10 | María   |
| 11 | Pedro   |

Ejercicio:

Crea una tabla llamada **transacciones** con las siguientes columna:

| COLUMNA | TIPO DE DATO | RESTRICCIONES |
|---------|--------------|---------------|
| id      | INTEGER      | PRIMARY KEY   |
| monto   | REAL         | NOT NULL      |
| fecha   | DATE         |               |

Luego vamos a insertar los siguientes registros:

| ID | MONTO   | FECHA      |
|----|---------|------------|
|    | 1000.00 | 2024-01-01 |
|    | 2000.00 | 2024-01-02 |
|    | 3000.00 | 2024-01-03 |
| 10 | 4000.00 | 2024-01-04 |
|    | 5000.00 | 2024-01-05 |

> **Importante**: Al único campo que vamos a agregar un id de forma personalizada va a ser al cuarto registro, esto con el fin de observar la relación que se genera entre el campo incremental y como aumenta según el valor que insertemos.

```sql
CREATE  TABLE TRANSACCIONES (
	ID INTEGER  PRIMARY  KEY,
	MONTO FLOAT  NOT  NULL,
	FECHA DATE
);
INSERT  INTO TRANSACCIONES (MONTO, FECHA)
VALUES
	(1000.00,  '2024-01-01'),
	(2000.00,  '2024-01-02'),
	(3000.00,  '2024-01-03');
INSERT  INTO TRANSACCIONES (ID, MONTO, FECHA)
VALUES
	(10,  4000.00,  '2024-01-04');
INSERT  INTO TRANSACCIONES (MONTO, FECHA)
VALUES
	(5000.00,  '2024-01-05');
```

Resultado:

| ID | MONTO | FECHA      |
|----|-------|------------|
| 1  | 1000  | 2024-01-01 |
| 2  | 2000  | 2024-01-02 |
| 3  | 3000  | 2024-01-03 |
| 10 | 4000  | 2024-01-04 |
| 11 | 5000  | 2024-01-05 |

### Primary key y texto
La clave primaria no está limitada exclusivamente a valores numericos, tambien se pueden tilizar datos de texto. Tomemos, por ejemplo, una tabla de personas, donde podriamos emplear la direccion de correo electronico como la clave primaria, ya que cada individuo posee una direccion de correo única.

En SQLite, los campos que son de tipo INTEGER y se designan como PRIMARY KEY no pueden contener valores nulos. No obstante, a diferencia de otros sistemas de gestion de bases de datos como MySQL o POstgreSQL cuando se utiliza PRIMARY KEY con tipos de datos como texto u otros, se permite que el valor sea nulo.

POr lo tanto, si queremos que un campo sea tanto clave primaria como no nulo, debemos especificarlo metemante la combinacion de PRIMARY KEY y NOT NULL

Ejemplo:

```sql
CREATE TABLE posts (
	title TEXT PRIMARY KEY NOT NULL
)
```

Ejercicio:

Crea una tabla llamada **personas** con las siguientes columnas:

| COLUMN NAME | DATA TYPE | CONSTRAINTS          |
|-------------|-----------|----------------------|
| email       | TEXT      | PRIMARY KEY NOT NULL |
| nombre      | TEXT      |                      |
| apellido    | TEXT      |                      |

Inserta los siguientes registros:

| EMAIL                | NOMBRE | APELLIDO |
|----------------------|--------|----------|
| example1@example.com | John   | Doe      |
| example2@example.com | Jane   | Smith    |
| example3@example.com | Mike   | Johnson  |

> Puedes probar usando el mismo email en dos registros diferentes para que observes como se comporta la restricción.

```sql
CREATE  TABLE PERSONAS (
	EMAIL TEXT PRIMARY  KEY  NOT  NULL,
	NOMBRE TEXT,
	APELLIDO TEXT
);
INSERT  INTO PERSONAS
VALUES
	('example1@example.com',  'John',  'Doe'),
	('example2@example.com',  'Jane',  'Smith'),
	('example3@example.com',  'Mike',  'Johnson')
```

### Clave foránea
Una clave Foránea (Foreign Key)  es usada para enlazar dos tablas juntas. Es una restriccion que se le puede agregar a una columna de una tabla para indicar que los valores que se inserten en esa columna deben existir en otra tabla.
Por ejemplo: si tenemos una tabla de personas y una tabla de autos, podriamos agregar una columna **personas_id** a la tabla de autos, y agregarle la resticcion de clave foránea, para indicar que el valor de esa columna debe existir en la tabla de personas. De esta forma nos aseguramos que  no se inserten autos de personas que no existen o que se borren personas que tienen autos asignados a su nombre, dejando autos sin dueño.

**personas**
| COLUMNA  | TIPO DE DATO | RESTRICCIONES |
|----------|--------------|---------------|
| id       | INTEGER      | PRIMARY KEY   |
| nombre   | TEXT         |               |
| apellido | TEXT         |               |

**autos**

| COLUMNA    | TIPO DE DATO | RESTRICCIONES                                    |
|------------|--------------|--------------------------------------------------|
| id         | INTEGER      | PRIMARY KEY                                      |
| patente    | TEXT         |                                                  |
| persona_id | INTEGER      | FOREIGN KEY (persona_id) REFERENCES personas(id) |

Con los siguientes datos:

**personas**
| ID | NOMBRE | APELLIDO |
|----|--------|----------|
| 1  | John   | Doe      |
| 2  | Jane   | Smith    |

**autos**
| ID | PATENTE | PERSONA_ID |
|----|---------|------------|
| 1  | ABC123  | 1          |
| 2  | DEF456  | 2          |


Podemos ver que el auto con patente **ABC123** pertenece a la persona con el id **1**, y el auto con patente **DEF456** pertenece a la persona con el id **2**. Adicionalmente, la clave foranea nos asegura que no podemos borrar la persona con el id 1, mientras que exista un aut con persona_id 1. De esta misma forma, no podremos insertar un auto con persona_id 3 ya que no existe una persona copn id 3

#### Agregando clave foránea

Para agregar una clave foranea a una tabla existente, debemos especificar la restriccion `FOREIGN KEY` seguida del nombre de la columna y la tabla a la que hace referencia y finalmente la columna de la tabla a la que hace referencia.

La sintaxis es la siguiente

```sql
ALTER TABLE nombre_tabla
ADD COLUMN nombre_columna tipo_dato REFERENCES nombre_tabla_referencia(nombre_columna_referencia)
```

Se ve complicado, pero veamos un ejemplo con las tablas **personas** y **autos**

```sql
ALTER TABLE autos
ADD COLUMN personas_id INTEGER REFERENCES personas(id)
```

La clave foránea debe hacer referencia a una columna que ya tenga una restriccion de **clave primaria**.


Otra sintaxis, extraida de [roadmap.sh](https://roadmap.sh/sql)

```sql
ALTER TABLE child_table
ADD FOREIGN KEY (fk_column)
REFERENCES parent_table(parent_key_column)
```

Ejercicio:

Se tiene las tablas **articulos**  y **categorias** con la siguiente estructura

**articulos**

| COLUMNA | TIPO DE DATO | RESTRICCIONES |
|---------|--------------|---------------|
| id      | INTEGER      | PRIMARY KEY   |
| nombre  | TEXT         |               |
| precio  | REAL         |               |

**Categorias**

| COLUMNA | TIPO DE DATO | RESTRICCIONES |
|---------|--------------|---------------|
| id      | INTEGER      | PRIMARY KEY   |
| nombre  | TEXT         |               |

Se pide agregar una clave foránea a la tabla **articulos** para que la columna **categoria_id** haga referencia a la columna **id** de la tabla **categorias**.

```sql
ALTER  TABLE articulos
ADD  COLUMN categoria_id INTEGER  REFERENCES categorias(id)
```

### Pk y Fks

Los conceptos de clave primaria y clave foránea son fundamentales para el diseño de bases de datos y los ocuparemos tan frecuentemente que los abreviaremos PK (primary key) y FK (foreign key).
Con la clave primaria podemos identificar de forma unica cada registro de una tabla, y con la clave foranea podemos relacionar dos tablas entre si y evitar que existan registros que no tengan una relacion valida.

A partir de ahora utilizaremos frecuentemente las abreviaciones (PK y FK). Tambien veremos que casi todas las tablas tendran una clave primaria. **Esto se debe a que la clave primaria nos ayuda a mantener la integridad de los datos y nos permite identificar de forma unica cada registro de una tabla**

Una practica comun en el diseño de base de datos es utilizar una columna llamada **id** como *PK*. Esta columna es de tipo **INTEGER** y tiene la resticcion `PRIMARY KEY` . Ademas, es comun que esta columna sea autoincremental, es decir, que el valor de la columna se incremente automaticamente cada vez que se inserta un registro nuevo. Pero esto *no es una obigacion*. Definir una clave primaria es una decision de diseño y en algunos casos puede ser mas conveniente utilizar otra columna como clave primaria.

Ejercicio:

Se tiene la tabla **transacciones** y la tabla **usuarios** con la siguiente estructura:


**transacciones**

| COLUMNA    | TIPO DE DATO | RESTRICCIONES                                    |
|------------|--------------|--------------------------------------------------|
| id         | INTEGER      | PRIMARY KEY                                      |
| monto      | REAL         |                                                  |
| usuario_id | INTEGER      | FOREIGN KEY (usuario_id) REFERENCES usuarios(id) |

**Usuraios**

| COLUMNA  | TIPO DE DATO | RESTRICCIONES |
|----------|--------------|---------------|
| id       | INTEGER      | PRIMARY KEY   |
| nombre   | TEXT         |               |
| apellido | TEXT         |               |


Con los siguientes datos:
**transacciones**

| ID | MONTO | USUARIO_ID |
|----|-------|------------|
| 1  | 100   | 1          |
| 2  | 200   | 2          |
| 3  | 300   | 1          |

**usuarios**

| ID | NOMBRE | APELLIDO |
|----|--------|----------|
| 1  | John   | Doe      |
| 2  | Jane   | Smith    |

1.  En este ejercicio primero intentaremos crear una transacción con un usuario que no existe para observar el error.
    
2.  Intentaremos borrar un usuario que tiene transacciones asociadas para observar el error.
    
3.  Luego eliminaremos nuestras consultas anteriores y modificaremos la tabla de transacciones para eliminar la clave foránea. Solo se debe eliminar la clave foránea, no la columna.
    

> TIP: Esto requiere crear una tabla temporal, copiar los datos de la tabla original a la tabla temporal, borrar la tabla original, y renombrar la tabla temporal con el nombre de la tabla original.

4.  Finalmente se deben asociar las transacciones al usuario con id 3. El cual no existe y la idea es demostrar que sin la FK podemos insertar transacciones sin usuarios asociados.

> Los puntos 1 y 2 son para observar que sucede. Para lograr la respuesta correcta tienes que realizar los puntos 3 y 4 en el editor.

```sql
-- Creamos una tabla copia
CREATE  TABLE transacciones2(
id INTEGER  PRIMARY  KEY,
monto float,
usuario_id INTEGER
);
-- Insertamos los valores originales a la tabla copia
INSERT  INTO transacciones2(id, monto, usuario_id)
SELECT  *
FROM transacciones;
-- Eliminamos la tabla original
DROP  TABLE transacciones;
-- Renombramos la tabla copia al nombre original
ALTER  TABLE transacciones2 RENAME  TO transacciones;
-- Colocamos todas las transcaciones con un valor de usuario_id 3
UPDATE transacciones
SET usuario_id =  3
```
## Tema 17: Consultas en multiples tablas

:arrow_up: [ir al inicio](.#tabla-de-contenidos)

Cuando trabajamos con bases de datos relacionales, surge con frecuencia la necesidad de combinar datos de varias tablas:

Veamos un ejemplo:

Tabla usuarios:
| EMAIL1                     | NOMBRE         | EDAD |
|----------------------------|----------------|------|
| juan.perez@example.com     | Juan Pérez     | 30   |
| maria.gonzalez@example.com | Maria González | 25   |
| john.doe@example.com       | John Doe       | 40   |
| test.user@example.com      | Test User      | 22   |

Tablas datos_contacto
| EMAIL2                     | TELÉFONO     |
|----------------------------|--------------|
| juan.perez@example.com     | 555-123-4567 |
| maria.gonzalez@example.com | 444-987-6543 |
| john.doe@example.com       | 777-555-8888 |
| test.user@example.com      | 111-222-3333 |
| juan.perez@example.com     | 999-888-7777 |
| maria.gonzalez@example.com | 333-111-0000 |

Si nos piden obtener todos los email, nombre, edad y telefono de todos los usuarios, tendriamos que unir estas tablas . PAra esto existe la clausula `JOIN`

En nuestro ejemplo, podemos unir las tablas con la siguiente consulta
```sql
SELECT *
FROM USUARIOS
JOIN datos_contacto
ON email1 = email2
```

Para unir tablas tenemos que establecer un punto de union. En este caso, lo que tienen en comun ambas tablas es el email.

Ejercicio:

Utilizando lo aprendido, selecciona todos los usuarios junto a sus notas. Observa los resultados antes de avanzar.

Tabla Usuarios:

| EMAIL1                     | NOMBRE         | EDAD |
|----------------------------|----------------|------|
| juan.perez@example.com     | Juan Pérez     | 30   |
| maria.gonzalez@example.com | Maria González | 25   |
| john.doe@example.com       | John Doe       | 40   |
| test.user@example.com      | Test User      | 22   |

Tabla Notas:
| EMAIL2                     | NOTAS |
|----------------------------|-------|
| juan.perez@example.com     | 90    |
| maria.gonzalez@example.com | 100   |
| john.doe@example.com       | 80    |
| test.user@example.com      | 0     |
| juan.perez@example.com     | 100   |
| maria.gonzalez@example.com | 100   |

```sql
SELECT  *
FROM USUARIOS
JOIN NOTAS ON EMAIL1 = EMAIL2
```

## Multiples tablas: utilizando atributo del mismo nombre

En el ejercicio anterior teniamos los atributos emain1 y email2. En este ejercicio aprenderemos que es posible que dos atributos distinyos compartan el mismo nombre, siempre y cuando esten ubicados en diferentes tablas.

Para emeplificar este ejercicio, utilizaremos el nombre email en ambas tablas.

Tabla Usuarios:
| EMAIL                      | NOMBRE         | EDAD |
|----------------------------|----------------|------|
| juan.perez@example.com     | Juan Pérez     | 30   |
| maria.gonzalez@example.com | Maria González | 25   |
| john.doe@example.com       | John Doe       | 40   |
| test.user@example.com      | Test User      | 22   |

Tabla datos_contacto

| EMAIL                      | TELÉFONO     |
|----------------------------|--------------|
| juan.perez@example.com     | 555-123-4567 |
| maria.gonzalez@example.com | 444-987-6543 |
| john.doe@example.com       | 777-555-8888 |
| test.user@example.com      | 111-222-3333 |
| juan.perez@example.com     | 999-888-7777 |
| maria.gonzalez@example.com | 333-111-0000 |


Uniremos los datos de ambas tablas utilizando `JOIN` pero en esta ocasion cuando especifiquemos el punto de union, utilizaremos el nombre de la tabla junto con el del atributo

```sql
SELECT *
FROM USUARIOS
JOIN DATOS_CONTACTO ON USUARIOS.EMAIL = DATOS_CONTACTO.EMAIL
```

Al hacerlo de esta forma, SQL puede entender a cual email nos referimos en cada situacion.

Ejercicio:

Utilizando lo aprendido, selecciona todos los usuarios junto a sus notas. Recuerda que para especificar la clave de union debes utilizar el nombre de la tabla para evitar ambiguedad. Observa los resultados antes de avanzar:

Tabla Usuarios:

| EMAIL                      | NOMBRE         | EDAD |
|----------------------------|----------------|------|
| juan.perez@example.com     | Juan Pérez     | 30   |
| maria.gonzalez@example.com | Maria González | 25   |
| john.doe@example.com       | John Doe       | 40   |
| test.user@example.com      | Test User      | 22   |

Tabla Notas:
| EMAIL                      | NOTAS |
|----------------------------|-------|
| juan.perez@example.com     | 90    |
| maria.gonzalez@example.com | 100   |
| john.doe@example.com       | 80    |
| test.user@example.com      | 0     |
| juan.perez@example.com     | 100   |
| maria.gonzalez@example.com | 100   |

```sql
SELECT  *
FROM USUARIOS
JOIN NOTAS ON USUARIOS.EMAIL = NOTAS.EMAIL
```

Resultado:

| EMAIL                      | NOMBRE         | EDAD | EMAIL                      | NOTAS |
|----------------------------|----------------|------|----------------------------|-------|
| juan.perez@example.com     | Juan Pérez     | 30   | juan.perez@example.com     | 90    |
| maria.gonzalez@example.com | Maria González | 25   | maria.gonzalez@example.com | 100   |
| john.doe@example.com       | John Doe       | 40   | john.doe@example.com       | 80    |
| test.user@example.com      | Test User      | 22   | test.user@example.com      | 0     |
| juan.perez@example.com     | Juan Pérez     | 30   | juan.perez@example.com     | 100   |
| maria.gonzalez@example.com | Maria González | 25   | maria.gonzalez@example.com | 100   |

### Seleccionando algunos atributos
Si tenemos dos tablas, como la de los ejecicios anteriores

Tabla Usuarios:
| EMAIL                      | NOMBRE         | EDAD |
|----------------------------|----------------|------|
| juan.perez@example.com     | Juan Pérez     | 30   |
| maria.gonzalez@example.com | Maria González | 25   |
| john.doe@example.com       | John Doe       | 40   |
| test.user@example.com      | Test User      | 22   |

Tabla datos_contacto

| EMAIL                      | TELÉFONO     |
|----------------------------|--------------|
| juan.perez@example.com     | 555-123-4567 |
| maria.gonzalez@example.com | 444-987-6543 |
| john.doe@example.com       | 777-555-8888 |
| test.user@example.com      | 111-222-3333 |
| juan.perez@example.com     | 999-888-7777 |
| maria.gonzalez@example.com | 333-111-0000 |


Puede ser que al seleccionar los datos no deseemos mostrar los  emails dos veces. Para esto, en lugar de utilizar `SELECT *` utilizaremos

```sql
SELECT USUARIOS.*, DATOS_CONTACTO.TELEFONO
FROM USUARIOS
JOIN DATOS_CONTACTO ON USUARIOS.EMAIL = DATOS_CONTACTO.EMAIL
```

De esta forma, seleccionamos todo lo de la tabla usuarios y solo los telefonos de la tabla datos_contacto

Ejercicio:

Dada la siguiente tabla:

Tabla Usuarios:

| EMAIL                      | NOMBRE         | EDAD |
|----------------------------|----------------|------|
| juan.perez@example.com     | Juan Pérez     | 30   |
| maria.gonzalez@example.com | Maria González | 25   |
| john.doe@example.com       | John Doe       | 40   |
| test.user@example.com      | Test User      | 22   |

Tabla Notas:
| EMAIL                      | NOTAS |
|----------------------------|-------|
| juan.perez@example.com     | 90    |
| maria.gonzalez@example.com | 100   |
| john.doe@example.com       | 80    |
| test.user@example.com      | 0     |
| juan.perez@example.com     | 100   |
| maria.gonzalez@example.com | 100   |

Selecciona de la tabla **usuarios** el email, nombre y edad y de la tabla **notas** sólo las notas. Une los registros de ambas tablas utilizando el email.

```sql
SELECT USUARIOS.*, NOTAS.NOTAS
FROM USUARIOS
JOIN NOTAS ON USUARIOS.EMAIL = NOTAS.EMAIL
```

Resultado:

| EMAIL                      | NOMBRE         | EDAD | NOTAS |
|----------------------------|----------------|------|-------|
| juan.perez@example.com     | Juan Pérez     | 30   | 90    |
| maria.gonzalez@example.com | Maria González | 25   | 100   |
| john.doe@example.com       | John Doe       | 40   | 80    |
| test.user@example.com      | Test User      | 22   | 0     |
| juan.perez@example.com     | Juan Pérez     | 30   | 100   |
| maria.gonzalez@example.com | Maria González | 25   | 100   |

### Join sin resultados
¿Que sucederia si los emails presentes en una tabla no se encuentran en la otra tabla al momento de unir los datos?

Tabla usuarios:

| EMAIL                      | NOMBRE         | EDAD |
|----------------------------|----------------|------|
| juan.perez@example.com     | Juan Pérez     | 30   |
| maria.gonzalez@example.com | Maria González | 25   |
| john.doe@example.com       | John Doe       | 40   |
| test.user@example.com      | Test User      | 22   |

Tabla datos_contacto

| EMAIL                        | TELÉFONO     |
|------------------------------|--------------|
| alvaro.sanchez@example.com   | 555-123-4567 |
| maria.fernandez@example.com  | 444-987-6543 |
| francisca.medina@example.com | 777-555-8888 |

LA respuesta es sencilla, si no hay ningun dato entre ambas tablas, no obtendremos resultados

Utilizando lo aprendido previamente, selecciona todos los registros de la union de las tablas **usuarios** y **datos_contacto**

```sql
SELECT  *
FROM USUARIOS
JOIN DATOS_CONTACTO ON USUARIOS.EMAIL = DATOS_CONTACTO.EMAIL
```

### Orden de Clausulas

Cuando queremos utilizar *joins* con las otras clausulas que hemos aprendido, tenemos que considerar el orden de estas.

En la siguiente tabla se muestra el orden que debemos seguir:

| COMANDO  | SE LEE COMO:                                  |
|----------|-----------------------------------------------|
| SELECT   | Selecciona estos datos.                       |
| FROM     | De esta tabla.                                |
| JOIN     | Únelos con esta tabla.                        |
| WHERE    | Filtra los valores que cumplan tal condición. |
| GROUP BY | Agrupa los resultados por este criterio.      |
| HAVING   | Filtra por estos criterios agrupados.         |
| ORDER BY | Ordena los resultados por este otro criterio. |
| LIMIT    | Limita los resultados a esta cantidad.        |

Ejercicio:

Dada las siguientes tablas, selecciona toda la informacion del usuario **juan.perez@example.com**

Tabla usuarios:

| EMAIL                      | NOMBRE         | EDAD |
|----------------------------|----------------|------|
| juan.perez@example.com     | Juan Pérez     | 30   |
| maria.gonzalez@example.com | Maria González | 25   |
| john.doe@example.com       | John Doe       | 40   |
| test.user@example.com      | Test User      | 22   |

Tabla notas

| EMAIL                      | NOTAS |
|----------------------------|-------|
| juan.perez@example.com     | 90    |
| maria.gonzalez@example.com | 100   |
| john.doe@example.com       | 80    |
| test.user@example.com      | 0     |
| juan.perez@example.com     | 100   |
| maria.gonzalez@example.com | 100   |

> Pista: debes seleccionar todo, unir las tablas y filtrar por el email respectivo

```sql
SELECT  *
FROM USUARIOS
JOIN NOTAS ON USUARIOS.EMAIL = NOTAS.EMAIL
WHERE USUARIOS.EMAIL =  'juan.perez@example.com'
```

Resultado:

| EMAIL                  | NOMBRE     | EDAD | EMAIL                  | NOTAS |
|------------------------|------------|------|------------------------|-------|
| juan.perez@example.com | Juan Pérez | 30   | juan.perez@example.com | 90    |
| juan.perez@example.com | Juan Pérez | 30   | juan.perez@example.com | 100   |

### Agrupar por multiples columnas
Al igual que en las consultas sobre una tabla, podemos utilizar funciones de agregacion y agrupando en consultas sobre multiples tablas.

Supongamos qye teeos dos tablas, una tabla llamada **Clientes** que almacena informacon soibre los clientes y otra llamada Pedidos que almacena informacion sobre los pedidos realizados por esos clientes. Queremos realizar una consulta que nos muestre la cantidad total de pedidos realizados por cada cliente. Para esto ejecutaremos una consulta que utilice la clausula `GROUP BY` para agrupar los pedidos por cliente y contaremos la cantidad total de pedidos para cada cliente

```sql
SELECT c.Nombre AS NombreCliente, COUNT(p.PedidoID) AS TotalPedidos
FROM Clientes c
JOIN Pedidos p on c.ClienteID = p.ClienteID
GROUP BY c.ClienteID
```

Ejercicio:

Tenemos dos tablas, **productos** y **ventas**. Realiza una consulta que nos muestre el producto mas vendido y la cantidad total de unidades vendidas de ese producto. La columna que muestre el total de unidades vendidas debe llamarse **total_vendido**

> Pista: recuerda el uso de ORDER BY y LIMIT

Tabla Productos:

| NOMBRE     | PRECIO | PRODUCTOID |
|------------|--------|------------|
| Producto A | 10     | 1          |
| Producto B | 15     | 2          |
| Producto C | 20     | 3          |

Tabla Ventas:

| CANTIDAD | FECHAVENTA   | PRODUCTOID |
|----------|--------------|------------|
| 20       | '2023-09-01' | 1          |
| 15       | '2023-09-02' | 1          |
| 10       | '2023-09-03' | 2          |
| 25       | '2023-09-04' | 3          |
| 30       | '2023-09-05' | 3          |

```sql
SELECT P.NOMBRE AS NOMBRE,  SUM(V.CANTIDAD)  AS TOTAL_VENDIDO
FROM PRODUCTOS P
JOIN VENTAS V ON P.PRODUCTOID = V.PRODUCTOID
GROUP  BY P.PRODUCTOID
ORDER  BY  2  DESC
LIMIT  1
```

Resultado:

|Nombre| TOTAL_VENDIDO  |
|--|--|
| PRODUCTO C | 55 |

## Tema 18: Tipos de join

:arrow_up: [ir al inicio](.#tabla-de-contenidos)

## INNER JOIN

La clausula `INNER JOIN` en SQL es un tipo de union que retorna los registros coincidentes en ambas tablas. Esta operacion compara cada fila de la primera tabla con cada fila de la segunda tabla para encontrar todos los pares de filas que satisfaga la condicion.

Cuando no se especifica el punto de JOIN en la consulta, por defecto sera `INNER JOIN`

Es decir:
```sql
SELECT *
FROM USUARIOS
JOIN DATOS_CONTACTO ON USUARIOS.EMAIL = USUARIOS.EMAIL
```

es lo mismo que decir:

```sql
SELECT *
FROM USUARIOS
INNER JOIN DATOS_CONTACTO ON USUARIOS.EMAIL = DATOS_CONTACTO.EMAIL
```

* Es el `JOIN`por defecto en SQL. Si mencionamos `JOIN`sin especificar el tipo, SQL considerará que es un `INNER JOIN`
* Retorna solo las filas coincidentes en ambas tablas
* En una operación de Inner Join se combinan los registros de ambas tablas siempre y cuando la clave en común esté en ambas tablas. Si en una de las tablas no está la clave ese registro no aparecerá en el resutlado final.

Ejercicio:

Une las tablas utilizando JOIN (o INNER JOIN) para obtener todos los registros de ambas tablas. Mira las tablas antes de realizar el ejercicio y pon especial atención en Francisco quien no tiene ninguna nota en el sistema.

Tabla Usuarios:

| EMAIL                      | NOMBRE         | EDAD |
|----------------------------|----------------|------|
| juan.perez@example.com     | Juan Pérez     | 30   |
| maria.gonzalez@example.com | Maria González | 25   |
| john.doe@example.com       | John Doe       | 40   |
| francisco@example.com      | Test User      | 22   |

Tabla Notas:

| EMAIL                      | NOTAS |
|----------------------------|-------|
| juan.perez@example.com     | 90    |
| maria.gonzalez@example.com | 100   |
| john.doe@example.com       | 80    |
| juan.perez@example.com     | 100   |
| maria.gonzalez@example.com | 100   |

```sql
SELECT  *
FROM USUARIOS
INNER  JOIN NOTAS ON NOTAS.EMAIL = USUARIOS.EMAIL;
```


| EMAIL                      | NOMBRE         | EDAD | EMAIL                      | NOTAS |
|----------------------------|----------------|------|----------------------------|-------|
| juan.perez@example.com     | Juan Pérez     | 30   | juan.perez@example.com     | 90    |
| maria.gonzalez@example.com | Maria González | 25   | maria.gonzalez@example.com | 100   |
| john.doe@example.com       | John Doe       | 40   | john.doe@example.com       | 80    |
| juan.perez@example.com     | Juan Pérez     | 30   | juan.perez@example.com     | 100   |
| maria.gonzalez@example.com | Maria González | 25   | maria.gonzalez@example.com | 100   |

### Inner JOIN con diagrama de venn

Un diagrama de venn nos permite visualizar conjunts y operaciones entre ellos,. Estos diagramas se representan con circulos que repesentan conjuntos de datos, en ellos, los elementos que tienen en comun los conjuntos de datos se representan en la interseccion de los circulos.

Cuando trabajamos con bases de datos, podemos utilizar estos diagramas para visualizar los registros que se obtendrian al realizar los distintos tipos de `JOIN`.

Para hacerlo, pondremos como elementos las claves de union de las tablas. Los elementos que solo esten en la primera tabla, los representaremos en un circulo, los elementos que esten en la segunda tabla los representaremos en el segundo circulo, y los elementos que esten en ambas tablas los representaremos en la interseccion.

Ejemplo:

Tenemos la **tabla productos**

| id |   nombre   | precio |
|:--:|:----------:|:------:|
| 1  | Producto 1 | 100    |
| 2  | Producto 2 | 200    |
| 3  | Producto 3 | 300    |

**Tabla Ventas**

| id | id_producto | cantidad |
|:--:|:-----------:|:--------:|
| 1  | 3           | 2        |
| 2  | 4           | 2        |

Las claves en comun de estas tablas son `id` en **productos** y `id_producto` en **ventas**, estos los ponemos en el circulo de venn:

![circulo venn](https://tutorial-sql.s3.amazonaws.com/sql_images/3571_Inner+Join+con+diagrama+de+venn_15-Inner_Join_en_venn.png)

Para armar este diagrama, primero identificamos las claves de union de las tablas. Luego, en un circulo izquiero, que representa la tabla **productos** ponemos los registros 1, 2 y 3 asociados a la clave `id`. EN el circulo derecho, que representa la tabla **ventas** ponemos los registros 3 y 4 asociados a la clave `id_producto` , en la interseccion de ambos productos, ponemos el registro 3 ya que es el unico que se encuentra en ambas tablas.

Mirando el diagrama, y con lo que hemos aprendido, podemos decir que un `INNER JOIN` entre estas dos tablas nos devolvera el registro 3, ya que es el unico que se encuentra en ambas tablas. Es decir, un **inner join** nos regresa la interseccion de ambos conjuntos.

**Ejercicio**

Dada las siguientes tablas

Tabla **actores**

| actor_id |       nombre       |
|:--------:|:------------------:|
| 1        | Robert Downey Jr.  |
| 2        | Scarlett Johansson |
| 3        | Chris Hemsworth    |
| 4        | Mark Ruffalo       |
| 5        | Chris Evans        |

Tabla **peliculas**

| pelicula_id |      titulo     | actor_id |
|:-----------:|:---------------:|:--------:|
| 101         | Iron Man        | 1        |
| 102         | Avengers        | 1        |
| 103         | Black Widow     | 2        |
| 104         | Thor            | 3        |
| 105         | Avengers        | 3        |
| 106         | Avengers        | 4        |
| 107         | Avengers        | 5        |
| 108         | Captain America | 5        |



En un papel, dibuja un diagrama de Venn que muestre los registros que se obtendrían al realizar un INNER JOIN entre las tablas actores y peliculas.

En el editor de código a continuación, realiza una consulta que muestre el nombre de los actores y los títulos de las películas en las que han actuado.

¿El resultado del código coincide con tu dibujo?

![imagen](https://github.com/user-attachments/assets/4dd93bf6-cd51-407f-8494-eb36c791a3ac)

```sql
Select a.nombre, p.titulo
from actores as a
inner join peliculas as p 
ON a.actor_id = p.actor_id
```

### Left Join

La clausula `LEFT JOIN`combina filas de dos o mas tablas basado en una columna relacionada entre ellas, y retorna todas las filas desde la tabla de la izquierda (tabla 1) y las coincidencias de la tabla de la derecha (tabla 2). Si no hay coincidencias, el resultado es `NULL`en la tabla de la derecha.

![left join](https://github.com/borgesmj/notas-y-apuntes/assets/121818423/4c198d4d-d653-40e1-adde-77b5516d6f21)


Con los siguientes datos, al hacer un INNER JOIN no obtendremos dentro de los resultados a [**Francisco**](./#inner-join), lo cual podría ser un gran error si estuviésemos haciendo un reporte de todos los estutemantes.

Tabla usuarios:

| EMAIL                      | NOMBRE         | EDAD |
|----------------------------|----------------|------|
| juan.perez@example.com     | Juan Pérez     | 30   |
| maria.gonzalez@example.com | Maria González | 25   |
| john.doe@example.com       | John Doe       | 40   |
| francisco@example.com      | Test User      | 22   |

Tabla notas

| EMAIL                      | NOTAS |
|----------------------------|-------|
| juan.perez@example.com     | 90    |
| maria.gonzalez@example.com | 100   |
| john.doe@example.com       | 80    |
| juan.perez@example.com     | 100   |
| maria.gonzalez@example.com | 100   |

Con un `LEFT JOIN` todas las filas de la tabla de la izquierda (USUARIOS en este caso) apareceran en el resultado, y si un usuario no tiene una coincidencia en la tabla de la derecha (NOTAS), los campos correspondientes en la tabla de notas se llenaran con valores `NULL`.

La sintaxis para utilizar LEFT JOIN es similar a INNER JOIN 

```sql
SELECT *
FROM TABLA1
LEFT JOIN TABLA2 ON TABLA1.ATRIBUTO = TABLA2.ATRIBUTO
```
Ejemplo:
Asumamos que tenemos doa tablas: **Orders** y **Customers**

```sql
SELECT ORDERS.ORDERID, CUSTOMERS.CUSTOMERNAME
FROM ORDERS
LEFT JOIN CUSTOMERS
ON ORDERS.CUSTOMERID = CUSTOMERS.CUSTOMERID
```
Ejercicio:
Se tiene una tabla de empleados y otra de departamentos. Utilizando lo aprendido, selecciona a todos los empleados junto a sus departamentos correspondientes incluyendo a los empleados que aun no han sido asignados a ningun departamento. En ambas tablas existe la columna email

```sql
SELECT  *
FROM EMPLEADOS
LEFT  JOIN DEPARTAMENTOS ON EMPLEADOS.EMAIL = DEPARTAMENTOS.EMAIL
```

Resultado:

| EMAIL                      | NOMBRE         | EDAD | EMAIL                      | DEPARTAMENTO |
|----------------------------|----------------|------|----------------------------|--------------|
| juan.perez@example.com     | Juan Pérez     | 30   | juan.perez@example.com     | Marketing    |
| juan.perez@example.com     | Juan Pérez     | 30   | juan.perez@example.com     | RRHH         |
| maria.gonzalez@example.com | Maria González | 25   | maria.gonzalez@example.com |              |
| john.doe@example.com       | John Doe       | 40   | john.doe@example.com       | TI           |
| francisco@example.com      | Test User      | 22   |                            |              |

### Left Join en Diagrama de Venn

Armemos un diagrama de Venn

Tabla **productos**

| id |   nombre   | precio |
|:--:|:----------:|:------:|
| 1  | Producto 1 | 100    |
| 2  | Producto 2 | 200    |
| 3  | Producto 3 | 300    |

Tabla **ventas**

| id | id_producto | cantidad |
|:--:|:-----------:|:--------:|
| 1  | 3           | 2        |
| 2  | 4           | 2        |

Para armar este diagrama, repetimos los pasos que aprendimos previamente. Primero identificamos las claves de union de las tablas, Luego en un circulo izquierdo, representa la tabla **productos**, ponemos los registros 1, 2 y 3, asociados a la clave `id`. EN el circulo derechom que representa a la tabla **ventas** ponemos los registros 3 y 4 asociados a la clave `id_producto`. En la interseccion ds ambos  ponemos el registro 3, que es el unico que se encuentra en ambas tablas.

<img width="705" alt="3618_Left Join en diagrama de venn_leftJoin" src="https://github.com/user-attachments/assets/483bea39-0bb0-442e-ac11-3268c3fad664">

Cuando hacemos una operación de Left Join entre la tabla A y la tabla B, en los resultados aparecerán todos los registros de la tabla A, incluso aquellos que no tienen una clave correspondiente en la tabla B. O sea podemos visualizar el Left Join como el conjunto de la izquierda en un diagrama de Venn.

**Ejercicio**

Dadas las siguientes tablas:

**Tabla profesion**

| id |  Profesion |
|:--:|:----------:|
| 1  | Ingeniero  |
| 2  | Médico     |
| 3  | Abogado    |
| 4  | Arquitecto |

**Tabla Personas**

| id | Nombre | profesion_id |
|:--:|:------:|:------------:|
| 1  | Juan   | 1            |
| 2  | Maria  | 2            |
| 3  | Ana    | 3            |

Se tiene una tabla llamada Personas que contiene el nombre de las personas y el id de la profesión a la que pertenecen. Se quiere obtener un listado de todas las profesiones y las personas que pertenecen a cada una de ellas. Si una profesión no tiene personas asociadas, se debe mostrar el nombre de la profesión y NULL en el campo Nombre. La tabla resultante sólo debe contener dos columnas: Profesion y Nombre.

```SQL
SELECT PRO.PROFESION, PER.NOMBRE
FROM PROFESION AS PRO
LEFT JOIN PERSONAS AS PER
ON PRO.ID = PER.PROFESION_ID;
```

### Right Join
La clausula `RIGTH JOIN` retorna todos los registros de la tabla de la derecha (tabla 2) y los resultados coincidentes de la tabla de la izquierda (tabla 1). Si no hay coincidencias, el resultado será `NULL`en la tabla de la izquierda.

Utilizando las tablas previas de **usuarios** y **notas** si quieres obtener todos los registros de las notas y los correspondientes usuarios, incluso si hay notas que no tienen usuarios asociados (lo cual seria atipico en este contexto, pero sirve para el ejemplo) puede usar RIGHT JOIN.

```sql
SELECT *
FROM TABLA1
RIGHT JOIN TABLA2 ON TABLA1.ATRIBUTO = TABLA2.ATRIBUTO
```

Tabla usuarios

| EMAIL                      | NOMBRE         | EDAD |
|----------------------------|----------------|------|
| juan.perez@example.com     | Juan Pérez     | 30   |
| maria.gonzalez@example.com | Maria González | 25   |
| francisco@example.com      | Test User      | 22   |

Tabla notas:

| EMAIL                      | NOTAS |
|----------------------------|-------|
| juan.perez@example.com     | 90    |
| maria.gonzalez@example.com | 100   |
| juan.perez@example.com     | 100   |
| maria.gonzalez@example.com | 100   |
| emilio@example.com         | 90    |

En este ejemplo puntual **emilio@example.com ** tiene notas, pero no tenemos su registro en la tabla usuarios. Utilizando RIGHT JOIN podemos mostrar su informacion.

Ejercicio:

Dada las tablas **empleados** y **departamentos** se pide los registros de los departamentos de una oficina y sus correspondientes empleados, incluso si hay departamentos sin empleados asociados. En amas tablas existe la columna email.

```sql
SELECT  *
FROM EMPLEADOS
RIGHT  JOIN DEPARTAMENTOS ON EMPLEADOS.EMAIL = DEPARTAMENTOS.EMAIL
```

RESULTADO:
| EMAIL                  | NOMBRE     | EDAD | EMAIL                  | DEPARTAMENTO |
|------------------------|------------|------|------------------------|--------------|
| juan.perez@example.com | Juan Pérez | 30   | juan.perez@example.com | Marketing    |
| juan.perez@example.com | Juan Pérez | 30   | juan.perez@example.com | RRHH         |
|                        |            |      |                        | Finanzas     |
|                        |            |      | john.doe@example.com   | TI           |

### Left Join y Right Join

Utilizar LEFT JOIN y RIGHT JOIN depende simplemente de que tabla queremos nombrar primero:

```sql
SELECT *
FROM tabla1
LEFT JOIN tabla2 ON tabla1.id = tabla2.id
```

Es practicamete lo mismo que

```sql
SELECT *
FROM tabla1
RIGHT JOIN tabla2 ON tabla1.id = tabla2.id
```

LEFT JOIN y RIGHT JOIN son un reflejo uno del otrp, sin embargo, existe una pequeña diferencia cuando los utilizamos en conjunto con `SELECT *`, dado que los atributos de la primera tabla se mostraran primero.

Por ejemplo, si tenemos las siguientes tablas:

Usuarios 

| EMAIL                      | NOMBRE         | EDAD |
|----------------------------|----------------|------|
| juan.perez@example.com     | Juan Pérez     | 30   |
| maria.gonzalez@example.com | Maria González | 25   |
| francisco@example.com      | Test User      | 22   |

Notas:

| EMAIL                      | NOTAS |
|----------------------------|-------|
| juan.perez@example.com     | 90    |
| maria.gonzalez@example.com | 100   |
| juan.perez@example.com     | 100   |
| maria.gonzalez@example.com | 100   |
| emilio@example.com         | 90    |

Con 

```sql
SELECT *
FROM USUARIOS
LEFT JOIN NOTAS ON USUARIOS.EMAIL = NOTAS.EMAIL;
```

Nos regresa:

| EMAIL                      | NOMBRE         | EDAD | EMAIL                      | NOTAS |
|----------------------------|----------------|------|----------------------------|-------|
| juan.perez@example.com     | Juan Pérez     | 30   | juan.perez@example.com     | 90    |
| juan.perez@example.com     | Juan Pérez     | 30   | juan.perez@example.com     | 100   |
| maria.gonzalez@example.com | Maria González | 25   | maria.gonzalez@example.com | 100   |
| maria.gonzalez@example.com | Maria González | 25   | maria.gonzalez@example.com | 100   |
| francisco@example.com      | Test User      | 22   | NULL                       | NULL  |

En cambio, con

```sql
SELECT *
FROM NOTAS
RIGHT JOIN USUARIOS ON NOTAS.EMAIL = USUARIOS.EMAIL
```

Obtendremos:

| EMAIL                      | NOTAS | EMAIL                      | NOMBRE         | EDAD |
|----------------------------|-------|----------------------------|----------------|------|
| juan.perez@example.com     | 90    | juan.perez@example.com     | Juan Pérez     | 30   |
| juan.perez@example.com     | 100   | juan.perez@example.com     | Juan Pérez     | 30   |
| maria.gonzalez@example.com | 100   | maria.gonzalez@example.com | Maria González | 25   |
| maria.gonzalez@example.com | 100   | maria.gonzalez@example.com | Maria González | 25   |
| NULL                       | NULL  | francisco@example.com      | Test User      | 22   |

Para obtener los resultados en el mismo orden, simplemente podemos especificar el orden que queremos:

```sql
SELECT USUARIOS.*, NOTAS.*
FROM NOTAS
RIGHT JOIN USUARIOS ON NOTAS.EMAIL = USUARIOS.EMAIL
```

A partir de este ejercicio. queda a nuestra discrecion como resolver los problemas, ya sea utilizando LEFT JOIN o RIGHT JOIN pero para que las respuestas sean marcadas correctas los atributos deben aparecer en el mismo orden que las tablas son mencionadas, a menos que se especifique lo contrario.

Ejercicio:

Selecciona todos los registros de todos los productos (tabla productos) junto a sus precios (tabla precios), incluyendo a los productos que no tienen precio asignado. Las tablas se relacionan entre si por la columna producto_id.

```sql
SELECT PRODUCTOS.*, PRECIOS.*
FROM PRODUCTOS
LEFT  JOIN PRECIOS ON PRECIOS.PRODUCTO_ID = PRODUCTOS.PRODUCTO_ID
```

Resultado:

| PRODUCTO_ID | NOMBRE     | PRECIO_ID | PRODUCTO_ID | PRECIO |
|-------------|------------|-----------|-------------|--------|
| 1           | Producto A | 1         | 1           | 10.99  |
| 2           | Producto B | 2         | 2           | 15.99  |
| 3           | Producto C |           |             |        |

### Identificando tipos de Join
* Existen múltuplis tipos de join
* Hasta este momento solo hemos visto `INNER`, `LEFT`, `RIGHT` JOIN
* Debemos saber identificar el tipo de `JOIN` a utilizar en una consulta a partir de una peticion.

|  | **INNER JOIN**  | **LEFT JOIN (o LEFT OUTER JOIN)** | **RIGHT JOIN (o RIGHT OUTER JOIN)** |
|--|--|--| --|
| **¿Cuando usarlo?** | Cuando necesitas SOLO las filas donde haya coincidencias en ambas tablas  | Cuando necesitas TODAS las filas de la tabla izquierda y las filas coincidentes de la tabla derecha | Cuandp necesitas TODAS las filas de la tabla derecha y las filas coincidentes de la tabla izquierda |
| **Resultado** | Devuelve solo las filas con datos correspondientes en ambas tablas  | Devuelve todas las filas de la tabla de la izquierda y las coincidencias de la tabla de la derecha, con NULLs donde no haya coincidencias. |Devuelve todas las filas de la tabla de la derecha y las coincidencias de la tabla de la izquierda, con NULLs donde no haya coincidencias. |

**Ejercicio**

Se tienna base de datos con dos tas principales **autores** y **libros**

Crea una consulta con el fin de obtener informacion con el nombre del autor junto con el titulo del libro que ha escrito. **La consulta debe incluir sólo aquellos libros que tienen autores asignados**

Las columnas de la consulta deben llamarse:
*    `nombre_autor`
-   `titulo_libro`
Tabla **Autores**

| id |         nombre         |
|:--:|:----------------------:|
| 1  | Gabriel García Márquez |
| 2  | Isabel Allende         |
| 3  | J.K. Rowling           |

Tabla **libros**

| id |               titulo               | id_autor |
|:--:|:----------------------------------:|:--------:|
| 1  | Cien Años de Soledad               | 1        |
| 2  | La Casa de los Espíritus           | 2        |
| 3  | Harry Potter y la Piedra Filosofal | 3        |
| 4  | Libro sin Autor                    | NULL     |

```SQL
SELECT A.NOMBRE AS NOMBRE_AUTOR, L.TITULO AS TITULO_LIBRO
FROM AUTORES AS A
INNER  JOIN LIBROS AS L 
ON A.ID = L.ID_AUTOR
```

### Identificando tipos de Join parte 2

Ejercicio: 

Se tiene una base de datos con dos tablas principales: empleados y proyectos.

Crea una consulta con el fin de obtener información detallada, y que muestre el nombre del empleado junto con el nombre del proyecto en el que participa.

Tabla **empleados**

| id |     nombre     | id_proyecto |
|:--:|:--------------:|:-----------:|
| 1  | Juan Pérez     | 1           |
| 2  | María Gonzalez | 2           |
| 3  | Pedro López    | NULL        |
| 4  | Ana Rodríguez  | 3           |

Tabla **Proyectos**

| id |    nombre_proyecto    |
|:--:|:---------------------:|
| 1  | Desarrollo Web        |
| 2  | App Móvil             |
| 3  | Sistema de Inventario |

El resultado debe tener las columnas con los siguientes nombres e incluir a todos los empleados, aunque no tengan asignado proyecto.

-   nombre_empleado
-   nombre_proyecto
```SQL
SELECT E.NOMBRE AS NOMBRE_EMPLEADO, P.NOMBRE_PROYECTO
FROM EMPLEADOS AS E
LEFT  JOIN PROYECTOS AS P
ON E.ID_PROYECTO = P.ID
```
### Identificando tipos de Join parte 3

Ejercicio:

Se tiene una base de datos con dos tablas principales: empleados y proyectos.

Se pide obtener una lista de todos los proyectos junto con los nombres de los empleados asignados a cada proyecto, incluyendo aquellos proyectos que no tienen empleados asignados", se utilizan las siguientes columnas:

El resultado debe estar únicamente compuesto por las columnas nombre_empleado y nombre_proyecto que corresponden al nombre del empleado y al nombre del proyecto de sus respectivas tablas, incluso aquellos que no tienen empleados asignados (empleado NULL).

Tabla **empleados**
| id |     nombre     | id_proyecto |
|:--:|:--------------:|:-----------:|
| 1  | Juan Pérez     | 1           |
| 2  | María González | 2           |
| 3  | Pedro López    | NULL        |
| 4  | Ana Rodríguez  | 3           |

Tabla **Proyectos**

| id |    nombre_proyecto    |
|:--:|:---------------------:|
| 1  | Desarrollo Web        |
| 2  | App Móvil             |
| 3  | Sistema de Inventario |
| 4  | Marketing Digital     |

```SQL
SELECT E.NOMBRE AS NOMBRE_EMPLEADO, P.NOMBRE_PROYECTO
FROM EMPLEADOS AS E
RIGHT  JOIN PROYECTOS AS P
ON P.ID = E.ID_PROYECTO
```

## Tema 19: Cardinalidad

:arrow_up: [ir al inicio](.#tabla-de-contenidos)

### Relaciones 1 a 1
¿Que es la cardinalidad de una relación?
La cardinalidad de una relación es la cantidad de elementos de una tabla que pueden estar relacionadas con otra tabla.

Las relaciones de las tablas se pueden clasificar en tres tipos según su cardinalidad.

En este ejercicio veremos la relación 1 a 1, denotada como `1:1`. En esta relación, cada relación de una tabla estará relacionada con un único registro de otra tabla, por ejemplo, cada persona puede tener un único pasaporte y cada pasaporte tiene una única persona:

Tabla **personas** 

| id | nombre |
|:--:|:------:|
| 1  | Juan   |
| 2  | María  |
| 3  | Carlos |

Tabla **pasaportes**

| id | persona_id |
|:--:|:----------:|
| 1  | 1          |
| 2  | 2          |
| 3  | 3          |

Al hacer un `join` entre las tablas personas y pasaportes, obtendríamos:

| id | nombre | id | persona_id |
|:--:|:------:|:--:|:----------:|
| 1  | Juan   | 1  | 1          |
| 2  | María  | 2  | 2          |
| 3  | Carlos | 3  | 3          |

Es decir, por cada registro de la tabla personas hay un único registro en la tabla pasaportes.

**Ejercicio**

Dada las siguientes tablas:

Tabla **Vehículos**

| id |     modelo     |
|:--:|:--------------:|
| 1  | Toyota Corolla |
| 2  | Honda Civic    |
| 3  | Ford Focus     |

Tabla **matriculas**

| id | vehiculo_id | matricula |
|:--:|:-----------:|:---------:|
| 1  | 1           | ABC-123   |
| 2  | 2           | XYZ-456   |
| 3  | 3           | DEF-789   |

Se pide crear una consulta que muestre toda la información de las matriculas de los vehículos junto a sus matriculas correspondientes.

**Solución**

```sql
SELECT *
FROM vehiculos
JOIN matriculas
ON vehiculos.id = matriculas.id
```

### Relación 1 a n
En este tipo de relación, un registro de una tabla puede estar relacionado con uno o varios registros de otra tabla, Por ejemplo, podemos tener una tabla de empleados y otra de departamentos, cada empleado puede pértenecer a un único departamento, pero cada departamento puede tener varios empleados. 

Tabla **departamentos**
| id |      nombre      |
|:--:|:----------------:|
| 1  | Recursos Humanos |
| 2  | TI               |
| 3  | Marketing        |

Tabla **Empleados**

| id | nombre | departamento_id |
|:--:|:------:|:---------------:|
| 1  | Ana    | 1               |
| 2  | Pedro  | 2               |
| 3  | Luis   | 2               |
| 4  | Marta  | 3               |
| 5  | Elena  | 1               |

Al hacer un `join` entre las tablas `empleados` y `departamentos` obtendríamos

| id | nombre | id |      nombre      |
|:--:|:------:|:--:|:----------------:|
| 1  | Ana    | 1  | Recursos Humanos |
| 2  | Pedro  | 2  | TI               |
| 3  | Luis   | 2  | TI               |
| 4  | Marta  | 3  | Marketing        |
| 5  | Elena  | 1  | Recursos Humanos |

Podemos ver que, por cada registro de la tabla **empleados** hay un único registro en la tabla **departamentos** pero un registro de la tabla **departamentos** puede estar relacionado con varios registros de la tabla **empleados**

**Ejercicio**

Dada las siguientes tablas:

Tabla **continentes**

| continente_id |  nombre |
|:-------------:|:-------:|
| 1             | África  |
| 2             | América |
| 3             | Asia    |
| 4             | Europa  |
| 5             | Oceanía |


Tabla **países**

| pais_id |     nombre    | continente_id |
|:-------:|:-------------:|:-------------:|
| 1       | Nigeria       | 1             |
| 2       | Brasil        | 2             |
| 3       | China         | 3             |
| 4       | Alemania      | 4             |
| 5       | Australia     | 5             |
| 6       | Argentina     | 2             |
| 7       | Japón         | 3             |
| 8       | Francia       | 4             |
| 9       | Egipto        | 1             |
| 10      | Nueva Zelanda | 5             |

Se pide crear una consulta que muestre toda la información de los países junto a su continente correspondiente. Observa dentro de los resultados que un país puede pertenecer a un único continente pero un continente puede tener varios países.

```sql
SELECT *
FROM paises
JOIN continentes
ON continentes.continente_id = paises.continente_id```
```
### Relación n a n

En base de datos, solo podemos lograr relaciones de 1 a 1 o de 1 a muchos, si queremos una relación de muchos a muchos, necesitamos una tabla intermedia, con ciertas caracteristicas que veremos mas tarde.

**Ejemplo**

Se tiene un sistema que guarda información de profesores y alumnos. Cada profesor puede tener varios alumnos y cada alumno puede tener varios profesores, para lograr esto se tiene una tabla **profesores** una tabla **alumnos** y una tabla **profesores_alumnos** que relaciona a los profesores con los alumnos.

tabla **profesores**

| profesor_id | nombre |
|:-----------:|:------:|
| 1           | Ana    |
| 2           | Pedro  |
| 3           | Luis   |

tabla **alumnos**

| alumno_id | nombre |
|:---------:|:------:|
| 1         | Marta  |
| 2         | Elena  |
| 3         | Juan   |

tabla **profesores_alumnos**

| profesor_id | alumno_id |
|:-----------:|:---------:|
| 1           | 1         |
| 1           | 2         |
| 2           | 1         |

Al unir las tablas **profesores** y **profesores_alumnos** con un `join`, obtendriamos:

| profesor_id | nombre | alumno_id |
|:-----------:|:------:|:---------:|
| 1           | Ana    | 1         |
| 1           | Ana    | 2         |
| 2           | Pedro  | 1         |

Al unir la tabla anterior con la tabla **alumnos**, obtendriamos

| profesor_id | nombre | alumno_id | nombre |
|:-----------:|:------:|:---------:|:------:|
| 1           | Ana    | 1         | Marta  |
| 1           | Ana    | 2         | Elena  |
| 2           | Pedro  | 1         | Marta  |


Donde podemos ver que por cada registro de la tabla **profesores** hay uno o mas registros en la tabla **profesores_alumnos** y por cada registro de esta tabla hay un registro en la tabla **alumnos**.

Para hacer el join entre más de 2 tablas, se puede hacer un join por cada tabla que se quiera unir.

```sql
SELECT *
FROM profesores
JOIN profesores_alumnos
ON profesores.profesor_id = profesores_alumnos.profesor_id
JOIN alumnos
ON profesores_alumnos.alumno_id = alumnos.alumno_id;
```

**Ejercicio**

Se tiene una base de datos con un catalogo de objetos y colores. Cada objeto puede tener varios colores, y cada color puede estar asociado a varios objetos

tabla **objetos**

| objeto_id | objeto |
|:---------:|:------:|
| 1         | Mesa   |
| 2         | Silla  |
| 3         | Cama   |

tabla **colores**

| color_id | color |
|:--------:|:-----:|
| 1        | Rojo  |
| 2        | Azul  |
| 3        | Verde |

tabla **objeto_colores**

| objetos_colores_id | objeto_id | color_id |
|:------------------:|:---------:|:--------:|
| 1                  | 1         | 1        |
| 2                  | 1         | 2        |
| 3                  | 2         | 1        |
| 4                  | 3         | 3        |

Se pide hacer una consulta que muestre los objetos y su color correspondiente.

```sql
SELECT  *
FROM objetos
JOIN objetos_colores
ON objetos.objeto_id = objetos_colores.objeto_id
JOIN colores
ON objetos_colores.color_id = colores.color_id
```

| objeto_id | objeto | objetos_colores_id | objeto_id | color_id | color_id | color |
|:---------:|:------:|:------------------:|:---------:|:--------:|:--------:|:-----:|
| 1         | Mesa   | 1                  | 1         | 1        | 1        | Rojo  |
| 1         | Mesa   | 2                  | 1         | 2        | 2        | Azul  |
| 2         | Silla  | 3                  | 2         | 1        | 1        | Rojo  |
| 3         | Cama   | 4                  | 3         | 3        | 3        | Verde |

### Características de una tabla intermedia

Si tenemos dos tablas: **A** y **B** que queremos relacionar de manera `n a n` necesitamos una tabla intermedia **C** que relacione ambas tablas.

Intentemos hacerlo con un ejemplo:

Tenemos la tabla **profesores** y la tabla **alumnos**, cada profesor puede tener varios alumnos, y cada alumno puede tener varios profesores, si agregamos la clave foranea en la tabla profesores tendriamos algo asi:

Tabla **profesores** 
| profesor_id | nombre | alumno_id |
|:-----------:|:------:|:---------:|
| 1           | Ana    | 1         |
| 2           | Pedro  | 1         |
| 3           | Luis   | 2         |

Tabla **alumnos**

| alumno_id | nombre |
|:---------:|:------:|
| 1         | Marta  |
| 2         | Elena  |
| 3         | Juan   |

Al hacer un `JOIN` en las tablas **profesores** y **alumnos** obtendriamos:

| profesor_id | nombre | alumno_id | nombre |
|:-----------:|:------:|:---------:|:------:|
| 1           | Ana    | 1         | Marta  |
| 2           | Pedro  | 1         | Marta  |
| 3           | Luis   | 2         | Elena  |

O sea, que por cada profesor hay uno o varios alumnos, pero por cada alumno hay un solo profesor. Esto no es lo que queremos, ya que un alumno puede tener mas de un profesor.

Si lo hacemos al contrario y agregamos la clave foranea en la tabla **alumnos** tendriamos algo como esto:

tabla **profesores**

| profesor_id | nombre |
|:-----------:|:------:|
| 1           | Ana    | 
| 2           | Pedro  | 
| 3           | Luis   |

tabla **alumnos**

| alumno_id | nombre | profesor_id |
|:---------:|:------:|:-----------:|
| 1         | Marta  | 1           |
| 2         | Elena  | 1           |
| 3         | Juan   | 2           |

Al hacer un `JOIN`` entre la tabla **profesores ** y **alumnos**, obtendríamos:

| alumno_id | nombre | profesor_id | nombre |
|:---------:|:------:|:-----------:|:------:|
| 1         | Marta  | 1           | Ana    |
| 2         | Elena  | 1           | Ana    |
| 3         | Juan   | 2           | Pedro  |

O sea, que por cada alumno hay uno o varios profesores, pero por cada profesor hay un solo alumno, y esto tampoco es lo que queremos.

Para lograr esta relacion de muchos a muchos necesitamos una **tabla intermedia** que relacione las tablas **profesores** y **alumnos**. Esta tabla intermedia tiene que tener una columna que sea clave foranea de cada una de las tablas principales, para poder servir de puente entre ellas.

tabla **profesores_alumnos**

| profesor_id | alumno_id |
|:-----------:|:---------:|
| 1           | 1         |
| 1           | 2         |
| 2           | 1         |

Por cada entrada en la tabla **profesores_alumnos**  tenemos una relacion entre un profesor y un alumno, si queremos saber que profesores tienen un alumno o que alumno tiene un profesor podemos hacer un `JOIN` entre las tablas **profesores_alumnos** y **profesores** o **alumnos** 

**Ejercicio** 
Se tiene un sistema que guarda informacion de **profesores** y **alumnos** . Cada profesor puede tener varios alumnos y cada alumno puede tener varios profesores, para lograr esto se tiene una tabla **profesores**, una tabla *¨*alumnos** y una tabla **profesores_alumnos** que relaciona a profesores y alumnos.

tabla **profesores**
| profesor_id | nombre |
|:-----------:|:------:|
| 1           | Julia  |
| 2           | Pedro  |
| 3           | Luis   |

tabla **alumnos**

| alumno_id | nombre |
|:---------:|:------:|
| 1         | Marta  |
| 2         | Elena  |
| 3         | Juan   |

tabla **profesores_alumnos**

| profesor_id | alumno_id |
|:-----------:|:---------:|
| 1           | 1         |

Se pide agregar registros a la tabla **profesores_alumnos** para que **Julia** tenga a **Elena** como alumna, y **Pedro** tenga a **Juan** como alumno. Luego mostrar los profesores con sus respectivos alumnos.

Ingresa los datos en el orden pedido

```sql
-- Insertamos los valores
INSERT  INTO profesores_alumnos
VALUES  (1,2),  (2,3);
-- Realizamos la consulta
SELECT  *
FROM PROFESORES
JOIN profesores_alumnos
ON profesores_alumnos.PROFESOR_ID = PROFESORES.PROFESOR_ID
JOIN ALUMNOS
ON profesores_alumnos.ALUMNO_ID = ALUMNOS.ALUMNO_ID
```

Resultado:

| profesor_id | nombre | profesor_id | alumno_id | alumno_id | nombre |
|:-----------:|:------:|:-----------:|:---------:|:---------:|:------:|
| 1           | Julia  | 1           | 1         | 1         | Marta  |
| 1           | Julia  | 1           | 2         | 2         | Elena  |
| 2           | Pedro  | 2           | 3         | 3         | Juan   |

### Sin restricción de unicidad

Restriccion de unicidad

Supongamos que tenemos un sistema de gestion para una biblioteca, que incluye tres tablas principales: **libros**, **usuarios** y **pedidos** , esta ultima actua como la tabla intermedia para manejar la relacion muchos a muchos entre **libros** y **usuarios**. En este sistema, un libro puede ser solicitado por multiples usuarios y cada  usuario puede tener mas de un libro.


Antes de construir la tabla intermedia tenemos que hacernos una pregunta importante: **¿un usuario puede pedir un libro mas de una vez?**

* Si la respuesta es **SI**, entonces **NO** necesitamos una restricción de unicidad.
* Si la respuesta es **NO**, entonces debemos asegurarnos que no hayan registros duplicados en la tabla intermedia y esto se hace con una **restriccion de unicidad**

En este ejemplo, tiene sentido que un usuario pueda pedir un libro mas de una vez, por lo que nuestra tabla intermedia quedaria de la siguiente manera:

| libro_id | usuario_id |
|:--------:|:----------:|
| 1        | 1          |
| 1        | 1          |
| 2        | 2          |
| 2        | 2          |
| 3        | 1          |

Dentro de la tabla podemos ver que el **usuario 1** ha pedido el **libro 1** mas de una vez, lo cual no implica un problema si no hay una restriccion de unicidad.

Ejercicio:

tabla **libros**
| libro_id |   titulo   |
|:--------:|:----------:|
| 1        | El Quijote |
| 2        | Don Juan   |
| 3        | Rayuela    |

tabla **usuarios**

| usuario_id | nombre |
|:----------:|:------:|
| 1          | Ana    |
| 2          | Pedro  |
| 3          | Luis   |

tabla **pedidos**

| libro_id | usuario_id |
|:--------:|:----------:|
| 1        | 1          |
| 1        | 1          |
| 2        | 2          |
| 2        | 2          |
| 3        | 1          |

Selecciona a todos los usuarios que han pedido el mismo libro más de una vez. Las columnas a mostrar son `usuario_id`, `libro_id` y `veces` donde `veces`es el número de veces que el usuario ha pedido el libro.

> Pista: Agrupa por libro_id y usuario_id y cuenta cuantos registros hay por cada grupo. Reflexiona si debes ocupar `where` o `having` para filtrar los resultados.

```sql
SELECT usuario_id, libro_id,  count(libro_id)  AS veces
FROM pedidos
GROUP  BY libro_id, usuario_id
HAVING  count(libro_id)  >  1
```

### Con restricción de unicidad

Supongamos que tenemos un sistema que guarda informacion de **proyectos** y **empleados**, cada empleado puede trabajar en varios proyectos, y cada proyecto puede tener varios empleados trabajando en el. Para manejar esto, tenemos una tabla **empleados**, una tabla **proyectos** y una tabla **empleados_proyectos** que relaciona los empleados con los proyectos.

En este caso, un empleado no puede estar asignado a un mismo proyecto mas de una vez,. Para evitar que esto suceda, al crear la tabla intermedia, agregaremos una clave primaria compuesta por las claves foraneas de las tablas principales.

```sql
CREATE TABLE Empleados_Proyectos (
empleado_id INT,
proyecto_id INT,
PRIMARY KEY (empleado_id, proyecto_id),
FOREIGN KEY (empleado_id) REFERENCES Empleados(id),
FOREIGN KEY (proyecto_id) REFERENCES Proyectos(id)
);
```

De esta manera, si se intenta crear un registro con un empleado y un proyecto que ya existen en la tabla, se generará un error, lo que asegura que no haya registros duplicados en la tabla intermedia.

**Ejercicio**:

Dadas las tablas:

Tabla **empleados**
| id |    nombre    |     puesto    |
|:--:|:------------:|:-------------:|
| 1  | Juan Pérez   | Desarrollador |
| 2  | María García | Analista      |
| 3  | Carlos López | Gerente       |

Tabla **proyectos**

| id |       nombre       | departamento |
|:--:|:------------------:|:------------:|
| 1  | Sistema de Gestión | TI           |
| 2  | Desarrollo Web     | TI           |
| 3  | Análisis de Datos  | Data Science |

Tabla **empleados_proyectos**

| empleado_id | proyecto_id |
|:-----------:|:-----------:|
| 1           | 1           |
| 1           | 2           |
| 2           | 1           |
| 2           | 3           |
| 3           | 1           |
| 3           | 2           |
| 3           | 3           |


Crea una consulta que seleccione todos los empleados junto con la cantidad de proyectos asignados a cada uno, demostrando que no hay registros duplicados en la tabla intermedia. Las columnas de la consulta deben ser `nombre`, `puesto` y `cantidad_proyectos`.

```SQL
SELECT E.NOMBRE, E.PUESTO,  COUNT(E.NOMBRE)  AS CANTIDAD_PROYECTOS
FROM EMPLEADOS AS E
JOIN EMPLEADOS_PROYECTOS
ON E.ID = EMPLEADOS_PROYECTOS.EMPLEADO_ID
JOIN PROYECTOS
ON EMPLEADOS_PROYECTOS.PROYECTO_ID = PROYECTOS.ID
GROUP  BY e.NOMBRE
```
## Operadores:

:arrow_up: [ir al inicio](.#tabla-de-contenidos)

### Operadores aritmeticos:
* `+`: Adicion
* `-`: Subtraccion
* `*`: Multiplicacion
* `/`: Division
* `%`: Módulo 

Ejemplo:
```sql
SELECT product, price, (price *0.18) as tax
FROM products;
```

### Operadores de comparacion
* `=`: igual que
* `!=` o `<>`: no igual que
* `>`: mayor que
* `<`: menos que
* `>=`: mayor o igual que
* `<=`: menor o igual que

Ejemplo:
```sql
SELECT name, age
FROM students
WHERE age > 18;
```

### Operadores lógicos
* `AND`: retorna verdadero si ambas condiciones son verdaderas
* `OR`: retorna verdadero si alguna de las soa condiciones es veradera
* `NOT`: retorna el booleano opuesto de una condicion

Ejemplo:

```sql
SELECT *
FROM employees
WHERE salary > 50000 AND age < 30
```

### Operadores bit a bit
* `&`: AND
* `|`: OR
* `^`: XOR

Los operadores bit a bit son mucho menos usados en SQL que los demas operadores



