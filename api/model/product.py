from api.model.shared import BaseClass

'''
There are a lot of product types. (food, medicine, etc.)
This class makes it easier to create a new type of product types.
On the 'smart' representation of this class, we can add some behaviour such as create a discount for 'X' product type
'''


class Kind(BaseClass):
    def __init__(self, id: int, name: str):
        super().__init__(id, name)


'''
Because our application is built to accept entries from the user.- 
we can't really categorize each product like a proper class. What we can do-
instead is just to create a 'shadow' product that points from the entries class.

On the 'smart' representation of this class, we can add some behaviour such as get entries data with specific product id
'''


class Product:
    """docstring for Product."""

    def __init__(self, id: int, product_type_id: int, name: str, price: float, meeasurement_id: int):
        self.id = id
        self.product_type_id = product_type_id
        self.meeasurement_id = meeasurement_id
        self.name = name
        self.price = price


class ProductManager:
    """docstring for ProductManager."""

    table_name = "products"

    def __init__(self, db):
        self.db = db
