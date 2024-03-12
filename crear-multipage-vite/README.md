# Crear Aplicacion Multipage con React y Vite

Realicé este repositorio para que sirva de guia para los nuevos programadores como yo, aquellos que estan comenzando en React.
React+Vite crea paginas SPA (Single Page Application) [mas informacion](https://abamobile.com/web/que-es-single-page-application-spa/), pero encontre este método para que pase a ser multi page y te funciones para crear un buen portfolio de proyectos.

## Comencemos

(asumiendo que ya tienes el proyecto creado en Vite)
1. Movemos el index.html a la carpeta `src`
2. Modificamos los links del favicon y el link del script en el index para quitarles el acceso a la carpeta `src` 

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Vite + React</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/main.jsx"></script>
  </body>
</html>
```
3. En la carpeta `src` creamos la carpeta con el nombre de la pagina, en este caso, yo comencé con la pagina `about`
4. Copiamos el `index.html` y lo pegamos dentro de la carpeta `about` 
5. Creamos un archivo llamado `about.jsx` dentro de la carpeta about, modificamos la ruta del sript en el index.html, para colocar `./about.jsx` y colocamos este codigo:
```
import React from 'react'
import  ReactDOM  from 'react-dom'

ReactDOM.render(
    <React.StrictMode>
        <h1>Welcome to the about page</h1>
    </React.StrictMode>,
    document.getElementById('root')
)
```
6. En la terminal del VS code instalamos la dependencia ```npm i @types/node -D```
7. Vamos al `vite.config.js` e importamos `import { resolve } from 'path'`
8. Configuramos el root agregando 
```
const root = resolve(__dirname, 'src')
const outDir = resolve(__dirname, 'dist')
```
9. Dentro del arreglo `defineConfig` colocamos la variable `root` y la llave `build` quedando asi
```
import { resolve } from 'path'
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

const root = resolve(__dirname, 'src')
const outDir = resolve(__dirname, 'dist')

// https://vitejs.dev/config/
export default defineConfig({
  root,
  plugins: [react()],
  build:{
    outDir,
    emptyOutDir: true,
    rollupOptions: {
      input:{
        main: resolve(root, 'index.html'),
        about: resolve(root, 'about', 'index.html')
      }
    }
  }
})

```
10. La nueva oagina estará alojada en `http://localhost:5173/about/` 
> Recuerda que el enlace localhost podria cambiar
11. Puedes crear tantas paginas necesites y colocarlo en el input del *paso 9*
12. Asi quedó la mia
![image](https://github.com/borgesmj/crear-multipage-vite/assets/121818423/b08142c0-1ca9-4d36-963c-6daf5752fc6e)


## Fuente @basarat
  [![Fuente](https://img.youtube.com/vi/STeKBm67l6M/maxresdefault.jpg)](https://youtu.be/STeKBm67l6M)
