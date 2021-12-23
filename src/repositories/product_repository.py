from database_connection import get_database_connection
from model.product_model import Product

def get_product_by_row(row):
    return Product(
    row['product_name'], row['product_category'], row['product_QR'], 
    row['product_quantity'])

class ProductRepository:
    """Class ProductRepository interact with tale products in database.
    """

    def __init__(self, connection):
        """Class initializer creating new instance of type ProductRepository

        Args:
            connection: database connection as an argument
        """
        self._db_connection = connection

    def find_products_by_category(self, category):
        """Find all products by category from database.

        Args:
            category: name of the category
        Returns: List of all available products with correct category name
        """
        cursor = self._db_connection.cursor()
        cursor.execute("SELECT * FROM products WHERE product_category=?", (category, ))
        rows = cursor.fetchall()
        
        return list(map(self.__get_product_by_row, rows))

    def find_product(self, value):
        """Finds a specific product

        Args:
            value : product name or product QR-code

        Returns: On success returns product itself, otherwise returns False
        """
        cursor = self._db_connection.cursor()
        cursor.execute("SELECT * FROM products WHERE product_name=? OR product_QR=?", (value, value))
        row = cursor.fetchone()
        if not row:
            return False
        
        return self.__get_product_by_row(row)

    def add_new_product(self, product):
        """add a new product to the database

        Args:
            product: an instance of Product class

        Returns: True
        """
        cursor = self._db_connection.cursor()
        cursor.execute("INSERT INTO products VALUES (?, ?, ?, ?)",
        (product.product_name, product.product_category, product.product_qr_code, 
        product.product_quantity))

        self._db_connection.commit()
        return True

    def __get_product_by_row(self, row):
        return Product(row['product_name'], row['product_category'], 
        row['product_QR'], row['product_quantity'])

product_repositories = ProductRepository(get_database_connection())
