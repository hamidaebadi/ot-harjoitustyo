import unittest
from repositories.product_repository import product_repositories
from model.product_model import Product

class TestProductRepository(unittest.TestCase):
    def setUp(self):
        self.product_test = Product("puhelinx", "Puhelimet", "0000", 100)

    def test_add_new_product(self):
        result = product_repositories.add_new_product(self.product_test)
        self.assertEqual(result, True)

    def test_find_product(self):
        result = product_repositories.find_product(self.product_test.product_name)
        self.assertIsInstance(result, Product)

    

    