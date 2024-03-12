![nodeJs banner](https://github.com/borgesmj/NodeJs-notas/blob/main/IMG/banner.png "banner")
Notas tomadas del video de [fazt](https://github.com/fazt) en [![Youtube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://youtu.be/i3OdKwuBjeM?si=CEeqtVdu-t3gDg8d)


# ¿Que es NodeJs?
Es un entorno de ejecución de JavaScript

## Ejecutar Node.js

En la consola, colocamos el comando "node" para iniciar

## Limpiar la consola `Ctrl + L`

## Podemos ejecutar logica de JS en la consola

Math.random() \* 10 // 1.3435211387340251

## Crear una variable / const

al igual de la consola del navegador, se utiliza LET, CONST, VAR

## funciones

let x = 0
undefined

> do {
> ... x++;
> ... console.log(x);
> ... }
> ... while (x < 10)

// 1
// 2
// 3
// 4
// 5
// 6
// 7
// 8
// 9
// 10

## Set interval

setInterval(()=>{console.log('hello')}, 1000)

El REPL lo ejecuta cada 1 segundo infinitamente, para deteterlo presionamos dos veces `CTRL + C`

## Para utilizar node en la consola de windows sin iniciarlo, utilizamos node -e

node -e "console.log(10 +10 )" // 20

Cambiar la carpeta con cd

## Guardar archivos desde node

Existe un comando .save que te permite guardar un archivo js en la carpeta donde estes ubicado

Si cerramos la sesion con CTRL C y volvemos a abrir una nueva sesion node, llamamos a la variable pero no regresará nada porque ees una sesion nueva, pero podemos cargar el archivo guardado con `.load -nombre del archivo-`

```
 .load names.js
const names = ['joe', 'jhon', 'maria']
names
const newNames = names.map((name) => (`Hello ${name}`))

[ 'joe', 'jhon', 'maria' ]
>

```

## VS code

### Hola mundo en NodeJs

En VsCode podemos ejecutar el archivo JS y ver la consola utilizando node

Nuestro archivo JS tiene este codigo

```
let userName = "fast";
let age = 17;
let hasHobbies = true;
let points = [10, 20, 30];
let user = {
  name: "ryan",
  lastName: "ray",
};
const PI = 3.1415;

if (age >= 18) {
  console.log("tu eres  un adulto");
} else {
  console.log("No eres un adulto");
}

const names = ["jhon", "jon", "marco"];

for (let i = 0; i < names.length; i++) {
  console.log(names[i]);
}

const showUserInfo = (userName, userAge) =>
  `The username is ${userName}, the user is ${userAge} years old`;

console.log(showUserInfo("miguel", 30));
```

al llamar al archivo mediante node, este ejecutará todos los comandos que hayamos puesto en er archivo y los mostrar{a en consola

```
No eres un adulto
jhon
jon
marco
The username is miguel, the user is 30 years old
```

## Modulos de la API de Node

Node tiene multiples modulos para realizar operacione y funciones, [ver documentacion](https://nodejs.org/api/modules.html)

### Modulo OS

[visitar](https://nodejs.org/api/os.html)

El modulo OS nos ayuda a entrar al sistema operativo del computador donde se está trabajando, por ejemplo:

1. os.userInfo() nos regresa un objeto con informacion del sistema, por ejempl el nombre del usuario o carpeta del usuario

2. os.uptime() nos regresa el tiempo que lleva encendida la maquina

3. os.plataform() se ve el sistema operativo donde se está ejecutando el node

4. os.totalmem() se ve la memoria total

5. os.freemem() regresa la memoria libre

6. os.release() regresa la informacion general del sistema

### Modulo Path

[visitar](https://nodejs.org/api/path.html)

Este modulo nos permite trabajar co carpetas y archivos y poder saber sus direcciones.

Node se ejecuta en que sistema esta trabajando, asi que node usa este modulo para poder crear y entrar a los archivos y rutas de ubicacion

por ejemplo: en windows se entra a los archivos mediante

C:\\Users\\user\\Desktop

en cambio en linux y Mac seria

home/user/desktop

este tipo dedetalles hay que tener en cuenta porque los proyectos se despliegan en serviores linux

1. path.join() une directorios y rutas de directorios

```
const filePath = path.join('/public', 'dist', '/styles', 'main.css')
console.log(filePath) // \public\dist\styles\main.css
```

2. path.basename() permite extraer la base del diretoprio del archivo

```
console.log(path.basename(filePath))
//main.css
```

3. path.dirname() regresa la ruta del directorio o carpeta sin el nombre del archivo

```
console.log(path.dirname(filePath))
//\public\dist\styles
```

4. path.parse() regresa la informacion dle archivo y rutas, pero en forma de objeto

```
console.log(path.parse(filePath))
//{
//  root: '\\',
//  dir: '\\public\\dist\\styles',
//  base: 'main.css',
//  ext: '.css',
//  name: 'main'
//}
```

5. path.resolve() es una alternativa de join(), si se le pasa una ruta, el trata de completar a partyir de la ruta inicial del sistema

```
console.log(path.resolve('dist'))
// C:\Users\57320\Desktop\Node-course\dist
```

### Modulo file system

[visitar](https://nodejs.org/api/fs.html)

El módulo node:fs permite interactuar con el sistema de archivos siguiendo el modelo de las funciones POSIX estándar.

se puede leer, modificar, agregar o eliminar archivos utilizando este modulo

### Para leer archivos:

```
const first = fs.readFileSync('./data/first.txt')

```

leerá el archivo y regresa un buffer

```
<Buffer 68 6f 6c 61 20 6d 75 6e 64 6f 20 64 65 73 64 65 20 65 6c 20 61 72 63 68 69 76 6f>
```

para poder leerlo con letras y palabras, añadimos un segundo parametro 'Utf8', quedando asi

```
const first = fs.readFileSync('./data/first.txt', 'Utf8')
//hola mundo desde el archivo
```

tambien se puede utilizar el metodo JS

```
console.log(first.toString())

```

### Para crear archivos

Esta funcion recibe dos parametros, la ruta de ubicacion del archivo y el contenido que tendrá

```
fs.writeFileSync('./data/tercero.txt', 'este es un tercer archivo')
```

#### metodo asincrono

Utilizar file sistem con método asíncrono

1 Primer paso

```
fs.readFile('./data/first.txt', function(){
  console.log('Terminó')
})
```

Esta fragmento de código le indica al CPU que ejecute primero la funcion de leer el archivo y luego que termine, va a ejecutar la siguiente funcion de mostrar el mensaje en colsola.

2 Segundo paso
La segunda funcion regresa dos parametros, _error_ y _data_, que indican que salio mal y que salio bien en la ejecución del codigo

```
fs.readFile('./data/first.txt', function(error, data){
  console.log(error)
  console.log(data)
})
```

Al ejecutarse de esta manera el codigo, mos regresa dos valores `null` y `<Buffer 68 6f 6c 61 20 6d 75 6e 64 6f 20 64 65 73 64 65 20 65 6c 20 61 72 63 68 69 76 6f>`, el primero es null ya que no existe nungun error que mostrar, el segundo es el texto del archivo `fisrt.txt` pero en codigo buffer, que deberá ser traducido con UTF-8

Otra manera de colocar el codigo anterior, es con arrow function, y colocando el .toString() para que traduzca el código buffer y funcionará perfectamente igual

```
fs.readFile('./data/first.txt', (error, data) => {
    console.log(error)
    console.log(data.toString())
  })
})
```

3 Tercer paso
No es necesario mostrar un error si no existe, asi que se mostrará con un condicional if

si colocamos un error a proposito

```
fs.readFile('./desconocida/first.txt', (error, data) => {
    if (error){
        console.log(error)
    }
    console.log(data.toString())
  })
```

nos regresa el error

```
[Error: ENOENT: no such file or directory, open 'C:\Users\57320\Desktop\Node-course\desconocida\first.txt']
```

4 Si es necesario leer un archivo despues de leer el primero, se podria hacer de esta manera

```
fs.readFile('./data/first.txt', (error, data) => {
    if (error){
        console.log(error)
    }
    console.log(data.toString())
    fs.readFile('./data/second.txt', (error, data) => {
        if (error){
            console.log(error)
        }
        console.log(data.toString())
        fs.writeFile('./data/newFile.txt', 'archivo creado desde fs', (error, data)=> {
            console.log(error)
            console.log(data)
        })
      })
  })
```

este codigo, lo que hace es ejecuta la primera funcion, lee el primero archivo, finalizado este lee el segundo archivo y luego finalizado crea un archivo con la tercera funcion, en la consola regresará

```
hola mundo desde el archivo
hello world 2
null
undefined
```

null es porque no existe un error en la tercera funcion y el undefided porque la funcion para crear archivos no regresa nada

Pero esta practica no es recomendable, porque si hay muchos fragmetos, se va iendo a la derecha y esto se llama [**callback hell**](https://www.google.com/search?q=callback+hell&sca_esv=578828967&rlz=1C1ALOY_esCO1055CO1055&tbm=isch&sxsrf=AM9HkKm6k1f29OV0t3twJ2C9cMMq07E-RQ:1698936710435&source=lnms&sa=X&ved=2ahUKEwjE7Pu4yKWCAxWSIEQIHVlWAMgQ_AUoAXoECAEQAw&biw=681&bih=601&dpr=1), ese metodo es inmantenible, se evita con promesas y async/await

### Modulo HTTP

En este módulo nos va a servir para poder crear los principales progranas qye se usan en Node, que serian servidores web, para comenzar creamos un archivo llamado `http.js`, importamos el modulo y guardamos en una constante del mismo nombre

```
const http = require('http')
```

PAra comenzar a entender este modulo primero hay que explicar un concepto basico en aplixaciones web wue se conoce conmo cliente-servidor.

Protocolo HTTP, es la manera de comunicar de entre dos computadores, la del cliente y el servidor.

con el modulo HTTP ahora creamos un servidor

Un servidor es un programa que estará 24/7 recibienod y enviando información, como por el momento no es necesario enviar una respuesta a un cliente, solo colocamos un 'Hello world' como respuesta, node requiere que finalices la respuesta despues de obtener un response, asi que debemos finalizar con response.end(), cuando alguien visote nuestro servidor, solo se le regresará un texto que diga "Hello World", luego necesitamos un puerto donde esté funcionando constantemente nuestro programa, para esto buscamos un puerto de la lista que hay en [internet](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers) buscamdo uno que no esté reservado, para este ejemplo, usaremos el puerto 3000

```
const http = require('http')

http.createServer((request, response) => {
    response.write('hello World')
    response.end()
}).listen(3000)

console.log('Servidor escuchando en el puesrto 3000')
```

Al ejecutar nos regresará en consola `Servidor escuchando en el puesrto 3000` y si visitamos [localhost:3000](http://localhost:3000/) regresa un "Hello world", ya esto nos indica que el puerto está funcionando

### Request

En la seccion anterior hemos creado un ejemplo basico de un servidor HTTP, ahora veremos que funciona el objeto request.

Para esto colocamos un `console.log(request)` dentro de nuestro codigo y ejecutamos, la pa gina de localhost seguira funcionando, y muestra el "Hello World" pero si vamos a la consola de NodeJs veremos todos el objeto HTTP, el objeto HTTP es informacion acerca del cliente que se puede utilizar en el backend.

El objeto HTTP es muy grande y hay ciertas cosas puntuales que necesitamos saber, por ejemplo, si quiero saber la url del cliente, utilizamos `console.log(request.url)`, guadramos, cerramos y volvemos a abrir el servidor, nos regresará

```
/
/favicon.ico
```

el '/' es porque el navegador interpreta la url base que se esta visitando, en este caso es `http://localhost:3000/` y toma el / final, y el `/favicon.ico` es porque siempre el navegador le va a pedir al servidor un favicon para mostrar, cada vez que el cliente cambie de url cambiara el / en la consola, si el cliente entra en `http://localhost:3000/profile` la consola regresará `/profile`, esto se puede utilizar para mostrar mensajes o paginas personalizadas dependiendo de la pagina que visita el cliente, por ejemplo:

```
const http = require('http')

http.createServer((request, response) => {

    console.log(request.url)

    if (request.url === '/about'){
        response.write('Acerca de')
        response.end()
    }

    response.write('hello World')
    response.end()
}).listen(3000)

console.log('Servidor escuchando en el puesrto 3000')
```

esta version del codigo evaluará si el cliente entró a la página `/about` y regresará `Acerca de`, guardamos, cerramos y volvemos a abrir el puerto. Al entrar en la oagin /about la consola nos regresará un error, esto debido a que el codigo tiene dos response.write(), asi que para solucionar este caso, debemos colocar un return antes del response.end() de la pagina '/about' para que se salga del codigo cuando lo ejecute, cerramos y volvemos a abrir el puerto.

Colocando estas condicionales, podemos establecer que se le regresa al cliente dependiendo la url que visite, de esta manera:

```
const http = require('http')

http.createServer((request, response) => {

    console.log(request.url)

    if (request.url === '/about'){
        response.write('Acerca de')
        return response.end()
    }

    if (request.url === '/'){
        response.write('Welcome to the server')
        return response.end()
    }

    response.write('not found')
    response.end()
}).listen(3000)

console.log('Servidor escuchando en el puesrto 3000')
```

- Si el cliente entra a la pagina principal, se le regresa `Welcome to the server`
- Si el cliente entra a '/about', se le regresara 'Acerca de'
- Pero si el cliente entra a cualquier otra pagina, se le va a regresar un 'Not found', que vendria siendo un muy pequeño ejemplo de error 404

Ahora, no solo se le puede regresra un texto, sino tambien un HTML al cliente.

```
const http = require('http')

http.createServer((request, response) => {

    console.log(request.url)

    if (request.url === '/about'){
        response.write('Acerca de')
        return response.end()
    }

    if (request.url === '/'){
        response.write('Welcome to the server')
        return response.end()
    }

    response.write('<h1>Error 404</h1>')
    response.end()
}).listen(3000)

console.log('Servidor escuchando en el puesrto 3000')
```

Esto regresará un error de not found o 404 al cliente si entra a una pagina web no registrada.

Si queremos colocar mucho mas texto, es bastante incomodo con conmillas simples, utilizamos los backticks para poder realizar saltos de linea y colocar mas codigo

```
const http = require('http')

http.createServer((request, response) => {

    console.log(request.url)

    if (request.url === '/about'){
        response.write('Acerca de')
        return response.end()
    }

    if (request.url === '/'){
        response.write('Welcome to the server')
        return response.end()
    }

    response.write(`
    <h1>Error 404</h1>
    <p>Esta pagina no se encuentra</p>
    <a href='/'>Regresar a la pagina de inicio</a>
    `)
    response.end()
}).listen(3000)

console.log('Servidor escuchando en el puesrto 3000')
```

De esta manera creamos nuestro servidor basico con node.

### npm

Hasta ajora, hemos aprendido a crear nuestros propios modulos, como los de la carpeta Math, o importado los modulos que ofrece node, pero hay modulos que no son creaos por nosotros ni trae node predeterminado, estos son los oaquetes de terceros, creados por otros desarrolladores, en codigo open source.

[visitar npm](https://www.npmjs.com/)

En esta pagina se encuentran modulos JavaScript y Node que se pueden utilizar

desarrolladores de node utilizan muchos paquetes aqui plasmados, por ejemplo, si queremos darle color a los mensajes de consola, utilizariamos [colors](https://www.npmjs.com/package/colors)

Realicemos un ejemplo:

Creamos un archivo en la carpeta raiz llamado `click.js` y colocamos el siguiente codigo

```
console.log('hello world')
console.log('borgesmj.github.io')
console.log('google.com')
```

Ejecutamos y comprobamos que este funcionando correctamente `node click.js`

ahora si le queremos colocar colores:

1 Ejecutamos el comando `npm install colors`
Esto creará tres archivos `package.json` `package-lock-json` y `node_modules`

2 importamos la propiedad colors
`const colors = require('colors')`

3 Solo hay que colocar un '.' al final del string y el módulo nos dara una serie de opciones para colocar en la consola

```
console.log('hello world'.bgGreen)
console.log('borgesmj.github.io'.bgBlue)
console.log('google.com'.rainbow)
```

### npm init
Existe una manera de crear tu propio archivo package.json manualmente, y colocar los datos que necesitemos

ejecutamos el comandp `npm init` y comienza a ejecutar unas preguntas referente a nuestro proyecto. 

1 Colocalmos el nombre del proyecto
2 Colocamos la version. Esta está identificada por un numero semver (semantic version), que tiene tres numeros (0.0.1), si le hacemos cambios muy pequeños a nuestra app, le cambiamos el tercer numero, de izquierda a derecha, si añadimos un cambio importante, pero que no afecta a la biblioteca se cambia el numero del medio, pero si se realiza un gran cambio que ya no es compatible con una version anterior, se cambia el primer numero.
3 Desccripcion
4 Archivo inicial, es el archivo que se va a iniciar cada vez que se inicie el programa, por defecto, node sugiere "index.js"
5 test comand
6 repositoio de git
7 Palabras claves
8 Autor
9 Licencia

Con este package.json podemos crear nuestros propios comandos en los scripts, por ejemplo, creamos un comando llamado "ejecutar", al que le ponemos las instrucciones "node app.js", ahora en la consola colocamos `npm run ejecutar`, esto funciona para aquellos programas que tienen muchos parametros.

Si cambiamos el comando "ejecutar" a "start", podemos quitar el run y que quede `npm start`, pero esto solo aplica para el comando start.

Podemos añadir todos los comandos que sean necesarios para nuestro proyecto.

Con un proyecto pequeño, no hay problema tener que guardar y ejecutar el comando cada vez que haya cambios, pero cuando es un proyecto grande, con mucho codigo, es recomendable utilizar el modulo "nodemon"

`npm i nodemon -D`

el -D es para instalarlo en el modo de desarrollo, para que node sepa que no es necesario en el modo de produccion

Lo que hace nodemon es ver todos los cambios que se vayan realizando en el codigo, y realiza los cambios sin tener que volver a ejecutar el comando 

### Modulos Globales
Node buscará los modulos dentro de nuestra lista de dependencias en el archivo package.json, si no lo encuentra, lo buscará en la carpeta "node_modules" y si no lo encuentra, lo buscara en las dependecias instaladas globalmente en el computador.

Para instalar una dependecia global, utilizamos la flag `-g` cuando vayamos a instalar nodemos o cualquier otro modulo

### npx
Este comando nos sirve para ejecutar aplicaciones de consola que ya vienen instalado con npm.

La carpera /node_modules/.bin tiene todos los ejecutables contenidos del proyecto

una manera de ejecutar algun comando contenido en la carpeta .bin podria ser con el siguiente comando:


```
.\node_modules\.bin\nodemon index.js 
```

Para que ejecute el archivo index.js, ya que nodemon está almacenado dentro de esta ruta de carpeta, asi se puede usar modulos que funcionan como CLI [(Command Line Interface)](https://aws.amazon.com/es/what-is/cli/#:~:text=A%20command%20line%20interface%20(CLI)%20is%20a%20text%2Dbased,operating%20system%20and%20the%20user.).

Si instalamos un modulo cualquiera, por ejemplo [Cowsay](https://www.npmjs.com/package/cowsay), para ejecutarlo mediante un scripts colocariamos en el package.json

```
{
  "dependencies": {
    "colors": "^1.4.0",
    "cowsay": "^1.5.0",
    "nodemon": "^3.0.1"
  },
  "devDependencies": {
  },
  "scripts": {
    "divaca": "cowsay hello world"
  }
}
```

Al ejecutarlo con `npm run divaca` la consola regresa

```
 _____________
< hello world >
 -------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

Ahora imaginemos que no necesitemos instalar este modulo, porque es algo muy momentaneo y puntual, hay una manera de utilizarlo sin tener que instalarlo, y esta manera es con `npx`, npx buscara en internet un modulo que no existe en el computador, lo va a descargar y ejecutarlo inmediatamente

```
  npx cowsay curso de node
```

La consola preguntará si procede a instalar el paquete, y luego ejecutará

```
 _______________
< curso de node >
 ---------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

¿Para que sirve esto?
Hay veces que queremos ejecutar programas que esten desarrollados con Node, pero no queremos instalarlos, solo utlizarlos una sola vez y que liego se elimine.

Veamos otro ejemplo:

1 Creemos una carpeta "public" y dentro de esta carpeta creamos un archivo HTML
2 Crearemos un servidor temporal utilizando el paquete npm [serve](https://www.npmjs.com/package/serve), pero no lo instalaremos por completo, ya que no lo necesitamos para desarrollo ni para produccion, asi que utilizaremos el comando `npx`
3 En la consola colocamos
```
npx serve public
```

nos crea un servidor http, y lo interesante de esto, es que los cambios que se realicen en el archivo html se veran reflejados en la pagina web. 

### Event Loop
Hasta este momento hemos creado funciones que nos permiten poder manejar peticiones, funciones que nos permiten poder ser ejecutadas despues de un tiempo, un ejemplo de esto es que podemos crear un servidor basico utilizando el modulo HTTP.

Este modulo, para poder crearlo, utiliza una funcion `createServer` y como parametros esperaba otras funciones, lo interesante de JavaScript es que vamos a necesitar una funcion, porque los parametros se ejecutan despues de un tiempo, o mejor dicho, se ejecutan despues de un evento. Para poder entender porque se ejecuta una funcion dentro de una funcion, hay que entender el concepto basico de node que se conoce como **event loop**.

Aqui tenemos un ejemplo
1 Creamos un archivo `event_loop.js` que tendrá tres comandos sencillos

```
console.log('first')
console.log('second')
console.log('third')
```

y ejecutamos el comando `node event_loop.js` la consola nos regresa:

```
first
second
third
```

2 Cuando halbamos de JavaScript y el Codigo asincrono

```
console.log('first')
setTimeout(() => {
    console.log('second')
}, 3000);
console.log('third')
```

node ejecutará el primer y tercer console.log, y el segundo lo ejecutara despues de un tiempo

Aunque cambiemos el valor del tiempo a 0, de esta manera 
```
console.log('first')
setTimeout(() => {
    console.log('second')
}, 0);
console.log('third')
```

la consola regresará 
```
first
third
second
```

por mas que el tiempo sea 0, node interpreta ese fragmento de codigo como una tarea pendiente y lo ejecuta al final.

Para hacer un ejemplo mas visual, crearemos un servidor HTTP sencillo

```
const http = require("http");

const server = http.createServer((req, res) => {
  if (req.url === "/") {
    res.write("welcome to the server");
    return res.end();
  }
  if (req.url === '/about'){
    return res.end('this is about page') // esta es otra manera de escribir, sin tener que colocar 'res.write'
  }

  res.end('not found')
});

server.listen(3000)
console.log('server on port 3000')
```

Ahora, aqui esta el detalle de que node puede manejar una sola tarea a la vez, supongamos que cuando se visita la pagina `/about` vamos a estar trabajando con una logica pesada, consulta a una base de datos o a otro servidor, o la ejecucion de una tarea que lleve mucho tiempo, por ejemplo:

```
const http = require("http");

const server = http.createServer((req, res) => {
  if (req.url === "/") {
    res.write("welcome to the server");
    return res.end();
  }
  if (req.url === '/about'){

    // una tarea pesada
    for (let i = 0; i < 100000; i++) {
        console.log(Math.random() * i)
    }

    return res.end('this is about page') // esta es otra manera de escribir, sin tener que colocar 'res.write'
  }

  res.end('not found')
});

server.listen(3000)
console.log('server on port 3000')
```

va a estar cargando la pagina `about` hasta que realice toda la tarea, incluso si visitamos en otra pestaña `localhost:3000` no cargará porque la base de la url esta bloqueado mientras realiza la tarea, no permite que node realice otra tarea, al bucle for se le conoce como codigo bloqueante, para evitar esto, se utiliza codigo asincrono, se ejecuta en un segundo plano, asi el codigo seguira ejecutando, y recibiendo peticiones

### Promesas
En esta seccion aprenderemos a utilizar un concepto muy importante de JS que se le conoce como promesas, es una manera mas facil de escribir codigo asincrono y ,ejor entendible que los callback.

Para entender este problema, resolveremos el codigo de file sistem utilizando promesas:

1 Crearemos un archivo que llamaremos `promises.js` y dentro de promises vamos a tratar de leer un archivo

```
const {readFile} = require('fs')

readFile('./data/first.txt', 'utf-8', (err, data) => {
    if (err){
        console.log(err)
    }
    console.log(data)
})
```

nos regresa en la consola 

```
hola mundo desde el archivo
```

El código funciona, pero escrito de esa manera, es un poco dificil de entenderm sobre todo para proyetos grandes, asi que se puede convertir el callback en una promesa:


```
const {readFile} = require('fs')

function getText(pathFile){
    return new Promise(function(resolve, reject){
        readFile(pathFile, 'utf-8', (err, data) => {
            if (err){
                reject(err)
            }
            resolve(data)
        })
    })
}

// si quiero leer un archivo, ya no es necesario escribir "readfile", en cambio, llamamos a la funcion pasando la ruta del archivo como parametro

getText("./data/second.txt")
    .then((result) => console.log(result))
    //si quiero leer otro archivo despues del primero
    .then(() => getText("./data/tercero.txt"))
    .then(result => console.log(result))
    .catch((error) => console.log(error))
```

puedo tener tantos `.then` como sean necesarios pero solo es necesario un `.catch(error)`, pero hay una manera aun mas sencilla de escribir este código.

### async/await

Hay una manera mas sencilla de escirbir el codigo anterior, utilizando un concepto nuevo de JavaScript, el cual se llama "Async/Await"

`Async` sirve para que podamos especificar que una funcion adentro de su contenido, está manejando un codigo asincrono, y `await` es cuando estamos usando una funcion asincrona, para indicar que esa funcion va a tomar algo de tiempo.

Volveremos a utilizar la funcion getText() pero con `async/await`

```
const {readFile} = require('fs')


function getText(pathFile){
    return new Promise(function(resolve, reject){
        readFile(pathFile, 'utf-8', (err, data) => {
            if (err){
                reject(err)
            }
            resolve(data)
        })
    })
}
async function read(){
    const result = await getText('./data/first.txt')
    const result2 = await getText('./data/second.txt')
    const result3 = await getText('./data/tercero.txt')
    const result4 = await getText('./data/newfile.txt')
    console.log(result)
    console.log(result2)
    console.log(result3)
    console.log(result4)
}

read()
```

pero ahora si queremos que nos refleje el error en caso de que haya uno, utilizamos `try/catch`

```
const { error } = require("console");
const { readFile } = require("fs");

function getText(pathFile) {
  return new Promise(function (resolve, reject) {
    readFile(pathFile, "utf-8", (err, data) => {
      if (err) {
        reject(err);
      }
      resolve(data);
    });
  });
}

async function read() {
  try {
    const result = await getText("./data/first.txt");
    const result2 = await getText("./data/second.txt");
    const result3 = await getText("./data/tercero.txt");
    const result4 = await getText("./data/newfile.txt");
    console.log(result);
    console.log(result2);
    console.log(result3);
    console.log(result4);
  } catch (error) {
    console.log(error);
  }
}

read();
```

Pero tambien podemos generar y explicar nuestros propios errores para indicar a otros desarrolladores donde está. utilizamos `throw`

### Promisify
En la seccion anterior hemos aprendido a como escribir promesas de una manera bastante sencilla con `async/await`, pero una parte importante es hacer callbacks y el fragmento de `getText()` es bastante dificil de leer, para hacerlo mas sencillo, node tiene modulos para hacerlo mas sencilla.

toda la funcion `function getText(pathFile)` lo pasamos a una sola linea `const readFilePromise = promisify(readFile)` quedando de esta manera:

```
const { readFile } = require("fs");
//importamos promosify desde los modulos de node
const { promisify } = require("util");

const readFilePromise = promisify(readFile);

async function read() {
  try {
    const result = await readFilePromise("./data/first.txt", "utf-8");
    console.log(result);
    const result2 = await readFilePromise("./data/second.txt", "utf-8");
    console.log(result2);
    const result3 = await readFilePromise("./data/tercero.txt", "utf-8");
    console.log(result3);
    const result4 = await readFilePromise("./data/newfile.txt", "utf-8");
    console.log(result4);
  } catch (error) {
    console.log(error);
  }
}

read();

```

### fs/promise

Desde file sistem podemos ahorrar el convertir la promesa con `promisify` utilizando `const { readFile } = require('fs/promises');` quedando de la siguiente manera:

```
const { readFile } = require('fs/promises');

async function read() {
  try {
    const result = await readFile("./data/first.txt", "utf-8");
    console.log(result);
    const result2 = await readFile("./data/second.txt", "utf-8");
    console.log(result2);
    const result3 = await readFile("./data/tercero.txt", "utf-8");
    console.log(result3);
    const result4 = await readFile("./data/newfile.txt", "utf-8");
    console.log(result4);
  } catch (error) {
    console.log(error);
  }
}

read();

```

Así, de esta manera, nos hemos ahorrado otras lineas de codigo, haciendolo mas entendible y facil de leer

### Eventos

En esta sección vamos a aprender a manejar eventos en Node
Cuando trabajamos con JavaScript en en frontEnd, hemos visto que si queremos añadir una escucha a un boton, debemos añadir un boton en el HTML, un `script` al documento, y un `addEventListener` a ese boton.

Una parte importante de JavaScript es el manejo de eventos.

Node provee modulos para crear eventos propios

```
const EventEmitter = require('events')

const customEmitter = new EventEmitter()
/*
customEmitter.emit() //emitir un evento
customEmitter.on() // escucha el evento
*/

customEmitter.on('response', (data) => {
    console.log(data)
})

customEmitter.emit('response')
```

la consola nos regresa `undefined` ya que el response esperaba unos datos, pero si modificamos el evento 'on' a:

```
customEmitter.on('response', (data) => {
    console.log('recibido')
    console.log(data)
})
```

nos regresará `recibido` y `undefined`

Ahora si colocamos otro parametro en `customEvent.emit()` de esta manera

```
customEmitter.emit('response', 'hello world')
```

la consola nos regresará

```
recibido
hello world
```

Asi como en el HTML podemos poner multiples eventos, podemos colocar multiples emit

```
customEmitter.emit('response', 'hello world')
customEmitter.emit('response', 'borgesmj')
customEmitter.emit('response', 'nodejs')
customEmitter.emit('response', 30)
customEmitter.emit('response', [1,2,3])
```

La consola nos regresará

```
recibido
hello world
recibido
borgesmj
recibido
nodejs
recibido
30
recibido
[ 1, 2, 3 ]
```

¿Para que sirve estos eventos?

Si recordamos, cuando creamos nuestro modulo HTTP, hemos creado un servidor, ese servidor espera una funcion, y esa funcion responde despues de determinado evento, es decir, cuando llega una peticion recien se ejecuta ese evento, y la funcion `createServer` tiene multiples lineas de escucha y emision de eventos.

### Streams

Los streams nos ayuda a enviar o dividir un archivo grande en multiples partes, para que sea trasmitido facilmente.

Primero creamos un archivo grande

```
const {writeFile} = require('fs/promises')


const  createBigfile = async() => {
    await writeFile('./data/bigfile.txt', 'hello world'.repeat(1000000))
}

createBigfile()
```

El `.repeat()` repetirá las veces que tenga de parámetro

para ver el tamaño del archivo colocamos el comando `dir data` y, en este caso, nos regresa: 

```
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a---         3/11/2023 1:45 p. m.       11000000 bigfile.txt
-a---        30/10/2023 2:03 p. m.             27 first.txt
-a---         2/11/2023 9:43 a. m.             23 newFile.txt
-a---        30/10/2023 2:00 p. m.             13 second.txt
-a---        30/10/2023 2:45 p. m.             50 tercero.txt
```

El archivo bigfile pesa mas de 10Mb, si un usuario desea usar este archivo, la mejor opcion seria dividirlo en partes 

```
const {createReadStream} = require('fs')

const streams = createReadStream('./data/bigfile.txt')

streams.on('data', (chunk) => {
    console.log(chunk)
})
```

Requerimos `createReadStream` del modulo fs, y lo llevamos a una constante y le pasamos de parametro el archivo grande, luego colocamos un listener de evento, nos regresa un objeto de eventos, luego cuando escucha el ebvento data, nosotros veremos porciones de datos a los que llamamos `chunk`, dividirá el archivo 65kb a la vez, y eso es lo que va mostrando.

Aparte de dividir los archivos, tambien tiene el evento para enviar un mensaje al final del stream

```
streams.on('end', () => {
    console.log('ya termine de leer el archivo')
})
```

y el createReadStream puede recibir un objeto de parametro donde se puede colocar el codificado

```
const streams = createReadStream('./data/bigfile2.txt',{
    encoding: 'utf-8'
})
```


### Streams y HTTP

```
const http = require('http')
const {createReadStream} = require('fs')



const server = http.createServer((req, res) => {
    const fileStream = createReadStream('./data/bigfile.txt', {
        encoding: 'utf-8'
    })

    fileStream.on('data', (chunk) => {
        fileStream.pipe(res)
    })

    fileStream.on('error', error => {
        console.log(error)
    })
})

server.listen(3000)
console.log(`server on port  ${3000}`)
```

[**ver mas**](https://nodejs.org/api/stream.html)

### EcmaScript modules
Este es un modulo que permite importar módulos en otros módulos.
Ya antes hemos hablado de los modulos, que nos funcionan para poder dividir un proyecto en partes, y teniamos la sintaxis `module.exports`, a esta sintaxis se le conoce como [**Commom JS**](https://nodejs.org/api/modules.html), para poder exportar e importar modulos.

Actualmente, hay un estandar en el navegador, y Node tambien está tratando de adaptarse a ese estandar, es decir, una sola forma de importar modulos. ¿Es posible usar `import` y `export`?, Si, si se puede usar, pero se debe realizar una configuracion antes.

Primero aprendamos una verison mas rapida de `npm init` para crear un package.json

Introducimos el comando 
```
npm init -y
```

De esta manera, se crea el archivo con las respuestas predeterminadas o por defecto.

Se hace énfasis en el package.json debido a que la configuracion va en este archivo

Añadimos una propiedad llamada `"type": "module",`, ahora podemos usar la sintaxis `import` y `export` en los archivos de JavaScript


creamos un archivo `esmodule.js`, recordemos que teniamos un archivo llamado `index.js` dentro de la carpeta `Math` que esportaba de esta manera:

```
module.exports = {
    add,
    sustract,
    divide,
    multiply
}
```

Ahora podemos hacerlo de esta manera: 

```
export default {
    add,
    sustract,
    divide,
    multiply
}
```

de la manera ES6, y en el archivo que acabamos de crear lo importaremos

```
import math from './Math/index.js'
```

**Muy imortante:** debe tener la extension del archivo.

Otro dato *importante*, el archivo que se exporta no debe quedarse con `module.exports =` debe tener `export default`, ya que la primera manera es commonJs y es la manera vieja y la segunda manera es mas moderna y que mas se asemeja a la usada por el navegador, se puede usar o una o la otra, pero no ambas al mismo tiempo.


Supongamos que no queremos exportar todas las funciones del archivo, sino funciones individualmente 

```
export function add(x,y){
    return x+y
}

export function sustract(x,y){
    return x-y
}

function multiply(x,y){
    return x*y
}

function divide(x,y){
    return x/y
}

```

y en archivo donde importamos

```
import {sustract} from './Math/index.js'
console.log(sustract(10,20))
```

### fetch

En la seccion anterior  hemos aprendido a utilizar los modulos de ES6, otra forma de conocer otras caracteristicas de node, es conociendo las API modernas que tiene, por ejemplo, utilizamos una API muy utilizada en las ultimas versiones, que seria `fetch()`, esta API nos sirve para traer datos de una direccion o una url.

Para el ejemplo, estaremos trabajando emn el archivo `fetch.js`

```
fetch("https://jsonplaceholder.typicode.com/posts")
  .then(res => res.json())
  .then(data => console.log(data));

```


Y si lo queremos utilizar con una funcion asincrona

```
async function loadData() {
    try {
        const res = await fetch("https://jsonplaceholder.typicode.com/posts");
        const data = await res.json();
        console.log(data);
    } catch (error) {
        console.log(error)
    }
}


loadData()
```
### Express

Hasta ahora hemos aprendido las bases de Node, hemos aprendido conceptos como los eventos, FS, y demas modulos, ahora si revisamos el modulo de http, hemos estado colocando logica como `request.url === '/` y regresabamos algo, esto funciona, pero si debemos construir una aplicacion real, por ejemplo con muchas mas rutas, ese metodo seria muy laborioso, en la actualidad se no se escribe codigo desde cero, para eso ya estan construidos los framworks que nos permiten resumir las logicas.

Para ejemplo, utilizaremos uno de esos frameworks

Vamos a crear una carpeta nueva en el escritorio y la llaaremos `node-website`

Comenzamos con iniciar el proyecto `npm init -y`, esto nos creará el package.json del proyecto

Ahora instalaremos una framework para trabajar en el proyecto

Googleamos "nodejs frameworks list" y nos da una serie de frameworks utilizados en la actualidad, para este ejemplo se utlizará ExpressJs que lo conseguimos en el siguiente [enlace](https://expressjs.com/)

¿Que hace este framework?, nos permite escribir codigo de backend similar a lo que hemos hecho hasta ahora, sin condicionales y minimizando el código.

[npm](https://www.npmjs.com/package/express)

Comenzamos con instalarlo, `npm i express` y creamos el archivo de arranque `ìndex.js` dentro del cual colocamos 

```
import  express  from "express";

const app = express()

app.listen(3000)
```

**NOTA:** recuerda modificar el package.json para y colocar `"type": "module",`

Si visitamos el enlace `http://localhost:3000/` nos regresa un `Cannot GET \` que seria la respuesta por  defecto y la muestra que nuestro programa funcionó bien pero que no regresa nada, si quisieramos regresar algo colocamos mas funciones

```
import  express  from "express";

const app = express()

app.get('/', (req, res) => {
    res.send('<h1>Bienvenido</h1>')
})
app.get('/about', (req, res) => {
    res.send('<h1>about</h1>')
})


app.listen(3000)

console.log('server on port 3000')
```

### Deploy 

En esta seccion, desplegaremos una aplicacion de Node de forma gratuita y aprenderemos como se ve una aplicacion de node en la realidad

Cuando realizamos aplicaciones con Node, nosotros no solo elaborar herramientas basadas en JavaScript que interactuan con el sistema operativo, sino que su principal uso es crear servidores web.

En la seccion anterior creamos una mini app ejemplo utilizando la framework Express, ahora, nosotros necesitamos desplegarlo, subirlo a la internet, ahora en este momento, nosotros podemos trabajar con node porque lo tenemos instalado en nuestro ordenador, por lo tanto, tambien debe estar instalado en donde se requiera trabajar.

Uno de los servicios gratuitos y en la nube para poder subir el codigo es `Heroku`, 