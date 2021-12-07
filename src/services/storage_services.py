from repositories.cage_repository import cage_repository
from repositories.product_repository import product_repositories

class Storage:
    def __init__(self):
        self._product_repository = product_repositories
        self._cage_repository = cage_repository

    def get_cages(self):
        return self._cage_repository.get_cages()

    def get_stored_products(self, category):
        return self._product_repository.find_products_by_category(category)

    def search_product(self, value):
        result = self._product_repository.find_product(value)
        if not result:
            return False
        return result