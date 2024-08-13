## Tema 19: Cardinalidad

:arrow_up: [ir al inicio](./README.md#tabla-de-contenidos)

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

**#### Ejercicio**

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

**#### Ejercicio**

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

**#### Ejercicio**

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

**#### Ejercicio** 
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

#### Ejercicio:

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

**#### Ejercicio**:

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