# 👉 Desafío del día 72

Ahora que conocemos las contraseñas seguras, podemos proteger *realmente* nuestro programa de diario.

Retrocede 10 días y coge el código de tu agenda del Día 62.

Cuando lo tengas, añade las siguientes características:

1. La **primera** vez que se ejecuta la agenda, el usuario debe crear un nombre de usuario y una contraseña.
2. Salt & hash la contraseña y almacenarla en la base de datos con el nombre de usuario como clave.
3. A continuación, proceder a la agenda.
4. La próxima vez que se ejecute ese programa, debería pedir el nombre de usuario y la contraseña, y sólo permitir el acceso si son correctos.
5. El nombre de usuario, la contraseña y la sal deben **excluirse** de las salidas de las entradas del diario, por razones obvias.


<detalles> <sumario> 💡 Consejos </sumario>

- Averigua si es la primera vez contando las claves del diario. Si no hay ninguna, es la primera vez.
- El nombre de usuario y la contraseña serán la **primera** entrada de clave en la base de datos. Piensa dónde empiezas a emitir las entradas del diario y ajusta tus bucles.

</detalles>