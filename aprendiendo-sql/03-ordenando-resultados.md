## Tema 3: Ordenando resultados
:arrow_up: [ir al inicio](./README.md)
### Ordenando filas
En este ejercicio aprenderemos a ordenar las filas de una tabla SQL y para estoi estutemaremos una nueva clausula llamada *ORDER BY*
La clasusula *order by* en SQL es usada para ordernar los resultados de una declaracion SELECT in orden ascendente o descendente. El comando ordena por defecto de maera ascendente, siq ueremos ordenar de manera descendente debemos usar la palabra clave `desc`


#### Sintaxis para orden ascendente
```sql
Select column1, column2
from table_name
order by column1, column2, asc
```

#### Sintaxis para orden desscendente
```sql
Select column1, column2
from table_name
order by column1, column2, desc
```

#### Ejercicio:
Ordena los registros de la tabla usuarios por el campo 'nombre'
```sql
select * from usuarios order by nombre
```
### Ordenando filas asc explicito
Ejercicio
En este ejercicio se tiene una tabla usuarios con los campos id, nombre, apellido, email y teléfono. Se te pide ordenar los registros de la tabla 'usuarios' por el campo 'nombre' en orden ascendente.
```sql
select * from usuarios order by nombre asc
```

### Ordenando filas desc
Ejercicio
Se tiene una tabla productos con los campos id, nombre, precio y stock. Selecciona sólo los precios de la tabla 'productos' ordenados de forma descendente.
```sql
select precio from productos order by precio desc
```

### Ordenando filas con valores nulos
Ordena la tabla empleados por la columna 'salario' de manera ascendente.
```sql
select * from empleados order by salario asc
```

### Ordenando con nulos al final
Con NULLS FIRST se muestran los nulos primeros y con NULLS LAST se muestran al final

Ejercicio
Dada una tabla productos con las columnas 'id', 'nombre' y 'precio' con los siguientes registos.

| ID | NOMBRE     | PRECIO |
|----|------------|--------|
| 1  | Producto 1 | 100    |
| 2  | Producto 2 | NULL   |
| 3  | Producto 3 | 50     |
| 4  | Producto 4 | NULL   |
| 5  | Producto 5 | 200    |

Ordena las filas de la tabla en función del precio de forma ascendente. Asegúrate de que las filas con valores nulos en la columna 'precio' aparezcan al final de la lista ordenada.

```sql
select * from productos order by precio asc nulls last
```
### Combinaciones de orden

En algunas situaciones vamos a querer ordenar en función de múltiples columnas. Por ejemplo, si queremos obtener una lista de todos los productos ordenados por su stock y luego por su color, podemos seleccionar todos los campos de la tabla y ordenarlos primero por el campo stock y luego por el campo color de la siguiente manera:

```SELECT * FROM productos ORDER BY stock ASC, color ASC```

Ejercicio
Se tiene la tabla empleados con la siguiente información:

| ID | NOMBRE         | SALARIO |
|----|----------------|---------|
| 1  | Juan Pérez     | 4800    |
| 2  | María López    | 5500    |
| 3  | Pedro García   | 5500    |
| 4  | Ana Martínez   | 5500    |
| 5  | Luis Rodríguez | 4800    |

Selecciona una lista de todos los empleados ordenados por su salario y por su nombre.
```sql
select * from empleados order by salario asc, nombre asc
```

### Combinaciones de orden asc y desc
Se tiene la tabla productos con la siguiente información:

| ID | NOMBRE     | STOCK | COLOR  |
|----|------------|-------|--------|
| 1  | Silla      | 10    | Rojo   |
| 2  | Mesa       | 5     | Verde  |
| 3  | Lámpara    | 15    | Azul   |
| 4  | Escritorio | 8     | Blanco |
| 5  | Estantería | 12    | Negro  |

Selecciona todos los registros de la tabla 'productos' y ordénalos primero por 'stock' de forma descendente y luego por 'color' de forma ascendente.
```
select * from productos order by stock desc, color asc
```
