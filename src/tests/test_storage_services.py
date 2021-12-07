import unittest
from services.storage_services import Storage

class TestStorageServices(unittest.TestCase):
    def setUp(self):
        self._storage_object = Storage()
        self._qr_code = "3442"
        self._wrong_qrcode = "wrong"


    def test_correct_category_finds_products(self):
        productList = self._storage_object.get_stored_products("Puhelimet")
        self.assertGreater(len(productList), 0)

    def test_product_founded_with_correct_qrcode(self):
        result = self._storage_object.search_product(self._qr_code)
        self.assertNotEqual(result, None)

    def test_product_not_founded_with_wrong_qrcode(self):
        result = self._storage_object.search_product(self._wrong_qrcode)
        self.assertEqual(result, False)
        