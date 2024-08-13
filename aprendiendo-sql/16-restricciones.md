## Tema 16: Restricciones
:arrow_up: [ir al inicio](./README.md#tabla-de-contenidos)

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

