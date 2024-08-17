# 👉 Desafío del día 92

El reto de hoy consiste en crear tu propia app del tiempo.

👉 Para empezar, hemos encontrado una API meteorológica gratuita, así que aquí tienes el código de inicio para ello.  Todo lo que necesitas hacer es personalizar tu zona horaria, longitud y latitud.  Este código obtiene la temperatura máxima y mínima y el código meteorológico.

```python
import requests, json
timezone = "GMT"
latitude = 51.5002
longitude = -0.1262

result = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone={timezone.upper()}")

user = result.json()
print(json.dumps(user, indent=2))
```
Tu aplicación meteorológica debería

1. Obtener el tiempo de tu zona.
2. Obtener la previsión para hoy. Debería mostrar (de forma realmente agradable):
    1. La versión de texto de lo que significa el código meteorológico.
    2. Temperaturas máxima y mínima.

Ejemplo:
![alt text](<Sin título-1.png>)

<detalles> <sumario> 💡 Consejos </sumario>

- Obtener la longitud & latitud de su ciudad más cercana.
- Smash a cabo una masiva `si ... elif ... else` declaración de selección.
- Utiliza operadores booleanos (and, or, not) para comprobar si hay más de un código meteorológico en el mismo `elif`, por ejemplo: `elif code==1 or code==2 or code==3:`.

</detalles>

Traducción realizada con la versión gratuita del traductor DeepL.com