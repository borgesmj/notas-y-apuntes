## Tema 7: Funciones de agregacion
:arrow_up: [ir al inicio](./README.md#tabla-de-contenidos)

### El mayor valor de una columna
En SQL hay funciones que nos permiten ejecutar operaciones sobre un conjunto de resultados. Estas reciben el nombre de **funciones de agregacion**

En este ejercicio trabajaremos con la funcion `MAX()` la cual nos permite encontrar el valor mas alto del campo que especifiquemos.
Se puede utiizar para tipos de datos de columnas numericos, caracteres y fecha. Si hay valores nulos, no son tomados para comparacion.

Sintaxis
```
SELECT MAX(column_name)
FROM table_name
where condition;
```

Por ejemplo:

Se tiene una tabla llamada empleados con los siguientes datos:

| EMAIL                   | NOMBRE         | EDAD | SUELDO |
|-------------------------|----------------|------|--------|
| juan.perez@workmail.com | Juan Pérez     | 30   | 50,000 |
| maria.gonzalez@corp.com | Maria González | 25   | 55,000 |
| john.doe@techplace.org  | John Doe       | 40   | 60,000 |
| francisco@startup.io    | Francisco      | 22   | 45,000 |

Podemos encointrar el salario mas alto utilizando:

```
SELECT MAX(salario) FROM empleados
```

> Cuando usamos funciones de agregacion, no podemos seleccionar directamente otros elementos de la misma tabla. Por ejemplo, `SELECT email, MAX(salario) FROM empleados;` arrojaria un error ya que estariamos selecionando email junto a la funcion. Pero no te preocupes, ya que aprenderemos como hacerlo apropiadamente cuando veamos la clausula _group by_ mas adelante

Ejercicio:
Utilizando los mismos datos previos selecciona la mayor edad de la tabla empleados

Tip: Aunque en SQL es válido escribir tanto MAX (columna) como MAX(columna), el corrector de ejercicios considerará la primera opción como incorrecta debido al espacio adicional. Por lo tanto, escribe la función sin espacios.

```
select max(edad)
from empleados
```

### El menor valor de una columna
`MIN` es una funcion agregada que se usa para retornar el valor mas pequeño en una columna seleccionada. 


Ejercicio
Utilizando la tabla empleados, encuentra el menor sueldo presente.

| EMAIL                   | NOMBRE         | EDAD | SUELDO |
|-------------------------|----------------|------|--------|
| juan.perez@workmail.com | Juan Pérez     | 30   | 50,000 |
| maria.gonzalez@corp.com | Maria González | 25   | 55,000 |
| john.doe@techplace.org  | John Doe       | 40   | 60,000 |
| francisco@startup.io    | Francisco      | 22   | 45,000 |

```
SELECT MIN(sueldo)
FROM empleados
```

### Suma de elementos de una columna
Hasta el momento hemos estutemado dos funciones de agregacion:
* MAX()
* MIN()

En este ejercicio introduciremos la funcion de agregacion `SUM()`.
LA funcion `SUM()` en SQL es usada para calcular la suma de una columna. Esta funcion nos permite sumar una columna de numeros en una tabla SQL.

La sintaxis de `SUM()` es:

```
SELECT SUM(column_name) FROM table_name
```

> Es importante tener en cuenta que la colunma donde se aplique `SUM()` debe tener solo valores numericos, de lo contrario, la consulta puede generar error o un resultado inesperado.


Ejercicio:

Utilizando la tabla empleados, encuentra la suma de todos los sueldos.

| EMAIL                   | NOMBRE         | EDAD | SUELDO |
|-------------------------|----------------|------|--------|
| juan.perez@workmail.com | Juan Pérez     | 30   | 50,000 |
| maria.gonzalez@corp.com | Maria González | 25   | 55,000 |
| john.doe@techplace.org  | John Doe       | 40   | 60,000 |
| francisco@startup.io    | Francisco      | 22   | 45,000 |


```
select sum(sueldo) from empleados
```

### Promedipo de una columna
La funcion en SQL `AVG()` es una funcion de agregacion, que retorna el valor promedio de una columna numerica. Esta funcion calcula la suma de valores en una columna y lo divide por el conteo de esos valores.

Ejercicio
Utilizando la tabla empleados, encuentra el promedio de todos los sueldos.

| EMAIL                   | NOMBRE         | EDAD | SUELDO |
|-------------------------|----------------|------|--------|
| juan.perez@workmail.com | Juan Pérez     | 30   | 50,000 |
| maria.gonzalez@corp.com | Maria González | 25   | 55,000 |
| john.doe@techplace.org  | John Doe       | 40   | 60,000 |
| francisco@startup.io    | Francisco      | 22   | 45,000 |


```
select AVG(sueldo) from empleados
```

### Contando elementos en una tabla

`COUNT()` es una funcion en SQL que retorna el numero de filas que coincide con un criterio especifico. Esencialmente la funcion `COUNT()` es usado para cuando necesitamos saber el recuento de un registro en la columna de determinada tabla.

Hay dos tipos de funciones COUNT: `COUNT(*)` y `COUNT(column)`

Ejercicio:
Encuentra la cantidad de registros (cantidad de filas) que tiene la tabla empleados.

| EMAIL                   | NOMBRE         | EDAD | SUELDO |
|-------------------------|----------------|------|--------|
| juan.perez@workmail.com | Juan Pérez     | 30   | 50,000 |
| maria.gonzalez@corp.com | Maria González | 25   | 55,000 |
| john.doe@techplace.org  | John Doe       | 40   | 60,000 |
| francisco@startup.io    | Francisco      | 22   | 45,000 |

```
select count(*) from empleados
```

### Ejercicio 1: Funciones de agregacion con where

Las funciones de agregación se pueden combinar con las claúsulas previamente estutemadas. Simplemente tenemos que respetar el orden establecido de las claúsulas.

A la hora de extraer datos de base de datos será muy común que utilicemos las funciones de agregación en conjunto con where.

```
SELECT AVG(columna1) FROM tabla WHERE columna2 < valor
```

Ejercicio
Utilizando la tabla empleados, calcula la suma de sueldos de todas las personas mayores a 27 años

| EMAIL                   | NOMBRE         | EDAD | SUELDO |
|-------------------------|----------------|------|--------|
| juan.perez@workmail.com | Juan Pérez     | 30   | 50,000 |
| maria.gonzalez@corp.com | Maria González | 25   | 55,000 |
| john.doe@techplace.org  | John Doe       | 40   | 60,000 |
| francisco@startup.io    | Francisco      | 22   | 45,000 |


```
select SUM(sueldo) from empleados where edad > 27
```

### Ejercicio 2: Funciones de agregacion con Where
Ejercicio
Utilizando la tabla empleados, calcula el promedio de los sueldos de todas las personas que ganan más de 50,000

| EMAIL                   | NOMBRE         | EDAD | SUELDO |
|-------------------------|----------------|------|--------|
| juan.perez@workmail.com | Juan Pérez     | 30   | 50,000 |
| maria.gonzalez@corp.com | Maria González | 25   | 55,000 |
| john.doe@techplace.org  | John Doe       | 40   | 60,000 |
| francisco@startup.io    | Francisco      | 22   | 45,000 |


```
select AVG(sueldo) from empleados where sueldo > 50000
```
### Ejercicio 3: Funciones de agregacion con where

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


Calcula cuantas personas trabajan en el area de marketing

```
select count(*) from empleados where departamento = 'Marketing'
```

### Ejercicio 4: Funciones de agregacion con where

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

Calcula cuantas personas trabajan en total en las areas de finanzas y marketing

```
select count(*) from empleados where departamento = "Marketing" or departamento = "Finanzas"
```
### Conteo de condiciones con string

Ejercicio
Se tiene la tabla usuarios con la siguiente información:

| ID | NOMBRE | APELLIDO | EMAIL                    | TELEFONO |
|----|--------|----------|--------------------------|----------|
| 1  | Juan   | Pérez    | juanperez@gmail.com      | 555-1234 |
| 2  | María  | García   | mariagarcia@hotmail.com  | 555-5678 |
| 3  | Pedro  | López    | pedrolopez@yahoo.com     | 555-9876 |
| 4  | Lucía  | Sánchez  | luciasanchez@outlook.com | 555-5555 |
| 5  | Jorge  | Martínez | jorgemartinez@gmail.com  | 555-4321 |

Cuenta la cantidad de usuarios cuyo nombre termina con la letra 'a' en la tabla de usuarios.

```
select count(*) from usuarios where nombre like '%a' 
```