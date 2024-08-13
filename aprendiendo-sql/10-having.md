## Tema 10: HAVING

:arrow_up: [ir al inicio](./README.md#tabla-de-contenidos)

### Introduccion a `HAVING`
`HAVING` es una clausula de SQL que nos permite filtrar conjuntos de resultados en una clausula `GROUP BY`.  Se utiliza para mencionar condiciones sobre grupos que se seleccionan. En otras palabras, HAVING se utiliza principalmente con la clausula GROUP BY para filtrar los resultados que devuelve un GROUP BY

Es similar a una clausula WHERE,pero opera sobre los resultados de una agrupacion. La clausula WHERE condiciona las columnas, mientras que la clausula HAVING condiciona los grupos creaod por la clausula GROUP BY.

HAVING se emplea para filtrar los resultados de una consulta que involucra funciones agregadas. EN otras palabras, HAVING permite aplicar condiciones de filtrado a los resultados de funciones como COUNT, MIN, MAX, SUM y AVG despues de que se han agrupado los datos con la clausula GROUP BY

Por ejemplo, si tenemos la siguiente tabla de inscripciones:

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

Nos piden crear un reporte mostrando los meses y la cantidad de inscruitos pero solo donde haya 2 o mas inscritos

```
SELECT strftime("%m", Fecha_Inscripcion) as mes, count(fecha_inscripcion) as cantidad_usuarios
FROM inscripciones
GROUP BY strftime("%m", Fecha_Inscripcion)
HAVING cantidad_usuarios > 2
```

En esta consulta, primero utilizamos GROUP BY para agrupar por mes. Luego utilizamos la funcion de COUNT(Fecha_Inscripcion) ára contar la cantidad de inscritps. Despues de haber agrupado los datos y calculado el total de inscritos, aplicamos la clausula HAVING para filtrar los resultados

Ejercicio:
Crea un reporte mostrando los meses y la cantidad de inscritos pero solo donde haya 1 inscrito. Las columnas deben llamarse mes y cantidad_usuarios, respectivamente.

```
SELECT strftime("%m", fecha_inscripcion) as mes, count(fecha_inscripcion) as cantidad_usuarios
FROM inscripciones
GROUP BY 1
HAVING cantidad_usuarios == 1
```

### Buscando duplicados
Uno de los usos mas recurrentes de HAVING es buscar duplicados. POr ejemplo, dada una tabla de correos, ver cuales estan mas de una vez

Ejercicio

Se tiene la tabla correos_corporativos

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

Muestra los correos que aparezcan en mas de una ocasion. LA tabla debe tener dos culumnas, una llamada correo y otra llamada cunta_correos que muestra la cantidad de repeticiones correspondiente a cada correo:

```
SELECT correo, count(correo) as cuenta_correos
FROM correos_corporativos
GROUP BY correo
HAVING cuenta_correos > 1
```

### HAVING y cuenta
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

Crea una consulta que muestre la cantidad de usuarios y el departamento en donde haya mas de un empleado. Las columnas deben llamarse cantidad_de_usuarios y departamento, respectivamente.

```
select count(departamento) AS CANTIDAD_DE_USUARIOS, departamento
FROM empleados
GROUP BY 2
HAVING cantidad_de_usuarios > 1
```

### Having y promedio
Ejercicio
Se tiene la siguiente tabla notas

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

Crea una consulta para determinar cuales son los estutemantes que aprobaron. El criterio de aprobacion es promedio_de_notas >= 50

LAs columnas a mostrar deben ser email y promedio_notas

```
SELECT email, AVG(notas) as promedio_notas
from notas
GROUP BY 1
HAVING promedio_notas >= 50
```

### Having y Order
Una vez qye hemos agrupado datos utilizando la clausula GROUP BY, es comun que necesitemos ordenar estos grupos segun algun criterio especifico. POr lo general, queremos ordenar los grupos en funcion de alguna metrica agregada, como la suma, el conteo, el promedio, etc. Para hacer esto, utilizamos la clausula ORDER BY junto con las funciones de agregacion.

El orden de las clausulas en una sonculta debe ser la siguiente:

```
| ORDEN | CLAUSULA | DESCRIPCIÓN                                                    |
|-------|----------|----------------------------------------------------------------|
| 1     | SELECT   | Especifica las columnas que se deben retornar en el resultado. |
| 2     | FROM     | Especifica las tablas de las cuales se extraerán los datos.    |
| 3     | WHERE    | Filtra registros antes de cualquier agregación o agrupación.   |
| 4     | GROUP BY | Agrupa registros por una o más columnas.                       |
| 5     | HAVING   | Filtra registros después de la agregación.                     |
| 6     | ORDER BY | Ordena los registros retornados por una o más columnas.        |
| 7     | LIMIT    | Limita el número de registros retornados.                      |
```

Ejercicio

Dada la siguiente tabña **ventas** , escribe una consulta SQL para obtener los productos que se han vendido en una cantidad total mayor a 1000, ordenados en orden descendente de cantidad vendida

| PRODUCTO | CANTIDAD |
|----------|----------|
| A        | 500      |
| B        | 2000     |
| C        | 300      |
| D        | 1500     |
| E        | 700      |
| A        | 600      |
| B        | 800      |
| C        | 1200     |
| D        | 400      |
| E        | 300      |

La tabla resultante debe tener dos columnas "producto" y "cantidad_total"

```
SELECT producto, sum(cantidad) as cantidad_total
from ventas
GROUP BY 1
HAVING cantidad_total > 1000
ORDER BY cantidad_total desc
```


### Having y Orden 2
Ejercicio
Supongamos que tiene una tabla de empleados con los siguientes datos:

| ID_EMPLEADO | NOMBRE | DEPARTAMENTO | SALARIO |
|-------------|--------|--------------|---------|
| 1           | Juan   | Ventas       | 3000    |
| 2           | Maria  | Marketing    | 3500    |
| 3           | Carlos | Ventas       | 4000    |
| 4           | Ana    | Marketing    | 2800    |
| 5           | Luis   | Ventas       | 3200    |

Tu tarea es escribir una consulta SQL que regrese los departamentos cuyo salario promedio es mayor a 3000, ordenados de mayor a menor salario promedio. Los resultados deben mostrar el nombre del departamento y el salario promedio, con los nombres de las columnas como departamento y salario_promedio, respectivamente

```
SELECT departamento, AVG(salario) as salario_promedio
FROM empleados
GROUP BY 1
HAVING salario_promedio > 3000
ORDER BY salario_promedio desc
```

RESULTADO

| DEPARTAMENTO | SALARIO_PROMEDIO |
|--------------|------------------|
| Ventas       | 3400             |
| Marketing    | 3150             |
