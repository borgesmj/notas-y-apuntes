
# Aprendiendo SQL
Notas tomadas del [**curso interactivo de Desafío LATAM**](https://sqlinteractivo.desafiolatam.com/cursos/1) e información tomada de [roadmap.sh](https://roadmap.sh/sql)

Este contenido estará estructurado acorde al contenido de Desafío LATAM y se refuerza con la información del roadmap.sh

> Nota rápida: siempre tener en cuenta el [orden de las clausulas](./#orden-de-clausulas)


## Tabla de contenidos

| DIA                           | Enlace                                  |
|-------------------------------|-----------------------------------------|
| Tema 1: Conceptos básicos      | [ir](./01-Introduccion.md)           |
| Tema 2: Seleccionando filas     | [ir](./02-seleccionando-filas.md)    |
| Tema 3: Ordenando Resultados   | [ir](./03-ordenando-resultados.md)   |
| Tema 4: Limit                  | [ir](./04-Limit.md)                  |
| Tema 5: Operaciones con string | [ir](./05-operaciones-con-string.md) |
| Tema 6: Operaciones con fechas | [ir](./06-operaciones-con-fechas.md) |
| Tema 7: Funciones de agregacion | [ir](./07-Funciones-de-agregacion.md) |
| Tema 8: Distinct | [ir](./08-distinct.md) |
| Tema 9: Introducción a grupos | [ir](./09-introduccion-a-grupos.md) |
| Tema 10: HAVING | [ir](./10-having.md) |
| Tema 11: Subconsultas | [ir](./11-subconsultas.md) |
| Tema 12: Combinacion de consultas | [ir](./12-combinacion-de-consultas.md) |
| Tema 13: Insercion de registros | [ir](./13-insercion-de-registros.md) |
| Tema 14: Borrado y modificación de registros | [ir](./14-borrado-y-modificacion-de-registros.md) |
| Tema 15: Tablas | [ir](./15-tablas.md) |
| Tema 16: Restricciones | [ir](./16-restricciones.md) |
| Tema 17: Consultas en multiples tablas | [ir](./17-consultas-en-multiples-tablas.md) |
| Tema 18: Tipos de join | [ir](./18-tipos-de-join.md) |
| Tema 19: Cardinalidad | [ir](./19-cardinalidad.md)
| Operadores | [ir](.#operadores) |

## Operadores:

:arrow_up: [ir al inicio](.#tabla-de-contenidos)

### Operadores aritmeticos:
* `+`: Adicion
* `-`: Subtraccion
* `*`: Multiplicacion
* `/`: Division
* `%`: Módulo 

Ejemplo:
```sql
SELECT product, price, (price *0.18) as tax
FROM products;
```

### Operadores de comparacion
* `=`: igual que
* `!=` o `<>`: no igual que
* `>`: mayor que
* `<`: menos que
* `>=`: mayor o igual que
* `<=`: menor o igual que

Ejemplo:
```sql
SELECT name, age
FROM students
WHERE age > 18;
```

### Operadores lógicos
* `AND`: retorna verdadero si ambas condiciones son verdaderas
* `OR`: retorna verdadero si alguna de las soa condiciones es veradera
* `NOT`: retorna el booleano opuesto de una condicion

Ejemplo:

```sql
SELECT *
FROM employees
WHERE salary > 50000 AND age < 30
```

### Operadores bit a bit
* `&`: AND
* `|`: OR
* `^`: XOR

Los operadores bit a bit son mucho menos usados en SQL que los demas operadores




