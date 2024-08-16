# Divertido, ¿eh? Divertido, ¿cómo?


## Dad Jokes

La API que vamos a utilizar hoy es la impresionante [icanhazdadjoke](https://icanhazdadjoke.com/api). Echa un vistazo a la documentación de la API antes de continuar. Mira el **endpoint** para ver la URL a la que acceder y el formato de los datos que obtendremos de vuelta.

👉 Aquí está el código para obtener un chiste de papá al azar y la salida.
**NOTA** - El segundo argumento (`headers=`) en `requests.get()` es realmente importante. Le dice al código que no queremos el sitio web de vuelta, queremos datos JSON en un formato específico. A veces es necesario hacer eso.


```python
import requests, json

result = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"}) # get a random dad joke from the site endpoint and assign to a variable. The second argument (the header request) tells the script to return the json data as a string.

joke = result.json()
print(json.dumps(joke, indent=2))
```
:point_right: Puedo cambiar la sentencia print para que sólo muestre el chiste en lugar de todo el diccionario.
```python
print(joke["joke"])
```

### La API de este sitio es muy buena para aprender, ya que da un montón de buenos ejemplos de cómo importar chistes en diferentes formatos.


# 👉 Desafío del día 91

El reto de hoy es construir un programa a partir de este principio básico que:

1. Te regale un chiste al azar.
2. Pregunte si quieres guardarlo.
3. Si lo haces, debería:
    1. Guardar el número de identificación de la broma en replit db
4. Preguntar al usuario si desea ver los chistes guardados y mostrar el contenido de la base de datos.

Ejemplo:

![](recursos/chiste.png)

<detalles> <sumario> 💡 Consejos </sumario>

- Consulta los ejemplos de *fetching a specific joke* en la [icanhazdadjoke API](https://icanhazdadjoke.com/api#:~:text=Fetch%20a%20dad-,joke,-GET%20https%3A//icanhazdadjoke).

</detalles>