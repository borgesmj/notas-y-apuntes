const express = require('express');
const app = express();
const port = 3000;
const routerApi = require('./Routes') // importamos el archivo de las rutas, no colocamos "index.js" porque ya ese es un archivo que se busca en automatico

app.use(express.json())

app.get('/', (req, res) => {
  res.send('este es mi servidor express');
});
// rutas de ejemplo
app.get('/nueva-ruta', (req, res) => {
  res.send('nueva ruta'); // un ejemplo de una ruta distinta
});

routerApi(app)




app.listen(port, () => {
  console.log('app running on port:', port);
});
