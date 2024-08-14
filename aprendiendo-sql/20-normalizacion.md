## Introducción a la primera linea formal
-   La redundancia en una base de datos puede llevar a inconsistencias a la hora de identificar el dato correcto, actualizarlo o eliminarlo.
-   La normalización es un proceso de eliminación de redundancia en una base de datos

### ¿Que es la normalización?
Es el proceso de eliminar redundancias en una base de datos con el objetivo de prevenir inconsistencias. Este proceso consta de diversas etapas que, al aplicarse correctamente, permite que la base de datos sea mas eficiente y facil de mantener. Cada una de estas etapas recibe el nombre de `formas`

### Primera forma normal
En la primera forma normal se busca que cada registro sea identificable de forma única en una tabla. Veamos un ejemplo de una tabla que no cumple con la primera forma normal:

| Nombre |  Apellido | Estado Civil |
|:------:|:---------:|:------------:|
| Juan   | Pérez     | Casado       |
| María  | González  | Soltera      |
| Pedro  | Rodríguez | Casado       |
| Juan   | Pérez     | Soltero      |
| María  | González  | Viuda        |
| Pedro  | Rodríguez | Soltero      |
| Juan   | Pérez     | Divorciado   |
| María  | González  | Soltera      |
| Pedro  | Rodríguez | Casado       |

En esta tabla, si preguntamos por el estado civil de Juan Pérez, no sabríamos cuál es el correcto. Además, ¿es Juan Pérez una persona o son personas distintas y es una coincidencia que tengan el mismo nombre y apellido? Este es uno de los problemas que se busca solucionar con la primera forma normal.

#### Ejercicio

Supongamos que cada combinación de nombre y apellido de la tabla **personas**, previamente descrita, corresponde a una única persona, y el último registro de cada persona es el correcto. Borra los registros incorrectos.

> Hay formas de hacerlo automático, pero puedes simplemente borrar los registros incorrectos uno por uno separando las consultas con punto y coma. Es un trabajo tedioso, pero no olvidarás la lección de tener tablas que cumplan con la primera forma normal.

```sql
DELETE  FROM personas
WHERE  NOT  (nombre =  'Juan'  and apellido ='Pérez');
DELETE  FROM personas
WHERE id NOT  IN  (
		SELECT  MAX(id)
		FROM personas
		GROUP  BY nombre, apellido 
	);
```

## Convirtiendo a 1fn
-   La redundancia en una base de datos puede llevar a inconsistencias a la hora de identificar el dato correcto, actualizarlo o eliminarlo.
-   La normalización es un proceso de eliminación de redundancia en una base de datos
-   En primera forma normal debería haber una clave primaria que identifique de forma única a cada registro en una tabla.

#### Primera forma normal

En la primera forma normal, denotada como **1fn**, se busca que cada registro sea identificable de forma única en una tabla. Veamos un ejemplo de una tabla que no cumple con la primera forma normal:

| Nombre |  Apellido | Estado Civil |
|:------:|:---------:|:------------:|
| Juan   | Pérez     | Casado       |
| María  | González  | Soltera      |
| Pedro  | Rodríguez | Casado       |
| Juan   | Pérez     | Soltero      |
| María  | González  | Viuda        |
| Pedro  | Rodríguez | Soltero      |
| Juan   | Pérez     | Divorciado   |
| María  | González  | Soltera      |
| Pedro  | Rodríguez | Casado       |

En esta ocasión vamos a suponer que cada combinación de nombre y apellido de la tabla **personas** corresponde a una única persona, por lo tanto Juan Pérez con estado civil Casado, Soltero y Divorciado, son personas distintas. Para convertir esta tabla en primera forma normal agregaremos una clave primaria que identifique de forma única a cada registro.

> En SQLite no podemos agregar una clave primaria a una tabla que ya tiene datos, por lo que tendremos que crear una nueva tabla con la clave primaria y luego insertar los datos de la tabla original en la nueva tabla.
```sql
CREATE TABLE personas2 (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre TEXT NOT NULL,
  apellido TEXT NOT NULL,
  estado_civil TEXT NOT NULL
);

/* Seleccionamos los datos de personas y lo insertamos en personas2 */
INSERT INTO personas2 (nombre, apellido, estado_civil)
SELECT nombre, apellido, estado_civil
FROM personas;

/* Borramos la tabla personas */
DROP TABLE personas;

/* Renombramos la tabla personas2 a personas */
ALTER TABLE personas2 RENAME TO personas;
```

Esto dará como resultado esta tabla

