## Tema 5: Operaciones con string

:arrow_up: [ir al inicio](./README.md)

### Transformando un string en mayusculas
Para transformar un string a mayusculas en [*SQLITE*](https://www.sqlite.org/) podemos utilizar la funcion UPPER()
UPPER() es una funcion de cadena incorporada en SQL. Como lo sugiere su nombre, es unada para convertir todas las letras en una cadena especificada a mayusculas
La sintaxis de la funcion es la siguiente:

```
UPPER(string)
```

Ejercicio
Se tiene una tabla de usuarios con las columnas nombre, apellido, email y teléfono.

Selecciona los emails de la tabla usuarios con el alias email_upper. Todos los emails deben ser mostrados en mayúsculas.

```
SELECT UPPER(email) as email_upper FROM usuarios
```

### Trasformando un string a minúsculas
La funcion LOWER() es una funcion incorporada en que transforma todos los caracteres en mayusculas a minusculas, puede resultar muy util al realizar operaciones de búsqueda o comparaciones que nos e distinguen entre mayusculas o minusculas.

Ejercicio
Se tiene una tabla de usuarios con los campos id, nombre, e email. El campo email es de tipo texto y contiene algunas mayúsculas, lo que puede ocasionar errores en la base de datos.

Selecciona los emails de la tabla usuarios con el alias email_lower. Todos los emails deben ser mostrados en minúsculas.

```
select lower(email) as email_lower
from usuarios
```

### Quitando los espacios en blanco de un string
En SQLite la función TRIM() se utiliza para eliminar los espacios en blanco iniciales y finales de un string.

Por ejemplo, si tenemos una tabla de productos con una columna 'nombre' que contiene espacios en blanco al inicio y final de cada nombre, podemos utilizar la siguiente consulta para quitar esos espacios:

```SELECT TRIM(nombre) FROM productos;```

Esto nos devolverá los nombres de los productos sin los espacios en blanco al inicio y final.

Ejercicio
Se tiene una tabla de usuarios con las columnas nombre, apellido, email y teléfono. Los nombres y correos poseen espacios en blanco tanto al inicio como al final de su valor. Utiliza la función TRIM() para seleccionar los nombres e emails y quitar los espacios en blanco.

```
select trim(nombre), trim(email) from usuarios
```

### Combinando funciones
En SQL podemos combinar funciones. Veamos un ejemplo combinando LOWER y TRIM:

```
SELECT LOWER(TRIM(email)) as email_limpios from usuarios;
```

Esta consulta selecciona los correos electronicos de la tablka 'usuarios', los convierte a minusculas y elimina cualquier espacio adicional alrededor de ellos.

Ejercicio:
Se tiene una tabla de usuarios con las columnas nombre, apellido, email y teléfono. Los nombres, apellidos y correos poseen espacios en blanco tanto al inicio como al final y algunos de ellos tienen mayúsculas.

Utiliza lo aprendido para seleccionar los nombres, emails y apellidos, limpiando cada uno de estos campos. Para que el resultado sea correcto debes ocupar los alias nombre_limpio, apellido_limpio e email_limpio respectivamente.

```
select lower(trim(nombre)) as nombre_limpio, lower(trim(apellido)) as apellido_limpio, lower(trim(email)) as email_limpio
from usuarios
```

### Obteniendo el largo de un string
En SQL LENGTH es una funcion incorporada que te permite encontrar la cantidad de caracteres de una cadena o la longitud de una cadena

```
LENGTH(string)
```

Por ejemplo, si queremos obtener la longituf del nombre de todos los usuarios en la tabla 'usuarios' podriamos utilzar la siguiente consulta

```
SELECT nombre, LENGTH(nombre) FROM usuarios;
```

Ejercicio:
Selecciona el largo del apellido de todos los usuarios en la tabla usuarios.

```
select length(apellido) from usuarios
```

### Obteniendo el nombre mas largo de la tabla
Ejercicio:
Se tiene una tabla usuarios con las columnas nombre, apellido, email y teléfono.

Utiliza lo aprendido para seleccionar el largo de los 3 correos más largos de la tabla. La columna resultante debe mostrar sólo el largo (cantidad de caracteres) de estos correos.

```
select length(email) from usuarios order by length(email) desc limit 3
```

### Ordenando todos los datos y la funcion
Ejercicios
Se tiene una tabla usuarios con las columnas nombre, apellido, email y teléfono.

Utiliza lo aprendido para seleccionar los 3 correos más largos de la tabla. El resultado debe mostrar dos columnas: una con los emails y otra con sus largos respectivos.

```
SELECT email, length(email) 
FROM usuarios 
ORDER BY length(email) DESC 
LIMIT 3
```

### Concatenar strings
CONCAT es una funcion de SQL que te permite concatenar o unir dos o mas cadenas de caracteres. Esto es extremadamente util siempre que necesites combinar  texto de varias columnas en una sola.

La sintaxis de CONCAT es bastante simple:

```
CONCAT (string1, string2, ..., string_n)
```

Esta funcion acepta como entrada cualquier numero de argumentos de cadena desde dos hasta tantos como sea necesario y devuelve una nueva cadena que es el resultado de todas las cadenas de entradas unidas.

Un ejemplo de consulta de concatenacion seria la siguiente:

```
SELECT nombre || ' ' || apellido AS nombre_completo FROM empleados;
```

En esta consulta, estamos concatenando el nombre y el apellido de cada empleado, separados por un espacio, y utilizando el alias 'nombre_completo' para la nueva columna creada

Ejercicio
Supongamos que tienes una tabla llamada productos con los campos 'producto', 'marca' y 'precio'. Selecciona una lista de todos los productos con su nombre, seguido de un guion ("-"), y su marca. Asigna el alias 'marca_producto' a la columna creada.

```
select producto ||'-' ||marca as marca_producto from productos
```

> En SQL, ambas formas de concatenar strings son válidas, pero dependen del sistema de gestión de bases de datos que estés utilizando.
CONCAT (string1, string2, ..., string_n): Esta es la función de concatenación estándar que se utiliza en muchos sistemas de gestión de bases de datos, como MySQL, SQL Server, PostgreSQL, etc. En esta función, se proporcionan los strings que se desean concatenar como argumentos separados por comas.
Ejemplo:
```
SELECT CONCAT(nombre, ' ', apellido) AS nombre_completo FROM empleados;
```
> SELECT nombre || ' ' || apellido AS nombre_completo FROM empleados;: Esta sintaxis con doble barra vertical (||) es específica de algunos sistemas de gestión de bases de datos, como Oracle y SQLite. Se utiliza para concatenar strings.
Ejemplo:
```
SELECT nombre || ' ' || apellido AS nombre_completo FROM empleados;
```
> Ambas formas de concatenación hacen esencialmente lo mismo: combinan los valores de los campos especificados en una sola cadena. La diferencia principal radica en la sintaxis específica del sistema de gestión de bases de datos que estés utilizando.

### Seleccionando caracteres de un string con SUBSTR
LA funcion SQL SUBSTRING se utiliza para extraer una parte de una cadena, donde puede especificar ña posicion inicial y la longitud del texto. Esta funcion puede resultar muy beneficiosa cuando solo necesitas una parte especifica de una cadena

Sintaxis:
```
SUBSTRING(string, start, length)
```

Ejercicio
Se tiene una tabla usuarios con las columnas id, nombre, apellido, email y teléfono. Utiliza la función SUBSTR para seleccionar las tres primeras letras del apellido de cada usuario en la tabla 'usuarios'. Asigna el nombre 'primeras_letras' a la columna creada.

```
select substring(apellido, 1, 3) as primeras_letras
from usuarios
```
### Seleccionando caracteres
Se tiene una tabla de usuarios con las columnas nombre y apellido. Utilizando la función SUBSTR(), selecciona 3 caracteres del apellido de María, partiendo desde el segundo caracter. Asigna el alias 'tres_caracteres_del_apellido' a la columna creada.

```
select substring(apellido, 2, 3) as tres_caracteres_del_apellido
from usuarios
where nombre = 'María'
```

