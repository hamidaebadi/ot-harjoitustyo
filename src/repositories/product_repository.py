from database_connection import get_database_connection
from model.product_model import Product

def get_product_by_row(row):
    return Product(row['product_name'], row['product_category'], row['product_QR'], row['product_quantity'])

class ProductRepository:
    def __init__(self, connection):
        self._db_connection = connection

    def find_products_by_category(self, category):
        cursor = self._db_connection.cursor()
        cursor.execute("SELECT * FROM products WHERE product_category=?", (category, ))
        rows = cursor.fetchall()
        return list(map(get_product_by_row, rows))

    def find_product(self, value):
        cursor = self._db_connection.cursor()
        cursor.execute("SELECT * FROM products WHERE product_name=? OR product_QR=?", (value, value))
        row = cursor.fetchone()
        if not row:
            return False
        return get_product_by_row(row)

    def add_new_product(self, product=None):
        cursor = self._db_connection.cursor()
        cursor.execute("INSERT INTO products VALUES (?, ?, ?, ?)",
        (product.product_name,
        product.product_category, 
        product.product_qr_code, 
        product.product_quantity))

        self._db_connection.commit()

        return True

product_repositories = ProductRepository(get_database_connection())