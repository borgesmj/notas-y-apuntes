const express = require('express');

ProductsService = require('./../services/product.service')

const router = express.Router();
// creamos una instancia de ese servicio
const service = new ProductsService()


// llamamos al servicio para poder encontrar todos productos
router.get('/', (req, res) => {
  const products = service.find();
  res.json(products);
});

// llamamos al servicio para traer un producto en especifico
router.get('/:id', (req, res) => {
  const { id } = req.params;
  const product = service.findOne(id);
  res.json(product)
});

router.post('/', (req, res) => {
  const body = req.body;
  const newProduct = service.create(body)
  res.status(201).json(newProduct);
});

router.patch('/:id', (req, res) => {
  const {id} = req.params
  const body = req.body;
  const product = service.update(id, body)
  res.json(product);
});

router.delete('/:id', (req, res) => {
  const {id} = req.params
  const rta = service.delete(id);
  res.json(rta);
});



module.exports = router;
