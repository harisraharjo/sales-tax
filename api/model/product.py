from api.model.shared import BaseClass


class Kind(BaseClass):
    def __init__(self, id: int, name: str):
        super().__init__(id, name)


class Product:
    """docstring for Product."""

    def __init__(self, id: int, entry_id: int, product_id: int, name: str, price: float, meeasurement_id: int):
        self.id = id
        self.entry_id = entry_id
        self.product_id = product_id
        self.meeasurement_id = meeasurement_id
        self.name = name
        self.price = price


class ProductManager:
    """docstring for ProductManager."""

    table_name = "products"

    def __init__(self, db):
        self.db = db
