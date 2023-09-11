
from typing import Union, List


# The design of this class is to have
class Entry:
    def __init__(self, id: int, rounding_by: float = 0.05):
        self.id = id
        self.rounding_by = rounding_by
        self.total_tax: Union[float, None] = None
        self.total_price: Union[float, None] = None
        self.tax_id: Union[int, None] = None
        self.product_id: Union[int, None] = None


class Entries:
    def __init__(self, ):
        self._data: Union[Entry, None] = None


class EntryManager:
    """docstring for EntryManager."""

    table_name = "entries"

    def __init__(self, db):
        self.db = db

    def get_all(self):
        return self.db[self.table_name]

    def get_input_props(self, keys: List[str]):
        return {k: list(self.db[k].values()) for k in keys}

    # def insert(self, id: int, ):
    #     if not id:
    #         entries: Union[Entry, None] = list(self.get_all().keys())
    #         if bool(entries):
    #             id = entries[-1]

    #     return EntrySmart(entry)
