from model.product_model import Product
from repositories.product_repository import product_repositories

class ImportServices:
    def __init__(self):
        pass

    def save_product(self, name, category, qr_code, quantity):
        productObj = Product(name, category, qr_code, quantity)
        operation = product_repositories.add_new_product(productObj)
        if operation:
            return True
        return False

