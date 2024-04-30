# Autenticación

El código eficiente a menudo tiene el inconveniente de ser muy difícil de entender al principio.  A menudo es muy denso, con muchas cosas sucediendo en una sola línea de código.

Por eso los profesores suelen enseñar lo que podría describirse como "el camino más largo" cuando diseñan lecciones sobre temas nuevos. 

Con todo esto en mente, no te enfades con nosotros cuando te digamos que *hay una manera más fácil* de crear un sistema de login que usando sesiones.  Has pasado los últimos días aprendiendo a fondo lo que ocurre entre bastidores, que era de lo que se trataba. No, de verdad. Lo prometemos. 



## Autenticación Replit

En Replit sabemos que probablemente utilizarás la autenticación **muchas veces**. Así que hemos horneado en la característica para usted.

👉 Ejecuta tu código, luego dirígete a tu panel de archivos de la izquierda y desplázate hasta que veas *autenticación*. Luego, actívalo.  Ya está.

![](resources/01_login1.png)

Ahora verás que tu repl utiliza la página de inicio de sesión Replit por defecto.
![](resources/01_login2.png)

También puedo acceder a un montón de información sobre el usuario almacenada en el panel de autenticación. 

Para ello voy a importar `request`, y luego usar `username = request.headers["X-Replit-User-Name"]` para asignar el nombre de usuario a una variable.  Obtuve el código `X-Replit-User-Name` del panel de autenticación.

Aquí está el código completo:

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
  username = request.headers["X-Replit-User-Name"]
  return f"Hello {username}"

app.run(host='0.0.0.0', port=81)
```
## ¡Pruébalo!

# 👉 Desafío del día 87

El reto de hoy es editar su página de inicio de sesión para el sistema de motor de blog de ayer. Usted debe terminar con significativamente menos código que tenías antes.

Su programa debe:

1. Cambiar el botón de inicio de sesión para reenviar al usuario a la página de edición.
2. En la página de edición, comprueba que eres tú. Si no lo eres, devuelve al usuario a la página principal.
    
Ejemplo:

![](resources/authenticate.png)

<detalles> <sumario> 💡 Consejos </sumario>

No mucho aquí hoy amigos. Es una simplificación de su sistema exitiing utilizando las técnicas del tutorial.
</detalles>
