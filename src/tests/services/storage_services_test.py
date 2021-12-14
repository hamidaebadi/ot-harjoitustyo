import unittest
from model.product_model import Product
from services.storage_services import Storage

class TestStorageServices(unittest.TestCase):
    def setUp(self):
        self._storage_object = Storage()
        self._qr_code = "412321"
        self._wrong_qrcode = "wrong"
        self._wrong_category = "wrong"
        self._correct_product_name = "Notebook X"
        self._wrong_product_name = "wrong"


    def test_correct_category_finds_products(self):
        productList = self._storage_object.get_stored_products("Puhelimet")
        self.assertNotEqual(productList, False)

    def test_wrong_category_returns_zero_products(self):
        result = self._storage_object.get_stored_products(self._wrong_category)
        self.assertEqual(len(result), 0)

    def test_product_founded_with_correct_qrcode(self):
        result = self._storage_object.search_product(self._qr_code)
        self.assertNotEqual(result, False)

    def test_product_not_founded_with_wrong_qrcode(self):
        result = self._storage_object.search_product(self._wrong_qrcode)
        self.assertEqual(result, False)
