import unittest
from services.storage_services import Storage
from services.import_services import ImportServices

class TestStorageServices(unittest.TestCase):
    def setUp(self):
        self._storage_object = Storage()


    def test_correct_category_finds_products(self):
        productList = self._storage_object.get_stored_products("Puhelimet")
        self.assertGreater(len(productList), 0)

        