| id | Nombre |  Apellido | Estado Civil |
|:--:|:------:|:---------:|:------------:|
| 1  | Juan   | Pérez     | Soltero      |
| 2  | María  | González  | Casada       |
| 3  | Pedro  | Rodríguez | Divorciado   |
| 4  | Juan   | Pérez     | Casado       |
| 5  | María  | González  | Soltera      |
| 6  | Pedro  | Rodríguez | Casado       |
| 7  | Juan   | Pérez     | Soltero      |
| 8  | María  | González  | Viuda        |
| 9  | Pedro  | Rodríguez | Soltero      |
| 10 | Juan   | Pérez     | Divorciado   |
| 11 | María  | González  | Soltera      |
| 12 | Pedro  | Rodríguez | Casado       |

#### Ejercicio

En el ejercicio anterior descubrimos los problemas que puede traer una tabla que no tiene clave primaria, al no poder identificar de forma única a cada registro.

Se tiene la siguiente tabla de **productos**

| Producto | Categoría | Precio |
|:--------:|:---------:|:------:|
| Manzana  | Fruta     | 0.50   |
| Pan      | Panadería | 1.00   |
| Leche    | Lácteos   | 1.20   |
| Manzana  | Fruta     | 0.55   |
| Pan      | Panadería | 1.10   |
| Queso    | Lácteos   | 2.50   |

Los productos que aparecen en la tabla aunque tengan el mismo nombre, son productos distintos. Se pide agregar una clave primaria a la tabla que identifique de forma única a cada producto.

> Ten en cuenta que no puedes agregar una clave primaria a una tabla que ya tiene datos, por lo que tendrás que crear una nueva tabla con la clave primaria y luego insertar los datos de la tabla original en la nueva tabla.
```sql
-- CREAMOS LA TABLA COPIA
CREATE  TABLE PRODUCTOS2 (
ID INTEGER  PRIMARY  KEY  AUTOINCREMENT,
Producto TEXT NOT  NULL,
Categoría TEXT NOT  NULL,
Precio REAL  NOT  NULL
);

-- INSERTAMOS LOS VALORES DE LA TABLA 1 A LA TABLA 2
INSERT  INTO PRODUCTOS2 (Producto, Categoría, Precio)
SELECT Producto, Categoría, Precio
FROM PRODUCTOS;

-- BORRAMOS LA TABLA ORIGINAL
DROP  TABLE PRODUCTOS;

-- CAMBIAMOS EL NOMBRE
ALTER  TABLE PRODUCTOS2 RENAME  TO PRODUCTOS;
```

### Grupos repetitivos
#### Ideas clave

-   La redundancia en una base de datos puede llevar a inconsistencias a la hora de identificar el dato correcto, actualizarlo o eliminarlo.
-   La normalización es un proceso de eliminación de redundancia en una base de datos
-   En primera forma normal debería haber una clave primaria que identifique de forma única a cada registro en una tabla.
-   Los grupos repetitivos son un indicio de que una tabla no cumple con la primera forma normal.

#### ¿Qué son los grupos repetitivos?

Los grupos repetitivos son un conjunto de campos que se repiten en una tabla. Por ejemplo, si en una tabla se tienen los campos `telefono1`, `telefono2` y `telefono3`, se podría considerar que estos campos forman un grupo repetitivo.

| id | nombre | apellido | telefono1 | telefono2 | telefono3 |
|:--:|:------:|:--------:|:---------:|:---------:|:---------:|
| 1  | Juan   | Pérez    | 12345678  | 87654321  | 45678912  |
| 2  | María  | González | 23456789  | 98765432  | 56789123  |

Existen diversos problemas asociados a los grupos repetitivos, pero en este caso puntual hay dos problemas evidentes:

1.  ¿Qué pasa si una persona tiene más de tres teléfonos? ¿Se debería modificar la tabla para agregar un campo `telefono4`, `telefono5`, etc.? ¿Cuál es el límite?
    
2.  Si la mayoría de las personas solo tienen un teléfono, ¿cómo se maneja la información de los campos `telefono2` y `telefono3`? ¿Se dejan en blanco? ¿Se les asigna un valor nulo? Probablemente terminemos con una gran cantidad de campos vacíos.
   

Resolver el problema de los grupos repetitivos es un paso importante en la normalización de una base de datos. En este caso, se podría crear una tabla `telefonos` que contenga los teléfonos de las personas y se relacione con la tabla `personas`, quedando de la siguiente manera:

Tabla **personas**
| id | nombre | apellido |
|:--:|:------:|:--------:|
| 1  | Juan   | Pérez    |
| 2  | María  | González |

Tabla **Telefonos**
| id_persona | telefono |
|:----------:|:--------:|
| 1          | 12345678 |
| 1          | 87654321 |
| 1          | 45678912 |
| 2          | 23456789 |
| 2          | 98765432 |
| 2          | 56789123 |

De esta forma, se puede tener un número arbitrario de teléfonos por persona sin necesidad de modificar la estructura de la tabla `personas`.

