from repositories.cage_repository import cage_repository
from repositories.product_repository import product_repositories

class Storage:
    """Storage class acts as a container for available products and cages.
       offers searching and getting operations on products and cages.

    Attributes:
        _product_repository: provide access to the product database
        __cage_repository: provide access to cage database
    """


    def __init__(self):
        """Class constructor create new storage object

        Attributes:
            _product_repository: provide access to the product database
            __cage_repository: provide access to cage database

        """
        self._product_repository = product_repositories
        self._cage_repository = cage_repository


    def get_cages(self):
        """Get all available cages

        Returns:
            [Cage]: List of all cages in warehouse
        """
        return self._cage_repository.get_cages()



    def get_stored_products(self, category):
        """Get all stored products from warehouse with category provided

        Args:
            category (str): Name of category to look its products

        Returns:
            [Product]: List of all avaiable products, if category exists, otherwise False
        """
        return self._product_repository.find_products_by_category(category)



    def search_product(self, value):
        """Find a specific product by provided name or Qr-code

        Args:
            value (str): Name or QR-code of product to be searched for

        Returns:
            Product: Product object, if operation successed, otherwise False
        """
        result = self._product_repository.find_product(value)
        if not result:
            return False
        return result
        