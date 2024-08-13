## Tema 17: Consultas en multiples tablas
:arrow_up: [ir al inicio](./README.md#tabla-de-contenidos)

Cuando trabajamos con bases de datos relacionales, surge con frecuencia la necesidad de combinar datos de varias tablas:

Veamos un ejemplo:

Tabla usuarios:
| EMAIL1                     | NOMBRE         | EDAD |
|----------------------------|----------------|------|
| juan.perez@example.com     | Juan Pérez     | 30   |
| maria.gonzalez@example.com | Maria González | 25   |
| john.doe@example.com       | John Doe       | 40   |
| test.user@example.com      | Test User      | 22   |

Tablas datos_contacto
| EMAIL2                     | TELÉFONO     |
|----------------------------|--------------|
| juan.perez@example.com     | 555-123-4567 |
| maria.gonzalez@example.com | 444-987-6543 |
| john.doe@example.com       | 777-555-8888 |
| test.user@example.com      | 111-222-3333 |
| juan.perez@example.com     | 999-888-7777 |
| maria.gonzalez@example.com | 333-111-0000 |

Si nos piden obtener todos los email, nombre, edad y telefono de todos los usuarios, tendriamos que unir estas tablas . PAra esto existe la clausula `JOIN`

En nuestro ejemplo, podemos unir las tablas con la siguiente consulta
```sql
SELECT *
FROM USUARIOS
JOIN datos_contacto
ON email1 = email2
```

Para unir tablas tenemos que establecer un punto de union. En este caso, lo que tienen en comun ambas tablas es el email.

Ejercicio:

Utilizando lo aprendido, selecciona todos los usuarios junto a sus notas. Observa los resultados antes de avanzar.

Tabla Usuarios:

| EMAIL1                     | NOMBRE         | EDAD |
|----------------------------|----------------|------|
| juan.perez@example.com     | Juan Pérez     | 30   |
| maria.gonzalez@example.com | Maria González | 25   |
| john.doe@example.com       | John Doe       | 40   |
| test.user@example.com      | Test User      | 22   |

Tabla Notas:
| EMAIL2                     | NOTAS |
|----------------------------|-------|
| juan.perez@example.com     | 90    |
| maria.gonzalez@example.com | 100   |
| john.doe@example.com       | 80    |
| test.user@example.com      | 0     |
| juan.perez@example.com     | 100   |
| maria.gonzalez@example.com | 100   |

```sql
SELECT  *
FROM USUARIOS
JOIN NOTAS ON EMAIL1 = EMAIL2
```

## Multiples tablas: utilizando atributo del mismo nombre

En el ejercicio anterior teniamos los atributos emain1 y email2. En este ejercicio aprenderemos que es posible que dos atributos distinyos compartan el mismo nombre, siempre y cuando esten ubicados en diferentes tablas.

Para emeplificar este ejercicio, utilizaremos el nombre email en ambas tablas.

Tabla Usuarios:
| EMAIL                      | NOMBRE         | EDAD |
|----------------------------|----------------|------|
| juan.perez@example.com     | Juan Pérez     | 30   |
| maria.gonzalez@example.com | Maria González | 25   |
| john.doe@example.com       | John Doe       | 40   |
| test.user@example.com      | Test User      | 22   |

Tabla datos_contacto

| EMAIL                      | TELÉFONO     |
|----------------------------|--------------|
| juan.perez@example.com     | 555-123-4567 |
| maria.gonzalez@example.com | 444-987-6543 |
| john.doe@example.com       | 777-555-8888 |
| test.user@example.com      | 111-222-3333 |
| juan.perez@example.com     | 999-888-7777 |
| maria.gonzalez@example.com | 333-111-0000 |


Uniremos los datos de ambas tablas utilizando `JOIN` pero en esta ocasion cuando especifiquemos el punto de union, utilizaremos el nombre de la tabla junto con el del atributo

```sql
SELECT *
FROM USUARIOS
JOIN DATOS_CONTACTO ON USUARIOS.EMAIL = DATOS_CONTACTO.EMAIL
```

Al hacerlo de esta forma, SQL puede entender a cual email nos referimos en cada situacion.

Ejercicio:

Utilizando lo aprendido, selecciona todos los usuarios junto a sus notas. Recuerda que para especificar la clave de union debes utilizar el nombre de la tabla para evitar ambiguedad. Observa los resultados antes de avanzar:

Tabla Usuarios:

| EMAIL                      | NOMBRE         | EDAD |
|----------------------------|----------------|------|
| juan.perez@example.com     | Juan Pérez     | 30   |
| maria.gonzalez@example.com | Maria González | 25   |
| john.doe@example.com       | John Doe       | 40   |
| test.user@example.com      | Test User      | 22   |

Tabla Notas:
| EMAIL                      | NOTAS |
|----------------------------|-------|
| juan.perez@example.com     | 90    |
| maria.gonzalez@example.com | 100   |
| john.doe@example.com       | 80    |
| test.user@example.com      | 0     |
| juan.perez@example.com     | 100   |
| maria.gonzalez@example.com | 100   |

```sql
SELECT  *
FROM USUARIOS
JOIN NOTAS ON USUARIOS.EMAIL = NOTAS.EMAIL
```

Resultado:

| EMAIL                      | NOMBRE         | EDAD | EMAIL                      | NOTAS |
|----------------------------|----------------|------|----------------------------|-------|
| juan.perez@example.com     | Juan Pérez     | 30   | juan.perez@example.com     | 90    |
| maria.gonzalez@example.com | Maria González | 25   | maria.gonzalez@example.com | 100   |
| john.doe@example.com       | John Doe       | 40   | john.doe@example.com       | 80    |
| test.user@example.com      | Test User      | 22   | test.user@example.com      | 0     |
| juan.perez@example.com     | Juan Pérez     | 30   | juan.perez@example.com     | 100   |
| maria.gonzalez@example.com | Maria González | 25   | maria.gonzalez@example.com | 100   |

### Seleccionando algunos atributos
Si tenemos dos tablas, como la de los ejecicios anteriores

Tabla Usuarios:
| EMAIL                      | NOMBRE         | EDAD |
|----------------------------|----------------|------|
| juan.perez@example.com     | Juan Pérez     | 30   |
| maria.gonzalez@example.com | Maria González | 25   |
| john.doe@example.com       | John Doe       | 40   |
| test.user@example.com      | Test User      | 22   |

Tabla datos_contacto

| EMAIL                      | TELÉFONO     |
|----------------------------|--------------|
| juan.perez@example.com     | 555-123-4567 |
| maria.gonzalez@example.com | 444-987-6543 |
| john.doe@example.com       | 777-555-8888 |
| test.user@example.com      | 111-222-3333 |
| juan.perez@example.com     | 999-888-7777 |
| maria.gonzalez@example.com | 333-111-0000 |


Puede ser que al seleccionar los datos no deseemos mostrar los  emails dos veces. Para esto, en lugar de utilizar `SELECT *` utilizaremos

```sql
SELECT USUARIOS.*, DATOS_CONTACTO.TELEFONO
FROM USUARIOS
JOIN DATOS_CONTACTO ON USUARIOS.EMAIL = DATOS_CONTACTO.EMAIL
```

De esta forma, seleccionamos todo lo de la tabla usuarios y solo los telefonos de la tabla datos_contacto

Ejercicio:

Dada la siguiente tabla:

Tabla Usuarios:

| EMAIL                      | NOMBRE         | EDAD |
|----------------------------|----------------|------|
| juan.perez@example.com     | Juan Pérez     | 30   |
| maria.gonzalez@example.com | Maria González | 25   |
| john.doe@example.com       | John Doe       | 40   |
| test.user@example.com      | Test User      | 22   |

Tabla Notas:
| EMAIL                      | NOTAS |
|----------------------------|-------|
| juan.perez@example.com     | 90    |
| maria.gonzalez@example.com | 100   |
| john.doe@example.com       | 80    |
| test.user@example.com      | 0     |
| juan.perez@example.com     | 100   |
| maria.gonzalez@example.com | 100   |

Selecciona de la tabla **usuarios** el email, nombre y edad y de la tabla **notas** sólo las notas. Une los registros de ambas tablas utilizando el email.

```sql
SELECT USUARIOS.*, NOTAS.NOTAS
FROM USUARIOS
JOIN NOTAS ON USUARIOS.EMAIL = NOTAS.EMAIL
```

Resultado:

| EMAIL                      | NOMBRE         | EDAD | NOTAS |
|----------------------------|----------------|------|-------|
| juan.perez@example.com     | Juan Pérez     | 30   | 90    |
| maria.gonzalez@example.com | Maria González | 25   | 100   |
| john.doe@example.com       | John Doe       | 40   | 80    |
| test.user@example.com      | Test User      | 22   | 0     |
| juan.perez@example.com     | Juan Pérez     | 30   | 100   |
| maria.gonzalez@example.com | Maria González | 25   | 100   |

### Join sin resultados
¿Que sucederia si los emails presentes en una tabla no se encuentran en la otra tabla al momento de unir los datos?

Tabla usuarios:

| EMAIL                      | NOMBRE         | EDAD |
|----------------------------|----------------|------|
| juan.perez@example.com     | Juan Pérez     | 30   |
| maria.gonzalez@example.com | Maria González | 25   |
| john.doe@example.com       | John Doe       | 40   |
| test.user@example.com      | Test User      | 22   |

Tabla datos_contacto

| EMAIL                        | TELÉFONO     |
|------------------------------|--------------|
| alvaro.sanchez@example.com   | 555-123-4567 |
| maria.fernandez@example.com  | 444-987-6543 |
| francisca.medina@example.com | 777-555-8888 |

LA respuesta es sencilla, si no hay ningun dato entre ambas tablas, no obtendremos resultados

Utilizando lo aprendido previamente, selecciona todos los registros de la union de las tablas **usuarios** y **datos_contacto**

```sql
SELECT  *
FROM USUARIOS
JOIN DATOS_CONTACTO ON USUARIOS.EMAIL = DATOS_CONTACTO.EMAIL
```

### Orden de Clausulas

Cuando queremos utilizar *joins* con las otras clausulas que hemos aprendido, tenemos que considerar el orden de estas.

En la siguiente tabla se muestra el orden que debemos seguir:

| COMANDO  | SE LEE COMO:                                  |
|----------|-----------------------------------------------|
| SELECT   | Selecciona estos datos.                       |
| FROM     | De esta tabla.                                |
| JOIN     | Únelos con esta tabla.                        |
| WHERE    | Filtra los valores que cumplan tal condición. |
| GROUP BY | Agrupa los resultados por este criterio.      |
| HAVING   | Filtra por estos criterios agrupados.         |
| ORDER BY | Ordena los resultados por este otro criterio. |
| LIMIT    | Limita los resultados a esta cantidad.        |

Ejercicio:

Dada las siguientes tablas, selecciona toda la informacion del usuario **juan.perez@example.com**

Tabla usuarios:

| EMAIL                      | NOMBRE         | EDAD |
|----------------------------|----------------|------|
| juan.perez@example.com     | Juan Pérez     | 30   |
| maria.gonzalez@example.com | Maria González | 25   |
| john.doe@example.com       | John Doe       | 40   |
| test.user@example.com      | Test User      | 22   |

Tabla notas

| EMAIL                      | NOTAS |
|----------------------------|-------|
| juan.perez@example.com     | 90    |
| maria.gonzalez@example.com | 100   |
| john.doe@example.com       | 80    |
| test.user@example.com      | 0     |
| juan.perez@example.com     | 100   |
| maria.gonzalez@example.com | 100   |

> Pista: debes seleccionar todo, unir las tablas y filtrar por el email respectivo

```sql
SELECT  *
FROM USUARIOS
JOIN NOTAS ON USUARIOS.EMAIL = NOTAS.EMAIL
WHERE USUARIOS.EMAIL =  'juan.perez@example.com'
```

Resultado:

| EMAIL                  | NOMBRE     | EDAD | EMAIL                  | NOTAS |
|------------------------|------------|------|------------------------|-------|
| juan.perez@example.com | Juan Pérez | 30   | juan.perez@example.com | 90    |
| juan.perez@example.com | Juan Pérez | 30   | juan.perez@example.com | 100   |

### Agrupar por multiples columnas
Al igual que en las consultas sobre una tabla, podemos utilizar funciones de agregacion y agrupando en consultas sobre multiples tablas.

Supongamos qye teeos dos tablas, una tabla llamada **Clientes** que almacena informacon soibre los clientes y otra llamada Pedidos que almacena informacion sobre los pedidos realizados por esos clientes. Queremos realizar una consulta que nos muestre la cantidad total de pedidos realizados por cada cliente. Para esto ejecutaremos una consulta que utilice la clausula `GROUP BY` para agrupar los pedidos por cliente y contaremos la cantidad total de pedidos para cada cliente

```sql
SELECT c.Nombre AS NombreCliente, COUNT(p.PedidoID) AS TotalPedidos
FROM Clientes c
JOIN Pedidos p on c.ClienteID = p.ClienteID
GROUP BY c.ClienteID
```

Ejercicio:

Tenemos dos tablas, **productos** y **ventas**. Realiza una consulta que nos muestre el producto mas vendido y la cantidad total de unidades vendidas de ese producto. La columna que muestre el total de unidades vendidas debe llamarse **total_vendido**

> Pista: recuerda el uso de ORDER BY y LIMIT

Tabla Productos:

| NOMBRE     | PRECIO | PRODUCTOID |
|------------|--------|------------|
| Producto A | 10     | 1          |
| Producto B | 15     | 2          |
| Producto C | 20     | 3          |

Tabla Ventas:

| CANTIDAD | FECHAVENTA   | PRODUCTOID |
|----------|--------------|------------|
| 20       | '2023-09-01' | 1          |
| 15       | '2023-09-02' | 1          |
| 10       | '2023-09-03' | 2          |
| 25       | '2023-09-04' | 3          |
| 30       | '2023-09-05' | 3          |

```sql
SELECT P.NOMBRE AS NOMBRE,  SUM(V.CANTIDAD)  AS TOTAL_VENDIDO
FROM PRODUCTOS P
JOIN VENTAS V ON P.PRODUCTOID = V.PRODUCTOID
GROUP  BY P.PRODUCTOID
ORDER  BY  2  DESC
LIMIT  1
```

Resultado:

|Nombre| TOTAL_VENDIDO  |
|--|--|
| PRODUCTO C | 55 |