#### Ejercicio

Dada la siguiente tabla, identifica los grupos repetitivos y propón una solución para normalizar la tabla.

tabla **empleados_desnormalizado**:

| id | nombre | apellido | proyecto1 | proyecto2 | proyecto3 |
|:--:|:------:|:--------:|:---------:|:---------:|:---------:|
| 1  | Juan   | Pérez    | 1         | 2         | 3         |

1.  Identifica los grupos repetitivos en la tabla `empleados_desnormalizado`.
2.  Crea las tablas **empleados** y **proyectos** en primera forma normal para que permitan almacenar la información de los empleados y los proyectos en una estructura normalizada.
3.  Ingresa la información de la tabla `empleados_desnormalizado` en las tablas normalizadas.

Crea una consulta que muestre la información de los empleados y los proyectos a los que están asignados en una estructura normalizada. Las columnas de la consulta deben ser `nombre`, `apellido` y `id_proyecto`.

```SQL
-- CREAMOS LA TABLA EMPLEADOS
CREATE  TABLE EMPLEADOS(
	ID INT  PRIMARY  KEY,
	NOMBRE TEXT,
	APELLIDO TEXT
);

-- INSERTAMOS LOS VALORES
INSERT  INTO EMPLEADOS VALUES
	(1,  'Juan',  'Pérez');

-- CREAMOS LA TABLA PROYECTOS
CREATE  TABLE PROYECTOS(
	ID_EMPLEADO INT,
	ID_PROYECTO INT,
	FOREIGN  KEY  (ID_EMPLEADO)  REFERENCES EMPLEADOS(ID)
);

-- iNSERTAMOS LOS VALORES
INSERT  INTO PROYECTOS VALUES
	(1,1),
	(1,2),
	(1,3);

-- REALIZAMOS LA CONSULTA
SELECT E.NOMBRE, E.APELLIDO, P.ID_PROYECTO
FROM EMPLEADOS E
JOIN PROYECTOS P
ON E.ID = P.ID_EMPLEADO
```

## Grupos repetitivos parte 2
-   La redundancia en una base de datos puede llevar a inconsistencias a la hora de identificar el dato correcto, actualizarlo o eliminarlo.
-   La normalización es un proceso de eliminación de redundancia en una base de datos
-   En primera forma normal debería haber una clave primaria que identifique de forma única a cada registro en una tabla.
-   Los grupos repetitivos son un indicio de que una tabla no cumple con la primera forma normal.
-   Hay más de un forma de tener grupos repetitivos en una tabla

#### Grupos repetitivos

Los grupos repetitivos son conjuntos de campos que se repiten dentro de una tabla. Sin embargo, existen varias formas en las que estos grupos repetitivos pueden aparecer en una tabla.

En el ejercicio anterior, se vio un ejemplo de un grupo repetitivo en el que se tenían varios campos con el mismo propósito. Por ejemplo: `telefono1`, `telefono2` y `telefono3`. Otra forma de tener grupos repetitivos es tener varios valores en un solo campo.
| id | Nombre Completo |                     Teléfonos                     |
|:--:|:---------------:|:-------------------------------------------------|
| 1  | Juan Pérez      | +56 9 1234 5678, +56 2 2345 6789, +56 9 8765 4321 |
| 2  | Pedro Rodríguez | +56 9 4321 9876, +56 2 6789 5432                  |
| 3  | Ana López       | +56 9 8765 2345, +56 2 4321 1987, +56 9 6789 5432 |

Los problema asociados a esta forma de grupos repetitivos son distintos:

-   Al modificar el teléfono de una persona, se debe modificar el campo `Teléfonos` que tiene varios registros y podríamos olvidar alguno o pasarlo a llevar por error.
-   Al tener los datos almacenados de esta forma es difícil saber cuanto teléfonos tiene cada persona.
-   Los teléfonos podrían tener distintos formatos y sería difícil establecer una restricción para que todos los teléfonos tengan el mismo formato.
-   Verificar si el mismo teléfono está asignado a más de una persona también se vuelve más complicado que al tener la tabla desnormalizada.

Por ejemplo, si quisiéramos contar la cantidad de teléfonos de cada persona, podríamos contar la cantidad de símbolos + en el campo Teléfonos. Para lograr esto, podemos calcular la cantidad total de caracteres en el campo Teléfonos y restarle la cantidad de caracteres en el mismo campo después de eliminar los símbolos +.

```sql
SELECT
    id,
    nombre_completo,
    LENGTH(telefonos) - LENGTH(REPLACE(telefonos, '+', '')) AS cantidad_telefonos
FROM
    personas;
```

Como se observa, es mucho más complicado que simplemente contar los registros de una tabla

#### Ejercicio

