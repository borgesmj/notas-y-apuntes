const { isUtf8 } = require("buffer");
const fs = require("fs");

// const first = fs.readFileSync('./data/first.txt', 'Utf8')

// const second= fs.readFileSync('./data/second.txt')

// console.log(first)
// console.log(second.toString())

// const contenido = 'este es el contenido dek tercer archivo modificado'

// fs.writeFileSync('./data/tercero.txt', contenido)

//Extraer datos con método asíncrono

fs.readFile("./data/first.txt", (error, data) => {
  if (error) {
    console.log(error);
  }
  console.log(data.toString());
  fs.readFile("./data/second.txt", (error, data) => {
    if (error) {
      console.log(error);
    }
    console.log(data.toString());
    fs.writeFile(
      "./data/newFile.txt",
      "archivo creado desde fs",
      (error, data) => {
        console.log(error);
        console.log(data);
      }
    );
  });
});
