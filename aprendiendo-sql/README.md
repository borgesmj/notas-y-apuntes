# Aprendiendo SQL
Notas tomadas del [**curso interactivo de Desafio LATAM**](https://sqlinteractivo.desafiolatam.com/cursos/1) e informacion tomada de [roadmap.sh](https://roadmap.sh/sql)

Este contenido estará estructurado acorde al contenido de Desafio LATAM y se refuerza con la informacion del roadmap.sh

## Tabla de contenidos

| DIA                           | Enlace                                  |
|-------------------------------|-----------------------------------------|
| Dia 1: Conceptos básicos      | [ir](.#dia-1-introduccion)           |
| Dia 2: Selecionando filas     | [ir](.#dia-2-seleccionando-filas)    |
| Dia 3: Ordenando Resultados   | [ir](.#dia-3-ordenando-resultados)   |
| Dia 4: Limit                  | [ir](.#dia-4-limit)                  |
| Dia 5: Operaciones con string | [ir](.#dia-5-operaciones-con-string) |
| Dia 6: Operaciones con fechas | [ir](.#dia-6-operaciones-con-fechas) |
| Dia 7: Funciones de agregacion | [ir](.#dia-7-funciones-de-agregacion) |
| Dia 8: Distinct | [ir](.#dia-8-distinct) |
| Dia 9: Introducción a grupos | [ir](.#dia-9-introducción-a-grupos) |
| Dia 10: HAVING | [ir](.#dia-10-having) |
| Dia 11: Subconsultas | [ir](.#dia-11-subconsultas) |
| Dia 12: Combinacion de consultas | [ir](.#dia-12-combinacion-de-consultas) |
| Dia 13: Insercion de registros | [ir](.#dia-13-insercion-de-registros) |
| Dia 14: Borrado y modificación de registros | [ir](.#dia-14-Borrado-y-modificación-de-registros) |


## Dia 1: Introduccion
[ir al inicio](.#tabla-de-contenidos)
### ¿Que significa SQL?
SQL viene de Structured Query Language (Lenguaje Estructurado de Consultas); es un lenguaje de programación que se utiliza para comunicarse y administrar bases de datos. SQL es un estándar para manipular datos almacenados en sistemas de gestión de bases de datos relacionales (relational database management systems - RDBMS), así como para el procesamiento de flujos en sistemas de gestión de flujos de datos relacionales (in a relational data stream management system - RDSMS). Fue desarrollado por primera vez en la década de 1970 por IBM.

> Una base de datos relacional representa una coleccion de tablas relacionadas

SQL consiste en varios componentes, cada uno con su unico proposito en comunicacion de bases de datos:

* Consultas: Es el componente que permite recuperar datos de una base de datos. La sentencia SELECT es la más utilizada para este fin.
* Lenguaje de definición de datos ( Data Definition Language - DDL): Permite crear, modificar o eliminar bases de datos y sus objetos relacionados, como tablas, vistas, etc. Los comandos incluyen:
  - CREATE TABLE
  - CREATE INDEX
  - CREATE VIEW
  - ALTER
  - DROP
  - TRUNCATE
* Lenguaje de manipulación de datos ( Data manipulation Language - DML): Permite gestionar datos dentro de objetos de bases de datos. Estos comandos incluyen:
  - SELECT
  - INSERT
  - UPDATE
  - DELETE.
* Lenguaje de control de datos ( Data control Langiage - DCL): Incluye comandos como GRANT y REVOKE, que tratan principalmente de derechos, permisos y otras tareas de gestión a ni vel de control para el sistema de base de datos.

**Tipos de  datos**
* Numéricos:
  - Integer: valor entero
  - Numeric (n,m): numero de hata 18 digitos (con decimales) donde **n** representa el total de digitos admitidos y **m** el numero de posiciones decimales.
  - Decimal (n.m): igual que numeric.
  - Float: npumero de coma flotante
* Alfanumáricos:
  - Char(n): almacena de 1 a 255 caracteres fijo.
  - varchar(n): datos de cadena de tamañp variable
* Fecha:
  - Date: almacena fechas con dia, mes y año
  - datetime: almacena fechas con fecha y hora
* Logicos:
  - BIT: tipo bit. Se aplica logica booleana
  - Boolean: cero => false. Distinto de cero => true.

SQL viene en muchas formas, como bases de datos Oracle, Microsoft SQL Server y MySQL. A pesar de sus muchas diferencias, todas las bases de datos SQL manejan los mismos comandos.

Una de las acciones que mas se requieren en SQL es consular los datos de una tabla. Esto lo podemos hacer con la instruccion `Select`

### `Select`
La declaracion `SLECT` en SQL es mayormente usada para obtener datos de la base de datos, es la mas esencial en SQL

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


### Seleccionando todas las columnas de una tabla
Si queremos seleccionar todas las columnas de una tabla, podemos usar el `*` asi:

```sql
SELECT * FROM table_name
```
### Seleccionando una columna de la tabla
En este ejercicio se tiene una tabla llamado usuarios que tiene las columnas nombre, apellido, email y telefono.

Selecciona sólo los nombres de la tabla usuarios.

```sql
SELECT nombre
from usuarios
```

### Seleccionando múltiples columnas de una tabla
Supongamos que tenemos una tabla llamada productos con las columnas 'nombre', 'precio', 'cantidad' y 'proveedor'. Selecciona sólo el nombre, precio y el proveedor

```sql
SELECT nombre, precio, proveedor FROM productos
```

### Asignando un alias a una columna con "AS"
Se tiene una tabla llamada usuarios con las columnas nombre, apellido, email y teléfono. Selecciona todos los nombres bajo el alias "cliente"

```sql
SELECT nombre as cliente from usuarios
```

### Asignando un alias a varias columnas con "AS"
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

### Asignando un alias con AS y comillas dobles

Selecciona el nombre y el email de los usuarios de la tabla usuarios, y asigna el nombre 'Correo electrónico' a la columna 'email'.

```sql
select nombre, email as "Correo electrónico" from usuarios
```
## Dia 2: Seleccionando filas

[ir al inicio](.#tabla-de-contenidos)

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
| 3    |             | carlos.diaz@mail.com  |
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
## Dia 3: Ordenando resultados
[ir al inicio](.#tabla-de-contenidos)
### Ordenando filas
En este ejercicio aprenderemos a ordenar las filas de una tabla SQL y para estoi estudiaremos una nueva clausula llamada *ORDER BY*
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

## Dia 4: Limit
[ir al inicio](.#tabla-de-contenidos)
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
## Dia 5: Operaciones con string

[ir al inicio](.#tabla-de-contenidos)

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


## Dia 6: Operaciones con fechas

[ir al inicio](.#tabla-de-contenidos)

En SQL, DATE  es un tipo de dato que almacena la fecha. NO ALMACENA EL INFORMACION DEL TIEMPO. EL formato de la fecha es: 'YYYY-MM-DD', por ejemplo: '2022-01-01'
SQL provee de varias funciones para manipular fechas.
SQL provee de muchas funciones para manejar la fecha:

### Obteniendo la fecha de hoy 
con la funcion `DATE()` podemos obtener la fecha de hoy, por ejemplo podemos utilizar la clausula `WHERE`  para obtener los registros del dia de hoy.

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

En este ejemplo estamos sumando 1 dia a la fecha actual (now). Si queremos sumar mas dias, por ejemplo 5 dias utilizaremos `Date('now', '5 day')`. Tambien es posible sumar semamas, meses, con:

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
## Dia 7: Funciones de agregacion
[ir al inicio](.#tabla-de-contenidos)

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
Hasta el momento hemos estudiado dos funciones de agregacion:
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

Las funciones de agregación se pueden combinar con las claúsulas previamente estudiadas. Simplemente tenemos que respetar el orden establecido de las claúsulas.

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
## Dia 8: Distinct

[ir al inicio](.#tabla-de-contenidos)

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
| antonio.diaz@empresa.com     |
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
| antonio.diaz@empresa.com     |
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
## Dia 9: Introducción a grupos
[ir al inicio](.#tabla-de-contenidos)
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
| antonio.diaz@empresa.com     |
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
| antonio.diaz@empresa.com     |
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
### Agruopar y promediar

Previamente aprendimos que AVG nos permite calcular el promedio de los elementos de una columna en una tabla. En este ejercicio lo utilizaremos para calcular promedios po grupo.

```
SELECT grupo, AVG(columna)
FROM tabla
GROUP BY grupo
```

Ejercicio

Dada la siguiente tabla de estudiantes


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

Encuentra el promedio de notas de cada estudiante. Las columnas deben tener el nombre completo y promedio_notas respectivamente

Este ejercicio tiene un supuesto importante, que no hay dos estudiantes con el mismo nombre y apellido. DIscutiremos este tipo de supuestos mas adelante cuando revisemos el concepto de integridad.

```
SELECT nombre_completo, AVG(nota) as promedio_notas
FROM estudiantes
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
Tenemos la siguiente tabla estudiantes

| CORREO                  | MATERIA     | NOTA |
|-------------------------|-------------|------|
| estudiante1@ejemplo.com | Matemáticas | 8.5  |
| estudiante2@ejemplo.com | Matemáticas | 9.0  |
| estudiante3@ejemplo.com | Matemáticas | 7.5  |
| estudiante1@ejemplo.com | Ciencias    | 8.0  |
| estudiante2@ejemplo.com | Ciencias    | 9.5  |
| estudiante3@ejemplo.com | Ciencias    | 7.0  |
| estudiante1@ejemplo.com | Historia    | 8.7  |
| estudiante2@ejemplo.com | Historia    | 9.2  |
| estudiante3@ejemplo.com | Historia    | 7.8  |

Calcula el promedio de cada estudiante en cada materia. LAs columnas deben llamarse correo, materi y promedio_notas

```
SELECT correo, materia, AVG(nota) as promedio_notas
FROM estudiantes
group by 1,2
```
## Dia 10: HAVING

[ir al inicio](.#tabla-de-contenidos)

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
| antonio.diaz@empresa.com     |
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

Crea una consulta para determinar cuales son los estudiantes que aprobaron. El criterio de aprobacion es promedio_de_notas >= 50

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

## Dia 11: Subconsultas

[ir al inicio](.#tabla-de-contenidos)

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

Se tiene la siguiente tabla de estudiantes

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
2. Seleccionamos los nombres de la tabla _estudiantes_ cuyo id este dentro de la subconsulta anterior


```
SELECT nombre from estudiantes
WHERE estudiante_id IN (SELECT estudiante_id from notas where promedio_notas <= 50)
```

Ejercicio
Se tiene una tabla estudiantes con un código y un nombre

| ESTUDIANTE_ID | NOMBRE |
|---------------|--------|
| 1             | Juan   |
| 2             | María  |
| 3             | Pedro  |
| 4             | Ana    |

Y se tiene una tabla _promedios_ con el codigo dek estudiante y su promedio de notas

| ESTUDIANTE_ID | PROMEDIO_NOTAS |
|---------------|----------------|
| 1             | 85             |
| 2             | 65             |
| 3             | 49             |
| 4             | 38             |

Muestra los nombres de todos los estudiantes que tengan un promedio denotas sobre 50.

Tip:
1. No necesitas agrupar ni promediar ni contar.
2. Hay mas de una forma de resolver este ejercicio, no te adelantes a joins e intenta resolverlo utilizando subqueries.


```
SELECT nombre
FROM estudiantes
WHERE estudiante_id IN (SELECT estudiante_id from promedios where promedio_notas > 50)
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

## Dia 12: Combinacion de consultas

[ir al inicio](.#tabla-de-contenidos)

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

Supongamos que tenemos dos tablas "Estudiantes" y "Profesores", que contienen una lista de apellidos e cada una. Queremos crear una lista que combine los apellidos de ambas tablas.

Estudiantes


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
FROM Estudiantes
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
Dada las tablas **estudiantes**

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
FROM estudiantes
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

## Dia 13: Insercion de registros

[ir al inicio](.#tabla-de-contenidos)

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
El formato de fecha es `YYYY-MM-DD`o sea, año.mes-dia, donde el año es de 4 digitos, el mes de dos digitos, y el dia de dos digitos.

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

En una base de datos de SQL, es posible agilizar el proceso de insercion de datos en una tabla mediante el uso de un campo autoincremental.Este tipo de campo es especialmente util cuando se trata de gestionar indentificadores unicos, como por ejemplo, el campo de 'id' de una tabla. La caracteristica de autoincremento se logra empleando la clausula AUTOINCREMENT en la definicion del campo.
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


## Dia 14: Borrado y modificación de registros
[ir al inicio](.#tabla-de-contenidos)

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

> Nota: La eliminación realizada mediante la sentencia "DELETE" es permanente y no puede deshacerse. Asegúrese siempre de tener una copia de seguridad antes de ejecutar una consulta DELETE, especialmente cuando se trata de una base de datos de producción.

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
