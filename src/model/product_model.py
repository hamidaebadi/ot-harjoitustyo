class Product:
    """
    Class Product defins a product object

    Attributes:
        product_name: product's name
        product_category: each product has a category
        product_qr_code: each product is identified by its unique QR code
        product_quantity: tells how many of a specific product is available
    """
    def __init__(self, name, category, qr_code, quantity):
        self.product_name = name
        self.product_category = category
        self.product_qr_code = qr_code
        self.product_quantity = quantity

    

