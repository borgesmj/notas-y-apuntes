## Tema 4: Limit
:arrow_up: [ir al inicio](./README.md#tabla-de-contenidos)
### Limitando la cantidad de resultados
La cláusula LIMIT se utiliza para limitar la cantidad de resultados devueltos por una consulta. Esto es útil cuando sólo necesitamos ver una cierta cantidad de registros en lugar de todos los registros que cumplan con la condición de la consulta.

Por ejemplo, si queremos obtener sólo los primeros 5 registros de una tabla, podemos usar la cláusula LIMIT de la siguiente manera:

```
SELECT * FROM tabla LIMIT 5
```

La clausula LIMIT se agrega al final de la consulta.

Ejercicio:

Selecciona los primeros 3 usuarios de la tabla de usuarios.

```
select * from usuarios limit 3
```

### Obtener los primeros alumnos con mejor nota
En SQL, la combinación de las cláusulas ORDER BY y LIMIT nos permite obtener el valor o valores máximos de una columna en una tabla. 

Una vez que hemos ordenado los registros, podemos utilizr la clausula LIMIT para limiatr la cantidad de resultados obtenidos, por ejemplo:

```
Select * from notas order by nota desc limit 3
```

Que corresponde a los tres mejores alumnos de la tabla notas

Ejercicio:

Se tiene una tabla de puntajes con las columnas id y puntaje. Utiliza lo aprendido para obtener el puntaje más alto de la tabla utilizando ORDER BY y LIMIT

```
select puntaje from puntajes order by puntaje desc limit 1
```

### Obtener el nombre del concierto con más entradas vendidas

Se tiene una base de datos con la tabla conciertos en la cual se almacena información sobre cada concierto, incluyendo el nombre del concierto y la cantidad de entradas vendidas. Los datos dentro de la base de datos corresponden a la siguiente tabla.

| NOMBRE_CONCIERTO | ENTRADAS_VENDIDAS |
|------------------|-------------------|
| Concierto A      | 150               |
| Concierto B      | 200               |
| Concierto C      | 180               |
| Concierto D      | 250               |

Encuentra el nombre del concierto que ha vendido la mayor cantidad de entradas (utiliza ORDER BY y LIMIT).

```
SELECT nombre_concierto, entradas_vendidas 
FROM conciertos 
ORDER BY entradas_vendidas DESC 
LIMIT 1
```