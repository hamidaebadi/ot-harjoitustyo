from model.product_model import Product
from repositories.product_repository import product_repositories

class ImportServices:
    def save_product(self, name, category, qr_code, quantity):
        product_obj = Product(name, category, qr_code, quantity)
        operation = product_repositories.add_new_product(product_obj)
        if operation:
            return True
        return False

