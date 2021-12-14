import unittest
from services.import_services import ImportServices

class TestImportServices(unittest.TestCase):
    def setUp(self):
        self._import_obj = ImportServices()

    def test_new_product_added_succeffully(self):
        result = self._import_obj.save_product("test", "puhelimet", "xxxx", 10)
        self.assertEqual(result, True)

    def test_new_category_added_successfully(self):
        result = self._import_obj.save_category("testCage")
        self.assertEqual(result, True)

    
