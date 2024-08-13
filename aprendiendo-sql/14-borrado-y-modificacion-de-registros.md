## Tema 14: Borrado y modificación de registros
:arrow_up: [ir al inicio](./README.md#tabla-de-contenidos)

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
