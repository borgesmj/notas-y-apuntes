## Tema 9: Introducción a grupos
:arrow_up: [ir al inicio](./README.md#tabla-de-contenidos)
### Agrupando valores con GROUUP BY
La clausula GROUP BY es una poderosa gherramienta en SQL que se utilizar para agrupar filas con valores identicos en una o varias columnas especificas, permitiendo realizar operaciones de agregacion en ada grupo.

Esta clausula viene dentro de la categoria de FUNCIONES DE GRUPO, asi como `count`, `sum`, `Average`, etc.

La sintaxis para GROUP BY es 
```
SELECT column1, column2
FROM table_name
GROPU BY column1, column2
```


Ejemplo:

Asumamos que tenemos una tabla llamada "sales". Esta tabla tiene tres columnas: ID, Item, y Ammount



| ID | Item | Amount |
|----|------|--------|
| 1  | A    | 150    |
| 2  | B    | 200    |
| 3  | A    | 100    |
| 4  | B    | 50     |
| 5  | A    | 200    |
| 6  | A    | 100    |
| 7  | B    | 150    |

Ejecutamos el siguiente comando de SQL

```
SELECT item, sum(Amount)
FROM sales
GROUP BY Item;
```

El codigo va a concatenar, o "agrupar" todos los items que sean los mismos a una nueva fila, aplicando la funciion SUM(). La salida será:

| Item | SUM(amount) |
|------|-------------|
| A    | 550         |
| B    | 400         |

Tenemos la siguiente tabla colores:

| COLOR    |
|----------|
| Rojo     |
| Azul     |
| Verde    |
| Amarillo |
| Naranja  |
| Morado   |
| Rosa     |
| Café     |
| Gris     |
| Negro    |
| Blanco   |
| Rojo     |
| Azul     |
| Verde    |
| Amarillo |

Podemos seleccioar los elementos unicos utilizando GROUP BY de la siguiente forma

```
SELECT color as color_unico
FROM colores
GROUP BY color
```

como resultado obtendremos


| COLOR    |
|----------|
| Amarillo |
| Azul     |
| Blanco   |
| Café     |
| Gris     |
| Morado   |
| Naranja  |
| Negro    |
| Rojo     |
| Rosa     |
| Verde    |

Ejercicio:
Dada la siguiente tabla de usuarios:

| CORREO                       |
|------------------------------|
| juan.perez@empresa.com       |
| maria.gonzalez@empresa.com   |
| carlos.rodriguez@empresa.com |
| ana.martinez@empresa.com     |
| luis.garcia@empresa.com      |
| carmen.lopez@empresa.com     |
| jose.hernandez@empresa.com   |
| francisco.martin@empresa.com |
| laura.sanchez@empresa.com    |
| antonio.temaz@empresa.com     |
| juan.perez@empresa.com       |
| maria.gonzalez@empresa.com   |

Crea una consulta que nos muestre cada correo una unica vez. La columna mostrada deberá llamarse `correo_unico`

```
SELECT correo as correo_unico
FROM usuarios
GROUP BY correo
```

### Agrupar y contar
GROUP BY es comunmente utilizada junto con funciones de agregacion como COUNT, MAX, MIN, SUM y AVG para obtener informacion resumida de un conjunto de datos

En este ejrcicio aprenderemos a agrupar y contar

Tenemos la siguiente tabla de colores

| COLOR    |
|----------|
| Rojo     |
| Azul     |
| Verde    |
| Amarillo |
| Naranja  |
| Morado   |
| Rosa     |
| Café     |
| Gris     |
| Negro    |
| Blanco   |
| Rojo     |
| Azul     |
| Verde    |
| Amarillo |


Queremos saber cuantas veces aparece cada color. esto lo podemos lograr combinando GROUP BY y la funcion de agregacion COUNT


```
SELECT color, count(color) as Repeticiones
FROM colores
GROUP BY color
```

| COLOR    | REPETICIONES |
|----------|--------------|
| Amarillo | 2            |
| Azul     | 2            |
| Blanco   | 1            |
| Café     | 1            |
| Gris     | 1            |
| Morado   | 1            |
| Naranja  | 1            |
| Negro    | 1            |
| Rojo     | 2            |
| Rosa     | 1            |
| Verde    | 2            |

Ejercicio

Dada la siguiente tabla de usuarios

| CORREO                       |
|------------------------------|
| juan.perez@empresa.com       |
| maria.gonzalez@empresa.com   |
| carlos.rodriguez@empresa.com |
| ana.martinez@empresa.com     |
| luis.garcia@empresa.com      |
| carmen.lopez@empresa.com     |
| jose.hernandez@empresa.com   |
| francisco.martin@empresa.com |
| laura.sanchez@empresa.com    |
| antonio.temaz@empresa.com     |
| juan.perez@empresa.com       |
| maria.gonzalez@empresa.com   |


Crea una consulta que nos muestre cada correo electronico una unica vez junto a la cantidad de repeticiones. LAs columnas deben llamarse correo y repeticiones

```
SELECT correo, count(correo) as repeticiones
from usuarios
group by correo
```

### Ejercitando agrupar y contar

Ejercicio
Dada la siguiente tabla empleados

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

Se pide contar cuantas personas trabajan en cada departamento. Las columnas resultantes deben llamarse departamento y cantidad_empleados

```
SELECT departamento, count(departamento) as cantidad_empleados
from empleados
group by departamento
```

### Agrupar y sumar
En este ejercicio agruparemos y sumaremos. La logica de la consulta es la misma previamente mencionada, solo cambia la funcin de agrupacion a utilizar. Por ejemplo, tenemos una tabla de pedidos con los siguientes datos:

| CLIENTE   | MONTO |
|-----------|-------|
| Cliente A | 1200  |
| Cliente A | 800   |
| Cliente B | 150   |
| Cliente C | 200   |
| Cliente B | 90    |

Si queremos calcular cuanto ha gastado cada cliente, podemos realizar la siguiente consulta:

```
SELECT Cliente, sum(Monto) as Monto_total
FROM pedidos
GrOUP BY Cliente
```

Ejercicio
Utilizando la siguiente tabla ventas e una empresa, crea una consulta que muestre cuanto vendio en total por cada categoria. Las columnas de la consulta deben llamarse categoria y monto_total

| PRODUCTO        | MONTO | CATEGORIA         |
|-----------------|-------|-------------------|
| Laptop Pro      | 1200  | Electrónicos      |
| Smartphone X    | 800   | Electrónicos      |
| Silla Ergo      | 150   | Mobiliario        |
| Mesa de Café    | 90    | Mobiliario        |
| Reloj Elegante  | 250   | Accesorios        |
| Bolso de Viaje  | 70    | Accesorios        |
| Zapatillas Run  | 100   | Ropa              |
| Camisa Casual   | 40    | Ropa              |
| Licuadora Max   | 60    | Electrodomésticos |
| Horno Compacto  | 110   | Electrodomésticos |
| Libro de Cocina | 20    | Libros            |
| Novela Misterio | 15    | Libros            |
| Audífonos Plus  | 50    | Electrónicos      |
| Lámpara Moderna | 45    | Mobiliario        |
| Laptop Pro      | 1200  | Electrónicos      |
| Silla Ergo      | 150   | Mobiliario        |
| Bolso de Viaje  | 70    | Accesorios        |
| Zapatillas Run  | 100   | Ropa              |

```
SELECT categoria as categoria, sum(monto) as monto_total
FROM ventas
group by categoria
```
### Agruopar y prometemar

Previamente aprendimos que AVG nos permite calcular el promedio de los elementos de una columna en una tabla. En este ejercicio lo utilizaremos para calcular promedios po grupo.

```
SELECT grupo, AVG(columna)
FROM tabla
GROUP BY grupo
```

Ejercicio

Dada la siguiente tabla de estutemantes


| NOMBRE_COMPLETO | NOTA |
|-----------------|------|
| Juan Pérez      | 7    |
| Juan Pérez      | 8    |
| Juan Pérez      | 6    |
| María Rodríguez | 9    |
| María Rodríguez | 7    |
| María Rodríguez | 8    |
| Carlos García   | 6    |
| Carlos García   | 5    |
| Carlos García   | 7    |
| Ana Fernández   | 8    |
| Ana Fernández   | 9    |
| Ana Fernández   | 8    |
| Luis Morales    | 7    |
| Luis Morales    | 6    |
| Luis Morales    | 5    |

Encuentra el promedio de notas de cada estutemante. Las columnas deben tener el nombre completo y promedio_notas respectivamente

Este ejercicio tiene un supuesto importante, que no hay dos estutemantes con el mismo nombre y apellido. DIscutiremos este tipo de supuestos mas adelante cuando revisemos el concepto de integridad.

```
SELECT nombre_completo, AVG(nota) as promedio_notas
FROM estutemantes
GROUP BY nombre_completo
```

### Maximo por grupo
En este ejercicio combinaremos la funcion de agregacion MAX() con GROUP BY para poder obtener el monto mas alto de cada grupo. LA sintaxis de la consulta será igual a las vistas previamente, es decir:

```
SELECT grupo. MAX(columna)
FROM tabla
GROUP BY grupo
```


Ejercicio:

Dada la siguiente tabla de ventas

| PRODUCTO        | MONTO | CATEGORIA         |
|-----------------|-------|-------------------|
| Laptop Pro      | 1200  | Electrónicos      |
| Smartphone X    | 800   | Electrónicos      |
| Silla Ergo      | 150   | Mobiliario        |
| Mesa de Café    | 90    | Mobiliario        |
| Reloj Elegante  | 250   | Accesorios        |
| Bolso de Viaje  | 70    | Accesorios        |
| Zapatillas Run  | 100   | Ropa              |
| Camisa Casual   | 40    | Ropa              |
| Licuadora Max   | 60    | Electrodomésticos |
| Horno Compacto  | 110   | Electrodomésticos |
| Libro de Cocina | 20    | Libros            |
| Novela Misterio | 15    | Libros            |
| Audífonos Plus  | 50    | Electrónicos      |
| Lámpara Moderna | 45    | Mobiliario        |
| Laptop Pro      | 1200  | Electrónicos      |
| Silla Ergo      | 150   | Mobiliario        |
| Bolso de Viaje  | 70    | Accesorios        |
| Zapatillas Run  | 100   | Ropa              |

Crea una consulta para calcular el monto mas alto por cada categoria. La tabla resultante debe tener dos columnas: categoria y monto_mas_alto

```
SELECT categoria, max(monto) as monto_mas_alto
FROM ventas
group by categoria
```
### Minimo por grupo
En este ejercicio combinaremos la funcion MIN() con GROUP BY para obtener el monto mas bajo de cada grupo. La sintaxis de la consulta será igual a las vistas previamente, es decir:

```
SELECT grupo, MIN(columna) FROM tabla GROPU BY grupo
```

Ejercicio:

Dada la tabla *ventas*

| PRODUCTO        | MONTO | CATEGORIA         |
|-----------------|-------|-------------------|
| Laptop Pro      | 1200  | Electrónicos      |
| Smartphone X    | 800   | Electrónicos      |
| Silla Ergo      | 150   | Mobiliario        |
| Mesa de Café    | 90    | Mobiliario        |
| Reloj Elegante  | 250   | Accesorios        |
| Bolso de Viaje  | 70    | Accesorios        |
| Zapatillas Run  | 100   | Ropa              |
| Camisa Casual   | 40    | Ropa              |
| Licuadora Max   | 60    | Electrodomésticos |
| Horno Compacto  | 110   | Electrodomésticos |
| Libro de Cocina | 20    | Libros            |
| Novela Misterio | 15    | Libros            |
| Audífonos Plus  | 50    | Electrónicos      |
| Lámpara Moderna | 45    | Mobiliario        |
| Laptop Pro      | 1200  | Electrónicos      |
| Silla Ergo      | 150   | Mobiliario        |

Crea una consulta para calcular el monto mas bajo por cada grupo. La tabla resultante debe tener dos columnas `categoria` y `monto_mas_bajo`

```
SELECT categoria, min(monto) AS monto_mas_bajo 
FROM ventas
GROUP BY categoria
```

### Funciones de agregacion y fechas
A la hora de construir informes, frecuentemente necesitaremos entregar informacion agrupada en un periodo de tiempo. Para lograr esto, utilizaremos una combinacion de GROUP BY con la funciuon strftime.

Tenemos la tabla *ventas* con la siguiente informacion:

| ID_VENTA | MONTO | FECHA_VENTA |
|----------|-------|-------------|
| 1        | 200   | 2010-01-15  |
| 2        | 150   | 2011-02-20  |
| 3        | 300   | 2012-03-10  |
| 4        | 250   | 2012-04-05  |
| 5        | 100   | 2014-05-25  |
| 6        | 350   | 2015-06-18  |
| 7        | 400   | 2015-07-22  |
| 8        | 180   | 2015-08-09  |
| 9        | 220   | 2018-09-30  |
| 10       | 275   | 2018-10-11  |

Se nos solicita determinar el monto total de ventas por año. Para resolverlo, tenemos qye agrupar por fecha y sumar los montos de la siguiente manera:

```
SELECT sum(monto), strftime("%Y"), fecha_venta AS año 
FROM ventas 
GROUP BY strftime("%Y", fecha_venta)
```


Ejercicio:
Utilizando esta nueva tabla de ventas

| ID_VENTA | MONTO | FECHA_VENTA |
|----------|-------|-------------|
| 1        | 200   | 2010-01-15  |
| 2        | 150   | 2010-02-20  |
| 3        | 300   | 2010-02-10  |
| 4        | 250   | 2010-04-05  |
| 5        | 100   | 2010-04-25  |
| 6        | 350   | 2010-04-18  |
| 7        | 400   | 2010-06-22  |
| 8        | 180   | 2010-06-09  |
| 9        | 220   | 2010-09-30  |
| 10       | 275   | 2010-10-11  |


Calcule el total de venta por mes El nombre de las columnas resultantes será "suma_ventas" y "mes" respectivamente.


```
SELECT sum(monto) as suma_ventas, strftime("%m", fecha_venta) as mes
FROM ventas
GROUP BY strftime("%m", fecha_venta)
```

### Ejercitando funciones de agregacion con fechas

Se tiene una tabla llamada _inscripciones_ con distintas fechas de inscrpciones de un usuario a un sitio web

| FECHA_INSCRIPCION |
|-------------------|
| 2022-01-15        |
| 2022-01-20        |
| 2022-02-10        |
| 2022-02-05        |
| 2022-03-25        |
| 2022-03-18        |
| 2022-04-22        |
| 2022-04-09        |
| 2022-05-30        |
| 2022-05-11        |
| 2022-06-19        |
| 2022-06-29        |
| 2022-07-12        |
| 2022-07-21        |
| 2022-08-08        |
| 2022-08-17        |
| 2022-09-13        |
| 2022-09-26        |
| 2022-10-14        |
| 2022-10-28        |

Cuenta cuantos usuarios se registraron cada mes. Las columnas resultantes deben llamarse "mes" y "cantidad_usuarios"

```
SELECT strftime("%m", fecha_inscripcion) as mes,  COUNT(Fecha_Inscripcion) AS cantidad_usuarios
FROM inscripciones
GROUP BY strftime("%m", fecha_inscripcion)
```

### Agrupando sin indicar el nombre de las columnas
Cuando se trata de agrupar datos e una consulta SQL, existe una forma de evitar la redundancia de la clausula SELECT. POr ejemplo, considera la siguiente consulta

```
SELECT stfrtime("%Y", fecha_venta) as año_venta, sum(monto) from ventas group by strftime("%Y", fecha_venta)
```

Podemos simplificarla de la siguiente manera

```
SELECT strftime("%Y", fecha_venta) AS año, SUM(monto)
FROM ventas
GROUP BY 1
```

En esta notacion se interpreta como "agrupa por el primer criterio". TAmbien es posible aplicar esta sintaxis en la clausula ORDEB BY

```
SELECT strftime("%Y", fecha_venta) AS año, SUM(monto)
FROM ventas 
GROUP BY 1
ORDER BY 1

```

De esta manera podemos lograr la agrupacion y ordenamiento sin repetir la expresion de la clausula SELECT

Ejercicio:
Dada la siguiente tabla de usuarios

| CORREO                       |
|------------------------------|
| juan.perez@empresa.com       |
| maria.gonzalez@empresa.com   |
| carlos.rodriguez@empresa.com |
| ana.martinez@empresa.com     |
| luis.garcia@empresa.com      |
| carmen.lopez@empresa.com     |
| jose.hernandez@empresa.com   |
| juan.perez@empresa.com       |
| carmen.lopez@empresa.com     |
| maria.gonzalez@empresa.com   |
| juan.perez@empresa.com       |
| maria.gonzalez@empresa.com   |

Crea una consulta que nos muestre cada correo una unica vez, acompañado del momento de veces que se repite. Las columnas deben llevar los nombres "correo" "repeticiones", respectivamente y deben estar ordenados alfabeticamente

```
SELECT correo, count(correo) as repeticiones
FROM usuarios
GROUP BY 1
ORDER BY 1 asc
```

### Agrupando por multiples columnas
En SQL es posible agrupas por multipes columnas utilizando la siguiente sintaxis

```
SELECT columna1, columna2 funcion_agrupado(columna3)
FROM tabla
GROUP BY columna1, columna2
```

Y como aprendimos en el ejerciio anterior, tambien podemos escribir la consulta de la siguiente manera:

```
SELECT columna1, columna2, funcion_agrupado(columna3)
FROM tabla
GROUP BT 1, 2
```

Ejercicio
Tenemos la siguiente tabla estutemantes

| CORREO                  | MATERIA     | NOTA |
|-------------------------|-------------|------|
| estutemante1@ejemplo.com | Matemáticas | 8.5  |
| estutemante2@ejemplo.com | Matemáticas | 9.0  |
| estutemante3@ejemplo.com | Matemáticas | 7.5  |
| estutemante1@ejemplo.com | Ciencias    | 8.0  |
| estutemante2@ejemplo.com | Ciencias    | 9.5  |
| estutemante3@ejemplo.com | Ciencias    | 7.0  |
| estutemante1@ejemplo.com | Historia    | 8.7  |
| estutemante2@ejemplo.com | Historia    | 9.2  |
| estutemante3@ejemplo.com | Historia    | 7.8  |

Calcula el promedio de cada estutemante en cada materia. LAs columnas deben llamarse correo, materi y promedio_notas

```
SELECT correo, materia, AVG(nota) as promedio_notas
FROM estutemantes
group by 1,2
```