# 👉 Desafío del día 86

El reto de hoy consiste en construir un motor de blog totalmente funcional.


1. Crea un sitio web con una 'página de inicio de sesión'.
2. El inicio de sesión debe funcionar sólo para **un** usuario: tú.
3. Si **estás** conectado, verás:
    1. 1. Una lista de los mensajes existentes
    2. 2. Una forma de añadir nuevas entradas (una caja de texto con un botón de enviar.) Enviar añade la entrada a tu blog usando Replit db.
4. Si **no estás conectado**, verás las entradas del blog (las más recientes primero) en una página continua.
5. Esta página de alimentación también tendrá un botón de 'login'.



Ejemplo:

![](recursos/blog.png)



<detalles> <sumario> 💡 Consejos </sumario>

- Puedes usar `reversed` para, bueno, invertir una lista y recorrerla en orden inverso. Así `for key in reversed(keys)`.
- Utilice `.replace()` para sobrescribir los elementos del diccionario: thisEntry = thisEntry.replace("{title}", db[key]["title"])`.
</detalles>

