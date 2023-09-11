
from typing import Union, List


'''
This class is designed to acept any input from the user.
This class's job is to point to other class. 
With this, we can have flexible behaviours such as get all entries that uses X rule.
'''


class Entry:
    def __init__(self, id: int, total_tax: float,
                 total_price: float,
                 tax_id: int,
                 product_id: int,  rule_id: int):
        self.id = id
        self.total_tax = total_tax
        self.total_price = total_price
        self.tax_id = tax_id
        self.product_id = product_id
        self.rule_id: rule_id


'''
This class cannot be created from initialization.-
because an entry data can only be created from the POST entries endpoint. 
We need to calculate the data first before storing the value.
'''


class Entries:
    def __init__(self):
        self._data: Union[Entry, None] = None

    def add(self, total_tax: float,
            total_price: float,
            tax_id: int,
            product_id: int,  rule_id: int):
        pass


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
