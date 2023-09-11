from api.model.shared import BaseClass
from typing import List, Union

'''
There are a lot of Tax types. (Sales tax, duty tax, etc.)
This class makes it easier to create a new type of tax types.
On the 'smart' representation of this class, we can add some behaviour such as create a discount for 'X' tax
'''


class TaxType(BaseClass):
    """docstring for TaxType."""

    def __init__(self, id: int, name: str):
        super().__init__(id, name)


'''
Besides that there are a lot of Tax types, there is also a lot of variant in each of those types.
Ex: Sales Tax -> VAT, Excise, etc.
This class makes it easier to create a variant for each type.
'''


class Tax(BaseClass):

    def __init__(self, id: int, name: str, tax_type_id: int, rate: float, whitelist: Union[List[int], None] = None):
        super().__init__(id, name)
        self.type = tax_type_id
        self.rate = rate
        self.whitelist = whitelist


class TaxSmart:
    def __init__(self, tax: Tax):
        self._data = tax

    def is_whitelisted(self, kind_id: int):
        return bool(self._data.whitelist and (kind_id in self._data.whitelist))

    def calculate(self, quantity: int, price: float):
        return (self._data.rate * quantity * price) / 100


class TaxManager:
    """docstring for TaxManager."""

    table_name = "taxes"

    def __init__(self, db):
        self.db = db

    def get(self, id: int):
        tax: Tax = self.db[self.table_name][id]

        return TaxSmart(tax)
