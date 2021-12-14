from model.product_model import Product
from repositories.product_repository import product_repositories
from repositories.cage_repository import cage_repository

class ImportServices:
    """ ImportServices class takes control over product's insertion and creating
        new cages to the warehouse
    """


    def save_product(self, name, category, qr_code, quantity):
        """Add new product to the warehouse

        Args:
            name (str): name of the product
            category (str): category of the product
            qr_code (str): unique product specific code
            quantity (int): amount of the product in warehouse

        Returns:
            bool: True, if product added successfully, otherwise False
        """
        product_obj = Product(name, category, qr_code, quantity)
        operation = product_repositories.add_new_product(product_obj)
        if operation:
            return True
        return False


    def save_category(self, name):
        """Add new cage to the warehouse

        Args:
            name (str): name the cage

        Returns:
            bool: True, if cage has been added successfully, otherwise False
        """
        result = cage_repository.insert_new_category(name)
        if not result:
            return False
        return True
