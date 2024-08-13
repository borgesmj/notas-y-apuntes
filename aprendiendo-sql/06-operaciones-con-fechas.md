## Tema 6: Operaciones con fechas

:arrow_up: [ir al inicio](./README.md#tabla-de-contenidos)

En SQL, DATE  es un tipo de dato que almacena la fecha. NO ALMACENA EL INFORMACION DEL TIEMPO. EL formato de la fecha es: 'YYYY-MM-DD', por ejemplo: '2022-01-01'
SQL provee de varias funciones para manipular fechas.
SQL provee de muchas funciones para manejar la fecha:

### Obteniendo la fecha de hoy 
con la funcion `DATE()` podemos obtener la fecha de hoy, por ejemplo podemos utilizar la clausula `WHERE`  para obtener los registros del tema de hoy.

```
SELECT * FROM usuarios WHERE fecha_registro = DATE();
```

Tambien es posible indicar explicitamente a la funcion que la fecha deseada es la de hoy:

```
SELECT * FROM usuarios WHERE fecha_registro = DATE('now')
```

Ejercicio
Se tiene una tabla llamada tareas con las siguientes columnas: "id" (identificador único), "descripcion" (descripción de la tarea) y "fecha_limite" (fecha límite para completar la tarea).

Obtén la descripción de todas las tareas que tengan fecha_limite igual a la fecha actual .

```
SELECT descripcion from tareas where fecha_limite = date()
```

### Obteniendo la fecha de mañana
En SQL es posible obtener fechas futuras.  En SQLite lo podemos lograr pasando un segundo argumento a la función DATE. Esto suena complicado pero es mas sencillo de lo que parece:

```
DATE('now', '1 day')
```

En este ejemplo estamos sumando 1 tema a la fecha actual (now). Si queremos sumar mas temas, por ejemplo 5 temas utilizaremos `Date('now', '5 day')`. Tambien es posible sumar semamas, meses, con:

2semanas: `DATE('now', '2 week')`
3 meses: `DATE('now', '3 month')`

Ejercicio
Se tiene una tabla de tareas con los campos id, descripcion y fecha_limite. Se pide seleccionar todos los campos de las tareas que tienen como fecha límite el día de mañana.

```
select * from tareas where fecha_limite = date('now', '1 day')
```

### Obteniendo la fecha de ayer
De la misma manera que buscamos la fecha de mañana, solo que con un numero negativo
```
DATE('now', '-1 day')
```
Ejercicio
Supongamos que tenemos una tabla llamada ganancias con las columnas "id" (identificador único), "fecha" (fecha de registro) y "monto" (ganancia del día).

Muestra el monto correspondiente al día de ayer.

```
select monto from ganancias where fecha = DATE('now', '-1 day')

```

### Extraccion del año
Para ciertos reportes es muy probable que nos pidan extraer informacin de una fecha, como por ejemplo. el año que se hizo una transaccion
Analicemos el siguiente escenario
Se tiene la tabla _ventas_ con la siguiente informacion

| ID_VENTA | MONTO | FECHA_VENTA |
|----------|-------|-------------|
| 1        | 200   | 2010-01-15  |
| 2        | 150   | 2011-02-20  |
| 3        | 300   | 2012-03-10  |
| 4        | 250   | 2013-04-05  |
| 5        | 100   | 2014-05-25  |
| 6        | 350   | 2015-06-18  |
| 7        | 400   | 2015-07-22  |
| 8        | 180   | 2015-08-09  |
| 9        | 220   | 2018-09-30  |
| 10       | 275   | 2019-10-11  |

Nos piden mostrar toda la información de la tabla y adicionalmente agregar una columna con el año de la venta.

```
SELECT *, strftime('%Y', fecha_venta) as año_venta FROM ventas 
```

El resultado de esta consulta será el siguiente

| ID_VENTA | MONTO | FECHA_VENTA | AÑO_VENTA |
|----------|-------|-------------|-----------|
| 1        | 200   | 2010-01-15  | 2010      |
| 2        | 150   | 2011-02-20  | 2011      |
| 3        | 300   | 2012-03-10  | 2012      |
| 4        | 250   | 2013-04-05  | 2013      |
| 5        | 100   | 2014-05-25  | 2014      |
| 6        | 350   | 2015-06-18  | 2015      |
| 7        | 400   | 2015-07-22  | 2015      |
| 8        | 180   | 2015-08-09  | 2015      |
| 9        | 220   | 2018-09-30  | 2018      |
| 10       | 275   | 2019-10-11  | 2019      |


Para mostrar los resultados de este tipo de funciones, es necesario asignar un nombre a la nueva columna, ya que, de lo contrario, la columna resultante mantendrá el nombre de "strftime('%Y', fecha_venta)", lo cual resultaría en una denominación poco legible para un informe

Ejercicio
Dada una tabla ventas con las columnas monto y fecha_venta, crea una consulta que muestre únicamente el monto y el año de la venta. La columna que muestre el año de la venta debe llamarse año_venta

```
select monto, strftime('%Y', fecha_venta) as año_venta from ventas
```


### Extracción del mes

En este caso, para obtener el mes, pasamos %m como argumento a la función strftime.

Ejercicio
Dada la tabla ventas previamente presentada con las columnas monto y fecha_venta, crea una consulta que muestre una tabla con el monto, el mes de la venta y el año de la venta, en ese mismo orden. La columna para el mes de la venta debe llamarse mes_venta y aquella para el año de la venta debe llamarse año_venta

```
select monto, strftime('%m', fecha_venta) as mes_venta, strftime('%Y', fecha_venta) as año_venta from ventas
```

### Extraccion del mes y año
Ejercicio
Dada la tabla ventas con las columnas monto y fecha_venta, crea una consulta que muestre las siguientes dos columnas:

* Monto
* El mes y año de la fecha de venta. Esta columna debe llamarse año_mes

| ID_VENTA | MONTO | FECHA_VENTA |
|----------|-------|-------------|
| 1        | 200   | 2010-01-15  |
| 2        | 150   | 2011-02-20  |
| 3        | 300   | 2012-03-10  |
| 4        | 250   | 2013-04-05  |
| 5        | 100   | 2014-05-25  |
| 6        | 350   | 2015-06-18  |
| 7        | 400   | 2015-07-22  |
| 8        | 180   | 2015-08-09  |
| 9        | 220   | 2018-09-30  |
| 10       | 275   | 2019-10-11  |

```
select monto, strftime('%Y-%m', fecha_venta) as año_mes from ventas
```

### Extracciones y where

Previamente aprendimos a filtrar utilizando como parámetro una fecha. Ahora utilizaremos lo aprendido para filtrar fechas de un año o mes en específico.

Se tiene la tabla ventas con la siguiente información:

| ID_VENTA | MONTO | FECHA_VENTA |
|----------|-------|-------------|
| 1        | 200   | 2010-01-15  |
| 2        | 150   | 2011-02-20  |
| 3        | 300   | 2012-03-10  |
| 4        | 250   | 2013-04-05  |
| 5        | 100   | 2014-05-25  |
| 6        | 350   | 2015-06-18  |
| 7        | 400   | 2015-07-22  |
| 8        | 180   | 2015-08-09  |
| 9        | 220   | 2018-09-30  |
| 10       | 275   | 2019-10-11  |

Nos piden mostrar todas las ventas del año 2012. Para esto utilizaremos la función strftime para extraer el año de las fechas, y luego filtraremos por el año indicado:

```
SELECT * FROM ventas WHERE strftime('%Y', fecha_venta) = '2012';
```

Ejercicio
Dada una tabla ventas con las columnas monto y fecha_venta, selecciona toda la información de las ventas del 2015

```
select * from ventas where strftime('%Y', fecha_venta) = '2015'
```