from .post_entries_dto import PostEntriesInputDTO
from typing import List
from ..model import TaxManager, RuleManager, EntryManager


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

        # list({ele for ele in test_dict if test_dict[ele]})
        # data["taxes"] = {k: data["taxes"] for k in keys}
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
            # print("\n->: ", quantity, price, kind_id, other_tax_id)
            # because right now there is only one type of other tax which is import

            sales_tax = 0
            if not base_tax.is_whitelisted(kind_id):
                # print("Calculate basic tax...")
                sales_tax += base_tax.calculate(quantity, price)

            if other_tax_id:
                # print("Calculate import tax...")
                sales_tax += tax_man.get(
                    other_tax_id).calculate(quantity, price)

            sales_tax = rule.round_to_nearest_float(sales_tax)
            print("Tax:", round(sales_tax, 2))

            price += sales_tax
            print("Price:", round(price, 2))

            total_price += price
            total_tax += sales_tax

            prices.append(round(price, 2))

        tup = total_tax, total_price

        print("priceys: ", prices)
        print("final tax: ", round(tup[0], 2))
        print("final price: ", round(tup[1], 2))

        return {
            "prices": prices,
            "total_tax": total_tax,
            "total_price": total_price
        }
