## Tema 15: Tablas
:arrow_up: [ir al inicio](./README.md#tabla-de-contenidos)
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
