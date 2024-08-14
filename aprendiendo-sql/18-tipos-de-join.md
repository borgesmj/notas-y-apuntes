## Tema 18: Tipos de join

:arrow_up: [ir al inicio](./README.md#tabla-de-contenidos)

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

### Full Outer Join
Existen distintos tipos de JOIN:
* Al utilizar `INNER JOIN` si en una des tablas no está la clave correspondiente, el registro no aparecerá en los resultados.
* Con `LEFT JOIN`, si en la tabla de la izquierda está la clave pero en la tabla de la derecha no, el registro de la tabla izquierda aparecerá en el resultado final con valores `NULL` en los registros de la tabla derecha.
* Con `RIGHT JOIN` si en la tabla de la derecha está la clave pero en la tabla de la izquierda no, el registro de la tabla derecha aparecerá en el resultado final con valores `NULL` en los registros de la tabla izquierda.
* Al utilizar `FULL OUTER JOIN` se obtienen todos los registros de ambas tablas, incluyendo los registros no coincidentes.

Un `FULL OUTER JOIN`  en SQL es un método para combinar filas de dos o mas tablas, basado en una columna relacionada entre ellos. Regresa todas las filas de la tabla de la izquierda (tabla 1) y de la tabla de la derecha (tabla 2).

La palabra clave `FULL OUTER JOIN` combina el resultados de ambas uniones, izquierda y derecha, y retorna todas (coincidentes y no coincidentes) las filas de las tablas en ambos lados de de la clausula join.

**Sintaxis**:

```SQL
SELECT column_name(s)
FROM table1
FULL OUTER JOIN table2
ON table1.column_name = table2.column_name;
```

Diagrama de Veen

![diagrama de venn en FULL OUTER JOIN](https://www.tutorialrepublic.com/lib/images/full-join.png)

Ejemplo:
Se tiene dos tablas

Tabla **empleados**
| id_empleado | nombre | id_departamento |
|:-----------:|:------:|:---------------:|
| 1           | Ana    | 10              |
| 2           | Juan   | 20              |
| 3           | María  | 30              |

Tabla **Departamento**

| id_departamento |   departamento   |
|:---------------:|:----------------:|
| 10              | Recursos Humanos |
| 20              | Finanzas         |
| 40              | Marketing        |

Una consulta con `FULL OUTER JOIN` entre las tablas empleados y departamentos, utilizando el campo `id_departamento`, daría como resultado:

| id_empleado | nombre | id_departamento |   departamento   |
|:-----------:|:------:|:---------------:|:----------------:|
| 1           | Ana    | 10              | Recursos Humanos |
| 2           | Juan   | 20              | Finanzas         |
| 3           | María  | 30              | NULL             |
| NULL        | NULL   | 40              | Marketing        |

Estos datoss ayudan a identificar que empleados no está relacionado con un departamento o que departamento no tiene empleados.

#### `FULL OUTER JOIN` en SQLite
El motor de búsqueda SQLite no soporta no soporta operaciones de `FULL OUTER JOIN` , sim embargo, se ede lograr el mismo efecto usando esta sintaxis.

```sql
SELECT *
FROM tableA
LEFT JOIN tableB
  ON tableA.column_name = tableB.column_name
UNION
SELECT *
FROM tableA
RIGHT JOIN tableB
  ON tableA.column_name = tableB.column_name
```

#### Ejercicio

Dada las tablas `empleados` y `departamentos` que vimos previamente, escribe una consulta que devuelva todos los registros coincidentes y no coincidentes entre las tablas empleados y departamentos.

```SQL
SELECT E.*, D.*
FROM EMPLEADOS E
FULL  OUTER  JOIN DEPARTAMENTOS D
ON E.ID_DEPARTAMENTO = D.ID_DEPARTAMENTO
```

### Full Outer Join parte 2
unperacion de `Full Outer Join` la union`RIGHT JOIN` y `LEFT JOIN` , devuelve todos los registros de ambas tablas incluyendo los registros no coincidentes.

#### UNION vs UNION ALL
Si miramos detenidamente, que si simplemente unimos los resultados de `LEFT JOIN` y `RIGHT JOIN` podríamos estar duplicando registros en el punto de intersección. Aqui es donde des recordar la direfencia entre [`UNION`.  y `UNION ALL` ](#union-vs-union-all). `UNION` elimina los registros dupliados mientras que `UNION ALL` no lo hace,r lo tanto si unimos los resultados de un `LEFT JOIN` y `RIGHT JOIN` debemos utilizar `UNION` para evitar duplicados.

```sql
SELECT *
FROM tableA
LEFT JOIN tableB
  ON tableA.column_name = tableB.column_name
UNION
SELECT *
FROM tableA
RIGHT JOIN tableB
  ON tableA.column_name = tableB.column_name
```

#### Ejercicio:

Se tienen las tablas **Clientes** y **Pedidos** 
Tabla **CLientes**

| id_cliente | nombre_cliente |
|:----------:|:--------------:|
| 1          | Cliente A      |
| 2          | Cliente B      |
| 3          | Cliente C      |
| 4          | Cliente D      |

Tabla **Pedidos**

| id_pedido | id_cliente | fecha_pedido |
|:---------:|:----------:|:------------:|
| 101       | 1          | 2023-01-10   |
| 102       | 3          | 2023-02-15   |
| 103       | 5          | 2023-03-20   |

Crea una consulta que devuelva todos los registros coincidentes y no coincidentes entre las tablas `clientes` y `pedidos`.

```sql
select c.*, p.*
from clientes c
left join pedidos p
on c.id_cliente = p.id_cliente
union
select c.*, p.*
from clientes c
right join pedidos p
on c.id_cliente = p.id_cliente
```

### Left excluding join

Al utilizar `LEFT JOIN` , si la clave está presente en la tabla de la izquierda, pero ausente en la tabla de la derecha, el registro de la tabla izquierda se mostrara al final con valores NULL, en los campos de la tabla derecha.

Un `left excluding join` es unambinacion del `LEFT JOIN` con la clausula `WHERE`, para mostrar los registros de la tabla izquierda que **no** tienen coincidencias en la tabla derecha.

#### Tabla Alumnos

| id | nombre | apellido |
|:--:|:------:|:--------:|
| 1  | Juan   | Perez    |
| 2  | Maria  | Garcia   |
| 3  | Pedro  | Lopez    |

#### Tabla Calificaciones

| id | alumno_id | calificacion |
|:--:|:---------:|:------------:|
| 1  | 1         | 8.5          |
| 2  | 1         | 7.9          |
| 3  | 2         | 9.2          |
| 4  | 2         | 8.8          |

En este ejemplo, si queremos obtener los alumnos que no tienen calificaciones, podemos hacerlo con un left excuding join

```sql
SELECT *
FROM alumnos a
LEFT JOIN calificaciones c
ON a.id = c.alumno_id
WHERE c.calificacion IS NULL;
```

y como resultado obtendriamos:

| id | nombre | apellido | id | alumno_id | calificacion |
|:--:|:------:|:--------:|:--:|:---------:|:------------:|
| 3  | Pedro  | Lopez    |    |           |              |

Dado que Pedro es el único alumno que **no tiene calificaciones** es el único que aparece en el resultado final.

#### Ejercicio 
Dada las siguientes tablas:

tabla **profesion** 

| id |   Nombre  |
|:--:|:---------:|
| 1  | Ingeniero |
| 2  | Doctor    |
| 3  | Abogado   |

Tabla **Personas**

| id | Nombre | Apellido | Profesion_id |
|:--:|:------:|:--------:|:------------:|
| 1  | Juan   | Perez    | 1            |
| 2  | Maria  | Garcia   | 2            |
| 3  | Pedro  | Lopez    | 2            |

Crea una consulta SQL que muestre todos los datos de las tablas mencionadas de las personas que no tienen profesión.

```sql
SELECT  *
FROM PERSONAS P
LEFT  JOIN PROFESION PR
ON P.Profesion_id = PR.ID
WHERE P.NOMBRE IS  NULL
```

### Right Excluding JOIN
Un right excluding join es una combinación de right join con una cláusula `WHERE` para mostrar los registros de la tabla derecha que no tienen coincidencias en la tabla izquierda.
`Right Excluding JOIN` es similar a `LEFT EXCLUDING JOIN`. Una consulta de right excluding join nos regresa los registros que **no tienen coincidencias** en la **tabla izquierda**
```SQL
SELECT *
FROM tableA
RIGHT JOIN tableB
  ON tableA.name = tableB.name
WHERE tableA.name IS NULL
```

Es importante observar que además de cambiar el JOIN hay que cambiar el `WHERE` y sustituir **tableA** por **tableB**

En una base de datos se tienen las tablas de calificaciones y cursos

tabla **calificaciones**
| id | alumno_id | curso_id | calificacion |
|:--:|:---------:|:--------:|:------------:|
| 1  | 1         | 1        | 8.5          |
| 2  | 1         | 2        | 7.9          |
| 3  | 2         | 1        | 9.2          |
| 4  | 2         | 2        | 8.8          |
| 5  | 3         | 1        | 7.5          |
| 6  | 4         | 2        | 9.1          |

tabla **cursos**
| id |    nombre   | docente_id |
|:--:|:-----------:|:----------:|
| 1  | Matemáticas | 1          |
| 2  | Ciencias    | 1          |
| 3  | Arte        | 1          |

Nos piden obtener toda la información de los cursos que no tienen calificaciones. Para resolver esto con un right excluding join, la consulta sería:

```sql
SELECT *
FROM calificaciones c
RIGHT JOIN cursos cu
ON cu.id = c.curso_id
WHERE c.id IS NULL;
```

Esto nos da como resultado:

| id | alumno_id | curso_id | calificacion | id | nombre | docente_id |
|:--:|:---------:|:--------:|:------------:|:--:|:------:|:----------:|
|    |           |          |              | 3  | Arte   | 1          |

#### Ejercicio:

Dadas las siguientes tablas:

tabla **docentes**
| id |  nombre  |
|:--:|:--------:|
| 1  | Benjamin |
| 2  | Felipe   |
| 3  | Susana   |

tabla **cursos**

| id |    nombre   | docente_id |
|:--:|:-----------:|:----------:|
| 1  | Matemáticas | 1          |
| 2  | Ciencias    | 1          |
| 3  | Arte        | 1          |

Utiliza un right join para obtener a los docentes que aún no tienen un curso asignado.

```sql
SELECT  *
FROM CURSOS C
RIGHT  JOIN DOCENTES D
ON D.ID = C.DOCENTE_ID
WHERE C.ID IS  NULL
```
### Full outer excluding join
Un Full outer excluding joing es la unión entre un `full outer join` con `where`.
`FULL OUTER EXCLUDING JOIN` nos entrega los registros coincidentes, pero también los no coincidentes de la tabla de la derecha como de la izquierda.

Aunque SQLite no soporta directamente `FULL OUTER JOIN`, podemos realizar un `FULL OUTER EXCLUDING JOIN` utilizando una combinación de `LEFT EXCLUDING JOIN` y `RIGHT EXCLUDING JOIN`.

```sql
SELECT *
FROM tabla_A
LEFT JOIN tabla_B ON tabla_A.clave = tabla_B.clave
WHERE tabla_B.clave IS NULL
UNION
SELECT *
FROM tabla_A
RIGHT JOIN tabla_B ON tabla_A.clave = tabla_B.clave
WHERE tabla_A.clave IS NULL
```

Esta consulta nos dará todos los registros de tabla_A que no tienen coincidencia en tabla_B, y todos los registros de tabla_B que no tienen coincidencia en tabla_A.

#### Ejercicio
Consideremos las siguientes tablas:

Tabla **empleados**

| id_empleado | nombre | id_departamento |
|:-----------:|:------:|:---------------:|
| 1           | Ana    | 10              |
| 2           | Juan   | 20              |
| 3           | María  | 30              |
| 4           | Carlos | NULL            |

Tabla **depertamentos**
| id_departamento |   departamento   |
|:---------------:|:----------------:|
| 10              | Recursos Humanos |
| 20              | Finanzas         |
| 40              | Marketing        |

Escribe una consulta SQL que implemente un FULL OUTER EXCLUDING JOIN entre las tablas `empleados` y `departamentos`. Esta consulta debe mostrar tanto a los Empleados que no están asignados a ningún departamento existente como a los departamentos que no tienen empleados asignados.

Una vez que hayas escrito la consulta, ejecútala y analiza los resultados y contesta las siguientes preguntas:

1.  ¿Por qué Carlos aparece en el resultado de la consulta?
2.  ¿Por qué el departamento de Marketing aparece en el resultado?
3.  ¿Cómo se diferencia este resultado de un FULL OUTER JOIN regular?

```sql
SELECT E.ID_EMPLEADO, E.NOMBRE, D.ID_DEPARTAMENTO, D.DEPARTAMENTO
FROM EMPLEADOS E
FULL  OUTER  JOIN DEPARTAMENTOS D
ON D.ID_DEPARTAMENTO = E.ID_DEPARTAMENTO
WHERE E.ID_EMPLEADO IS  NULL
UNION
SELECT E.ID_EMPLEADO, E.NOMBRE, E.ID_DEPARTAMENTO, D.DEPARTAMENTO
FROM EMPLEADOS E
FULL  OUTER  JOIN DEPARTAMENTOS D
ON D.ID_DEPARTAMENTO = E.ID_DEPARTAMENTO
WHERE D.DEPARTAMENTO IS  NULL
```

Resultado:

| id_empleado | nombre | id_departamento | departamento |
|:-----------:|:------:|:---------------:|:------------:|
|             |        | 40              | Marketing    |
| 3           | María  | 30              |              |
| 4           | Carlos |                 |              |

### Natural Join
El **NATURAL JOIN** es un tipo de join en SQL que se utiliza para combinar dos tablas utilizando las columnas que tienen el mismo nombre. Su sintaxis es la siguiente:

```sql
SELECT columnas
FROM tabla1
NATURAL JOIN tabla2;
```

-   Natural Join es un JOIN que adicionalmente asume que las columnas con el mismo nombre son las columnas de unión.
-   La ventaja de usar `NATURAL JOIN` es que simplifica la escritura de la consulta, pero solo es útil cuando las columnas de unión tienen el mismo nombre y tipo de datos en ambas tablas.

Veamos un ejemplo:
Supongamos que tenemos estas tablas:
Tabla **Clientes**
| id_cliente | nombre |       email       |
|:----------:|:------:|:-----------------:|
| 1          | Juan   | juan@example.com  |
| 2          | María  | maria@example.com |
| 3          | Pedro  | pedro@example.com |

Tabla **pedidos**
| id_pedido | id_cliente |  producto  | cantidad |
|:---------:|:----------:|:----------:|:--------:|
| 1         | 1          | Laptop     | 1        |
| 2         | 2          | Tablet     | 2        |
| 3         | 1          | Smartphone | 1        |

En este caso, ambas tablas tienen una columna `id_cliente` por lo que, al hacer un Natural Join, esta será la columna utilizada para unir las tablas.

```sql
SELECT *
FROM clientes
NATURAL JOIN pedidos;
```
| id_cliente | nombre |       email       | id_pedido |  producto  | cantidad |
|:----------:|:------:|:-----------------:|:---------:|:----------:|:--------:|
| 1          | Juan   | juan@example.com  | 1         | Laptop     | 1        |
| 2          | María  | maria@example.com | 2         | Tablet     | 2        |
| 3          | Pedro  | pedro@example.com | 3         | Smartphone | 1        |

Ejercicio:

Se tiene las siguiente stablas:

Tabla **productos**
| id_producto |   nombre   |  categoría  | precio |
|:-----------:|:----------:|:-----------:|:------:|
| 1           | Laptop     | Electrónica | 800    |
| 2           | Smartphone | Electrónica | 500    |
| 3           | Camiseta   | Ropa        | 20     |
| 4           | Zapatos    | Calzado     | 50     |

Tabla **ventas**
| id_venta | id_producto | cantidad |    fecha   |
|:--------:|:-----------:|:--------:|:----------:|
| 1        | 1           | 2        | 2024-01-01 |
| 2        | 2           | 1        | 2024-01-01 |
| 3        | 3           | 3        | 2024-01-02 |
| 4        | 4           | 1        | 2024-01-02 |

Realiza una consulta utilizando **NATURAL JOIN** que muestre el nombre del producto, la cantidad vendida y la fecha de venta de cada producto vendido. Utiliza los nombres originales de las columnas.

```sql
select p.nombre, v.cantidad, v.fecha
from productos p
natural  join ventas v
```

### Natural Left join
NATURAL LEFT JOIN realiza un LEFT JOIN utilizando las columnas que tienen el mismo nombre en ambas tablas. Su uso es el siguiente:
```sql
SELECT columnas
FROM tabla1
NATURAL LEFT JOIN tabla2;
```

-   Natural Join es un JOIN que adicionalmente asume que las columnas con el mismo nombre son las columnas de unión.
-   La ventaja de usar `NATURAL JOIN` es que simplifica la escritura de la consulta, pero solo es útil cuando las columnas de unión tienen el mismo nombre y tipo de datos en ambas tablas.
-   Así como para JOIN la opción de INNER es implícita, para NATURAL JOIN la opción de INNER también es implícita. y uno puede utilizar NATURAL INNER JOIN, NATURAL LEFT JOIN, NATURAL RIGHT JOIN.

Ejercicio:
Dada las tablas entregadas, crea un reporte que seleccione a todos los estudiantes (sus nombres), cursos inscritos y fecha de inscripciones. Si un estudiante no tiene cursos inscritos, se debe mostrar el estudiante sin los datos de inscripción.

Tabla **Estudiantes**

| id_estudiante | nombre | email              |
|---------------|--------|--------------------|
| 1             | Carlos | carlos@example.com |
| 2             | Laura  | laura@example.com  |
| 3             | Miguel | miguel@example.com |
| 4             | Ana    | ana@example.com    |

Tabla **inscripciones**

| id_inscripcion | id_estudiante | curso       | fecha       |
|----------------|---------------|-------------|-------------|
| 1              | 1             | Matemáticas | 2024-03-01  |
| 2              | 2             | Historia    | 2024-03-02  |
| 3              | 1             | Física      | 2024-03-03  |
| 4              | 3             | Química     | 2024-03-04  |


```SQL
SELECT E.NOMBRE, I.CURSO, I.FECHA
FROM ESTUDIANTES E
NATURAL  LEFT  JOIN INSCRIPCIONES I
```

### Self join
Un self join es un tipo de join en SQL que se utiliza para combinar una tabla consigo misma. Se usa cuando queremos relacionar filas de una tabla con otras filas de la misma tabla. Aunque el término "self join" se refiere a esta relación consigo misma, en la práctica se utilizan otros tipos de joins como INNER JOIN o LEFT JOIN para realizar esta operación
-   Un self join se utiliza para combinar una tabla consigo misma.
-   Self join no es un tipo de join específico, es solo el término utilizado para referirse a la operación de combinar una tabla consigo misma.
-   Para lograr el self join se utilizan otros tipos de joins como `INNER JOIN` o `LEFT JOIN`.

Ejemplo:
Supongamos que tenemos la tabla **empleados** con la siguiente estructura

| id_empleado | nombre | id_supervisor |
|:-----------:|:------:|:-------------:|
| 1           | Juan   | NULL          |
| 2           | María  | 1             |
| 3           | Pedro  | 1             |
| 4           | Ana    | 2             |
| 5           | Luis   | 2             |

Para obtener el nombre de **todos** los empleados junto con el nombre de su supervisor, podemos usar un self join de la siguiente manera:

```sql
SELECT e1.nombre AS nombre_empleado, e2.nombre AS nombre_supervisor
FROM empleados e1
LEFT JOIN empleados e2 ON e1.id_supervisor = e2.id_empleado;
```
Nos traería como resultado
| nombre_empleado | nombre_supervisor |
|:---------------:|:-----------------:|
| Juan            | NULL              |
| María           | Juan              |
| Pedro           | Juan              |
| Ana             | María             |
| Luis            | María             |

En este ejemplo, estamos obteniendo el nombre de cada empleado (`e1.nombre`) y el nombre de su supervisor (`e2.nombre`). El self join se realiza uniendo la tabla `empleados` consigo misma (`empleados e1 LEFT JOIN empleados e2`), utilizando la columna `id_supervisor` de `e1` y la columna `id_empleado` de `e2`.

Se utiliza `LEFT JOIN` en lugar de `INNER JOIN` para incluir a los empleados que no tienen supervisor, dado que en la consulta nos pedían los nombres de **todos** los empleados.

Ejercicio:

Se tiene la tabla **clientes** con los siguientes datos:

| id_cliente | nombre | id_cliente_referente |
|:----------:|:------:|:--------------------:|
| 1          | Juan   | NULL                 |
| 2          | María  | 1                    |
| 3          | Pedro  | 1                    |
| 4          | Ana    | 2                    |
| 5          | Luis   | 2                    |

Utilizando lo aprendido escribe una consulta que muestre el nombre de todos los clientes junto con el nombre de su cliente referente. Las columnas de la tabla resultante deben llamarse `nombre_cliente` y `nombre_cliente_referente`.

```SQL
SELECT 
	C1.NOMBRE AS NOMBRE_CLIENTE, 
	C2.NOMBRE AS NOMBRE_CLIENTE_REFERENTE
FROM CLIENTES C1
LEFT  JOIN CLIENTES C2
ON C1.ID_CLIENTE_REFERENTE = C2.ID_CLIENTE
```

### Self JOIN parte 2
Ejercicio:

Se tiene la tabla **amigos**

| id_amigo | nombre | id_amigo_conectado |
|:--------:|:------:|:------------------:|
| 1        | Carlos | NULL               |
| 2        | Laura  | 1                  |
| 3        | Miguel | 1                  |
| 4        | Ana    | 2                  |
| 5        | Luis   | 3                  |

Escribe una consulta SQL utilizando self join para obtener el nombre de cada amigo junto con el nombre de su amigo conectado. Solo se deben mostrar los amigos que tienen un amigo conectado. Las columnas de la tabla resultante deben llamarse `nombre` y `nombre_amigo_conectado`.

> Tip 1: ¿Qué tipo de join utilizarías para obtener los amigos conectados? 
> Tip 2: ¿Qué columnas de la tabla `amigos` se relacionan entre sí?
```SQL
SELECT
	A1.NOMBRE AS NOMBRE,
	A2.NOMBRE AS NOMBRE_AMIGO_CONECTADO
FROM AMIGOS A1
INNER  JOIN AMIGOS A2
ON A1.ID_AMIGO_CONECTADO = A2.ID_AMIGO
```
### Cross Join
El `Cross join` en SQL es usado para combinar todas las filas de la primera tabla, con todas las filas de la segunda tabla. Es tambien conocido como el **Producto Cartesiano**  de dos tablas. El aspecto mas importante de utilizar un `cross join` es que no requiere de una condicion para operar.

El inconveniente con `cross join` es que regresa el resultado del producto cartesiano de dos tablas, lo que significa un numero largo de filas y uso masivo de recursos. POr lo tanto, es critico usarlo sabiamente y cuando sea necesario.

La sintaxis del `cross join` es la siguiente
```sql
SELECT columnas
FROM tabla1
CROSS JOIN tabla2;
```

Ejemplo: 
Se tienen dos tablas, una de figuras geométricas y otra de colores. Se pide generar una consulta que muestre todas las figuras junto con todos los colores posibles.
Tabla **figuras**

| id_figura | nombre_figura |
|:---------:|:-------------:|
| 1         | Círculo       |
| 2         | Cuadrado      |
| 3         | Triángulo     |

Tabla **colores**
| id_color | nombre_color |
|:--------:|:------------:|
| 1        | Rojo         |
| 2        | Verde        |
| 3        | Azul         |

La consulta SQL necesaria tendrá la siguiente estructura:
```sql
SELECT nombre_figura, nombre_color
from figuras
cross join colores;
```

El resultado será una tabla con todas las combinaciones posibles de figuras y colores:
| nombre_figura | nombre_color |
|:-------------:|:------------:|
| Círculo       | Rojo         |
| Círculo       | Verde        |
| Círculo       | Azul         |
| Cuadrado      | Rojo         |
| Cuadrado      | Verde        |
| Cuadrado      | Azul         |
| Triángulo     | Rojo         |
| Triángulo     | Verde        |
| Triángulo     | Azul         |

Ejercicio:

Se tiene una tabla de números y una tabla de pintas. Genera una consulta que muestre todos los números junto con todas las pintas posibles simulando una baraja de cartas ordenada por números de menor a mayor y las pintas en orden alfabético. Las columnas de la tabla resultante deben llamarse `numero` y `pinta`.

Tabla **numeros**
| numero |
|:------:|
| 1      |
| 2      |
| 3      |
| 4      |
| 5      |
| 6      |
| 7      |
| 8      |
| 9      |
| 10     |
| 11     |
| 12     |
| 13     |

Tabla **pintas**
|   pinta   |
|:---------:|
| Corazones |
| Diamantes |
| Tréboles  |
| Picas     |

```SQL
SELECT NUMERO, PINTA
FROM NUMEROS
CROSS  JOIN PINTAS
ORDER  BY NUMERO, PINTA
```

### Join con funciones agregadas
-   **Combinar datos de varias tablas**: La claúsula JOIN nos permite combinar filas de dos o más tablas.
-   **Escoger el tipo de JOIN**: La elección del tipo de JOIN depende de si queremos contabilizar filas sin coincidencias, si es así usamos `LEFT JOIN`, si no usamos `INNER JOIN`.
-   **Agrupar datos**: El uso de `GROUP BY` permite agrupar filas que tienen el mismo valor en una o más columnas.
-   **Funciones de agregación**: Sobre datos agrupados, podemos utilizar funciones de agregación como `SUM()`, `COUNT()`, y `AVG()`.

#### ¿Qué vamos a aprender?

En estos ejercicios trabajaremos con problemas muy comunes en el análisis de datos, donde necesitamos combinar datos de varias tablas, agruparlos y obtener información de datos agregados. A lo largo de estos de estos ejercicios aprenderemos a identificar qué tipo de JOIN utilizar para cada caso.

#### Escenario

Se tiene una tabla de productos y una tabla de ventas. Se desea hacer una consulta que muestre cada producto con la cantidad de ventas realizadas.

Tabla **productos**

| id |   nombre   |
|:--:|:----------:|
| 1  | smartphone |
| 2  | tablet     |
| 3  | camiseta   |
| 4  | zapatos    |

Tabla **ventas**
Para este primer ejercicio vamos a suponer que la tabla de ventas solo permite registrar la venta de un producto a la vez.
| id | id_producto |
|:--:|:-----------:|
| 1  | 1           |
| 2  | 1           |
| 2  | 2           |
| 2  | 2           |
| 3  | 1           |

Si miramos las ventas, veremos que el producto con `id=1` se vendió 3 veces y el producto con `id=2` se vendió 2 veces, y el resto no se ha vendido. Es decir, el resultado esperado sería:

|   nombre   | cantidad_ventas |
|:----------:|:---------------:|
| smartphone | 3               |
| tablet     | 2               |
| camiseta   | 0               |
| zapatos    | 0               |

La solución a este ejercicio requiere de unir las tablas `productos` y `ventas` y agrupar los resultados por el nombre del producto para finalmente contar el número de ventas realizadas.

La pregunta importante es: ¿Qué tipo de JOIN deberíamos usar para este caso? ¿`INNER JOIN` o `LEFT JOIN`?

Para tomar la decisión, debemos considerar si queremos contabilizar productos sin ventas. Si queremos contabilizarlos, entonces deberíamos usar un `LEFT JOIN`. Si no queremos contabilizarlos, entonces deberíamos usar un `INNER JOIN`. En el ejemplo, la tabla del reporte muestra camisetas y zapatos que no han sido vendidos, por lo que deberíamos usar un `LEFT JOIN`.

```sql
SELECT p.nombre, COUNT(v.id) AS cantidad_ventas
FROM productos p
LEFT JOIN ventas v ON p.id = v.id_producto
GROUP BY p.nombre;
```

#### Ejercicio

Se tiene una tabla de usuarios y una tabla de notas. Se desea hacer una consulta que muestre la cantidad de notas que ha registrado cada usuario incluso si no ha registrado ninguna nota. Las columnas de las tablas deben ser `email` y `cantidad_notas`. Ordena el resultado por la cantidad de notas.

Tabla **usuarios**
|            email           |     nombre     |
|:--------------------------:|:--------------:|
| juan.perez@example.com     | Juan Pérez     |
| maria.gonzalez@example.com | Maria González |
| john.doe@example.com       | John Doe       |
| francisco@example.com      | Test User      |

Tabla **notas**

|            email           | notas |
|:--------------------------:|:-----:|
| juan.perez@example.com     | 90    |
| maria.gonzalez@example.com | 100   |
| john.doe@example.com       | 80    |
| juan.perez@example.com     | 100   |
| maria.gonzalez@example.com | 100   |

```SQL
SELECT U.EMAIL,  COUNT(N.NOTAS)  AS CANTIDAD_NOTAS
FROM USUARIOS U
LEFT  JOIN NOTAS N
ON U.EMAIL = N.EMAIL
GROUP  BY U.EMAIL
```
