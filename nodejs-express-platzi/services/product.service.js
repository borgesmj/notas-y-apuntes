const { faker } = require('@faker-js/faker');

class ProductsService {
  constructor() {
    this.products = [];
    this.generate();
  }

  generate() {
    const limit = 100;
    for (let index = 0; index < limit; index++) {
      this.products.push({
        id: faker.string.uuid(),
        name: faker.commerce.productName(),
        price: parseInt(faker.commerce.price(), 10),
        image: faker.image.url(),
      });
    }
  }

  // Para crear un nuevo producto
  create(data) {
    const newProduct = {
      id: faker.string.uuid(),
      ...data,
    };
    this.products.push(newProduct);
    return newProduct;
  }

  find() {
    return this.products;
  }

  findOne(id) {
    return this.products.find((item) => item.id === id);
  }

  update(id, changes) {
    const index = this.products.findIndex((item) => item.id === id);
    if (index === -1) {
      throw new Error('El producto no existe');
    }
    const product = this.products[index];
    this.products[index] = {
      ...product,
      ...changes,
    }
    return this.products[index];

  }

  delete(id) {
    const index = this.products.findIndex((item) => item.id === id);
    if (index === -1) {
      throw new Error('El producto no existe');
    } else {
      this.products.splice(index, 1); // recibe una posicion, y le decimos cuantos elementos queremos eliminar a partir de esa posicion
      return { id };
    }
  }
}

module.exports = ProductsService;