Se tiene la tabla **pedidos** que tiene una columna `id` y otra columna `productos`. Se pide que cuentes la cantidad de productos que tiene cada pedido en esta tabla no normalizada.

| id |                      productos                     |
|:--:|:--------------------------------------------------|
| 1  | producto1 producto2 producto3                      |
| 2  | producto4 producto5                                |
| 3  |                                                    |
| 4  | producto6 producto7 producto8 producto9 producto10 |
| 5  | producto11                                         |

Para simplificar el problema dentro de la tabla de sql, los productos están separados por un espacio y no hay espacios al principio ni al final de la cadena.

```sql
SELECT
ID,
PRODUCTOS,
LENGTH(productos)  - LENGTH(REPLACE(productos,  ' ',  ''))  +1
FROM PEDIDOS
```

> Aqui lo que vemos es una simple resta, entre la longitud total de la casilla LENGTH(productos) menos las misma casilla sin los espacios entre cada producto LENGTH(REPLACE(productos,  ' ',  '')) todas estas restas nos dara la cantidad de espacios eliminados, asi que se le suma 1 para los productos que estan al comienzo de cada lista.

## Grupos repetitivos 3
-   Los grupos repetitivos son un indicio de que una tabla no cumple con la primera forma normal.
-   Hay grupos repetitivos cuando tienes columnas que se repiten en una tabla, ejemplo: `proyecto1`, `proyecto2`, `proyecto3`.
-   Hay grupos repetitivos cuando tienes dentro de un campo varios valores, ejemplo: `producto1 producto2 producto3`.
-   Finalmente hay grupos repetitivos cuando tienes columnas que se repiten en varias filas, ejemplo: `nombre`, `apellido

Veamos por ejemplo la tabla departamentos:

| nombre_departamento | nombre_persona | apellido_persona |
|:-------------------:|:--------------:|:----------------:|
| Recursos Humanos    | Ana            | Pérez            |
| TI                  | Pedro          | Rodríguez        |
| TI                  | Luis           | González         |
| Marketing           | Marta          | López            |
| Marketing           | Elena          | Pérez            |

La tabla anterior, aunque sea un poco más difícil de evidenciar, también tiene grupos repetitivos. Dado que `nombre_departamento` se repite en varias filas para distintas personas.

Por ejemplo esto mismo podría estar como

| nombre_departamento |            personas            |
|:-------------------:|:------------------------------:|
| Recursos Humanos    | Ana Pérez                      |
| TI                  | Pedro Rodríguez, Luis González |
| Marketing           | Marta López, Elena Pérez       |

O como:

| nombre_departamento | Nombre Persona 1 | Nombre Persona 2 | Nombre Persona 3 |
|:-------------------:|:----------------:|:----------------:|:----------------:|
| Recursos Humanos    | Ana              |                  |                  |
| TI                  | Pedro            | Luis             |                  |
| Marketing           | Marta            | Elena            |                  |

Los problemas asociados a los grupos repetitivos son similares a los que se presentan en los ejercicios anteriores.

-   Si se quiere cambiar el nombre de un departamento, se tendría que cambiar en todas las filas que correspondan a ese departamento.
-   O un departamento podría quedar escrito de distintas formas, por ejemplo, TI, T.I., Tecnologías de la Información, etc. Y sería difícil establecer una restricción para que todos los departamentos tengan el mismo nombre.

Para eliminar los grupos repetitivos de esta tabla, se debe crear una nueva tabla `Personas` separada de la tabla `Departamentos` que relacione a las personas con los departamentos.

Departamentos
| id | nombre_departamento |
|:--:|:-------------------:|
| 1  | Recursos Humanos    |
| 2  | TI                  |
| 3  | Marketing           |

Personas

| id | nombre_persona | apellido_persona | departamento_id |
|:--:|:--------------:|:----------------:|:---------------:|
| 1  | Ana            | Pérez            | 1               |
| 2  | Pedro          | Rodríguez        | 2               |
| 3  | Luis           | González         | 2               |
| 4  | Marta          | López            | 3               |
| 5  | Elena          | Pérez            | 3               |

#### Ejercicio Didáctico

Con las tablas normalizadas de `Departamentos` y `Personas`. Muestra todos los departamentos y cuántas personas trabajan en cada uno. Las columnas deben llamarse `nombre_departamento` y `cantidad_personas`.

```SQL
SELECT 
	D.NOMBRE_DEPARTAMENTO,  
	COUNT(P.NOMBRE_PERSONA)  AS CANTIDAD_PERSONAS
FROM DEPARTAMENTOS D
JOIN PERSONAS P
ON D.ID = P.DEPARTAMENTO_ID
GROUP  BY D.NOMBRE_DEPARTAMENTO
ORDER  BY D.NOMBRE_DEPARTAMENTO ASC
```
