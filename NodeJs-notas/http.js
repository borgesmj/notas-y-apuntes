const http = require("http");

const server = http.createServer((request, response) => {
  console.log(request.url);

  if (request.url === "/about") {
    response.write("Acerca de");
    return response.end();
  }

  if (request.url === "/") {
    response.write("Welcome to the server");
    return response.end();
  }

  response.write(`
    <h1>Error 404</h1>
    <p>Esta pagina no se encuentra</p>
    <a href='/'>Regresar a la pagina de inicio</a>
    `);
  response.end();
});

server.listen(3000);

console.log("Servidor escuchando en el puesrto 3000");
