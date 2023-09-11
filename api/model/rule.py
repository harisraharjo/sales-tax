from .shared import BaseClass
import math


'''
To create a generic rule.
This way it's possible if we want to change the rounding_by value.
we can even also add more things that can manage the entries or tax calculations
'''


class Rule(BaseClass):
    """docstring for Rule."""

    def __init__(self, id: int, name: str, rounding_by=0.05, ):
        super().__init__(id, name)
        self.rounding_by = rounding_by


class RuleSmart:
    """docstring for RuleSmart."""

    def __init__(self, rule: Rule):
        self._data = rule

    def round_to_nearest_float(self, value: float):
        rounding_by = self._data.rounding_by
        return math.ceil(value / rounding_by) * rounding_by


class RuleManager:
    """docstring for RuleManager."""

    table_name = "rules"

    def __init__(self, db):
        self.db = db

    def get(self, id: int):
        rule: Rule = self.db[self.table_name][id]

        return RuleSmart(rule)
