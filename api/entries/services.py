from .post_entries_dto import PostEntriesInputDTO
from typing import List
from ..model import TaxManager, RuleManager, EntryManager

'''
This class is designed to contain all the business logic in the entry domain.
With this, we can encapsulate the business logic.
'''


class EntriesService:
    """docstring for Taxes."""

    base_tax_id = 1

    def __init__(self, db,):
        self.db = db

    def get_input_props(self):
        keys = ["kinds", "measurements", "taxes"]

        input_props = EntryManager(self.db).get_input_props(keys)
        input_props["taxes"].pop(0)

        return input_props

        # return Mapper(GetEntriesDTO).to_dto(**data)

    def calculate(self, data: PostEntriesInputDTO, rule_id: int):
        _zip = zip(data.amounts, data.prices,
                   data.product_types, data.tax_types)

        tax_man = TaxManager(self.db)
        base_tax = tax_man.get(self.base_tax_id)
        prices: List[float] = []
        total_tax: float = 0.0
        total_price: float = 0.0

        rule = RuleManager(self.db).get(rule_id)

        for (quantity, price, kind_id, other_tax_id) in _zip:

            sales_tax = 0
            if not base_tax.is_whitelisted(kind_id):
                sales_tax += base_tax.calculate(quantity, price)

            # because right now there is only one type of other tax which is import
            if other_tax_id:
                sales_tax += tax_man.get(
                    other_tax_id).calculate(quantity, price)

            sales_tax = rule.round_to_nearest_float(sales_tax)

            price += sales_tax

            total_price += price
            total_tax += sales_tax

            prices.append(round(price, 2))

        return {
            "prices": prices,
            "total_tax": round(total_tax, 2),
            "total_price": round(total_price, 2)
        }
