## Tema 13: Insercion de registros

:arrow_up: [ir al inicio](./README.md#tabla-de-contenidos)

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
El formato de fecha es `YYYY-MM-DD`o sea, año.mes-tema, donde el año es de 4 digitos, el mes de dos digitos, y el tema de dos digitos.

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

En una base de datos de SQL, es posible agilizar el proceso de insercion de datos en una tabla metemante el uso de un campo autoincremental.Este tipo de campo es especialmente util cuando se trata de gestionar indentificadores unicos, como por ejemplo, el campo de 'id' de una tabla. La caracteristica de autoincremento se logra empleando la clausula AUTOINCREMENT en la definicion del campo.
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

