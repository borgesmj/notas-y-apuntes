## Tema 2: Seleccionando filas

:arrow_up: [ir al inicio](./README.md)


| Sección | Título |
|---------|--------|
| 2.1 | [Cláusula WHERE](.#where) |
| 2.2 | [Operador mayor o igual que](.#utilizando-el-operador-mayor-o-igual-que) |
| 2.3 | [Operador menor que](.#utilizando-el-operador-menor-que) |
| 2.4 | [Operador menor o igual que](.#utilizando-el-operador-menor-o-igual-que-en-una-condicion) |
| 2.5 | [Condición de igualdad](.#seleccionando-filas-bajo-una-condicion-de-igualdad) |
| 2.6 | [Condición de igualdad con strings](.#seleccionando-filas-bajo-una-condicion-de-igualdad-tipo-de-dato-string) |
| 2.7 | [Condición de igualdad con booleanos](.#seleccionando-filas-bajo-una-condicion-de-igualdad-tipo-de-dato-booleano-true) |
| 2.8 | [Condición de igualdad con booleanos (falso)](.#seleccionando-filas-bajo-una-condicion-de-igualdad-tipo-de-dato-booleano-false) |
| 2.9 | [Operador AND](.#utilizando-dos-condiciones-con-operador-and) |
| 2.10 | [Operador OR](.#utilizando-operador-or) |
| 2.11 | [Seleccionando fechas](.#seleccionando-una-fecha) |
| 2.12 | [Operador BETWEEN](.#seleccionando-datos-entre-dos-valores-con-between) |
| 2.13 | [Operador LIKE](.#seleccionando-filas-con-like) |
| 2.14 | [Comodín al principio](.#seleccionando-con-comodin-al-principio) |
| 2.15 | [Valores no nulos](.#seleccionando-registros-sin-valores-nulos) |
| 2.16 | [Valores nulos](.#seleccionando-registros-con-valores-nulos) |


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

#### Ejercicio
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

#### Ejercicio
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
#### Ejercicio
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

#### Ejercicio
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