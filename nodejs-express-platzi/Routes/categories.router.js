const express = require('express')

const router = express.Router()

router.get('/:categoryId/products/:productId', (req, res) => {
  const { productId, categoryId } = req.params;
  res.json({
    productId,
    categoryId,
    name: 'producto 2',
    value: 5000,
  });
});

module.exports = router
