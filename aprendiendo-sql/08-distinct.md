## Tema 8: Distinct

:arrow_up: [ir al inicio](./README.md#tabla-de-contenidos)

### Seleccionar filtrando datos repetidos

En SQL la palabra clave `DISTINCT` nos permite filtrar los resultados repetidos de una consulta

Supongamos que tenemos la siguiente tabla llamada _colores_

| COLOR    |
|----------|
| Rojo     |
| Azul     |
| Verde    |
| Amarillo |
| Rojo     |
| Verde    |
| Rojo     |
| Verde    |
| Rojo     |
| Negro    |
| Blanco   |
| Rojo     |
| Azul     |
| Verde    |
| Amarillo |

Nos piden crear una conculta que nos muestre cada color una unica vez, para esto utilizamos el siguiente comando:

```
SELECT DISTINCT color AS color_unico
FROM colores
```

Ejercicio
Prueba en el editor la misma instrucción aprendida para ver cual sería el resultado de la consulta.

### Seleccionando correor unicos

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

Crea una consulta que nos muestre cada correo una única vez. La columa mostrada debe llamarse correo_unico

```
select distinct(correo) as correo_unico from usuarios
```

### Seleccionar distintos años

Se tiene la tabla _ventas_ con la sigguiente informaicon:

| ID_VENTA | MONTO | FECHA_VENTA |
|----------|-------|-------------|
| 1        | 200   | 2010-01-15  |
| 2        | 150   | 2011-02-20  |
| 3        | 300   | 2012-04-10  |
| 4        | 250   | 2013-04-05  |
| 5        | 100   | 2014-04-25  |
| 6        | 350   | 2015-06-18  |
| 7        | 400   | 2015-06-22  |
| 8        | 180   | 2015-06-09  |
| 9        | 220   | 2018-07-30  |
| 10       | 275   | 2019-07-11  |

Se nos ha solicitado crear una consulta que muestre los años en los que se han realizado transacciones, excluyendo repeticiones.
Como ya sabemos, [en ejercicios anteriores](.#extraccion-del-año), para obtener el año a partir de la feha de venta,podemos utilizar el siguiente codigo:


```
select strftime('%Y', fecha_venta) as año_venta from ventas
```

Sin embargo, para asegurarnos de obtener años unicos podemos agregar la clausula DISTINCT a nuestra consulta de la siguiente manera:

```
SELECT DISTINCT strftime('%Y', fecha_venta) as año_unico from ventas
```

Ejercicio: Utilizando la tabla ventas, previamente utilizada, selecciona todos los meses distintos, asignamdole a la columna el alias "mes_unico".

```
select distinct strftime('%m', fecha_venta) as mes_unico
from ventas
```

### Contar los valores distintos
Si queremos contar los valores distintos en una columna de una tabla, podemos combinar las funciones COUNT y DISTINCT de la siguiente manera `COUNT(DISTINCT columna)`

Veamos un ejemplo con la siguiente tabla empleados:

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

Podemos contar la cantidad de depetamentos unicos de la empresa con

```
SELECT COUNT(DISTINCT Departamento) FROM Empleados:
```

Ejercicio:

Se tiene la tabla usuarios con la siguiente informacion:

| ID | NOMBRE | APELLIDO | EMAIL                    | TELEFONO |
|----|--------|----------|--------------------------|----------|
| 1  | Juan   | Pérez    | juanperez@gmail.com      | 555-1234 |
| 2  | María  | García   | mariagarcia@hotmail.com  | 555-5678 |
| 3  | Pedro  | López    | pedrolopez@yahoo.com     | 555-5678 |
| 4  | Lucía  | Sánchez  | luciasanchez@outlook.com | 555-5555 |
| 5  | Jorge  | Martínez | jorgemartinez@gmail.com  | 555-5678 |


Crea una consulta que muestre los teléfonos únicos de la tabla. La columna mostrada debe llamarse telefonos_unicos

```
select count(distinct telefono) as telefonos_unicos from usuarios
```

### Contando correos únicos

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

Crea una consulta para contestar cuantos correos únicos existen en la tabla. La columna resultante debe llamarse correos_cant

```
select count(distinct correo) as correos_cant from usuarios
```

### Distinct con multiples columnas
Podemos usar DISTINCT con más de una columna para obtener combinaciones únicas de esas columnas. Supongamos que tienes una tabla llamada empleados con las columnas departamento y puesto.

Para este ejemplo trabajaremos con la siguiente tabla empleados:

| ID_EMPLEADO | NOMBRE    | DEPARTAMENTO | PUESTO        |
|-------------|-----------|--------------|---------------|
| 1           | Juan      | Ventas       | Vendedor      |
| 2           | María     | Ventas       | Vendedor      |
| 3           | Carlos    | IT           | Desarrollador |
| 4           | Ana       | IT           | Desarrollador |
| 5           | Luis      | Ventas       | Gerente       |
| 6           | Carmen    | IT           | Gerente       |
| 7           | José      | IT           | Desarrollador |
| 8           | Francisco | Ventas       | Vendedor      |

uego podemos obtener todas las combinaciones únicas de Departamento y Puesto utilizando la siguiente consulta:

```
SELECT DISTINCT departamento, puesto FROM empleados;
```

Con esto obtendremos la siguiente tabla resultante.

| DEPARTAMENTO | PUESTO        |
|--------------|---------------|
| Ventas       | Vendedor      |
| IT           | Desarrollador |
| Ventas       | Gerente       |
| IT           | Gerente       |

Ejercicio
Para la siguiente tabla "productos" deseamos obtener todas las combinaciones únicas de "Categoria" y "Precio"

| NOMBRE      | CATEGORIA   | PRECIO |
|-------------|-------------|--------|
| Laptop      | Electrónica | 1000   |
| Teléfono    | Electrónica | 500    |
| Camiseta    | Ropa        | 20     |
| Pantalón    | Ropa        | 40     |
| Auriculares | Electrónica | 50     |
| Libro       | Libros      | 15     |
| Mochila     | Accesorios  | 30     |

```
SELECT DISTINCT categoria, precio
FROM productos
```