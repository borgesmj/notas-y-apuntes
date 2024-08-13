## Tema 11: Subconsultas

:arrow_up: [ir al inicio](./README.md#tabla-de-contenidos)

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
