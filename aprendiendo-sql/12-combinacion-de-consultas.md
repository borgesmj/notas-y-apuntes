## Tema 12: Combinacion de consultas

:arrow_up: [ir al inicio](./README.md#tabla-de-contenidos)

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
