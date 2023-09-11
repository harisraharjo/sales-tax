# from typing import Union, NamedTuple
from api.model.shared import BaseClass

'''
There are a lot of measurement types. (bottle, cup, etc)
This class will make it easy to scale the types
With this, we can have flexible behaviours such as give discount to every product that has X measurement type.
'''


class Measurement(BaseClass):
    def __init__(self, id: int, name: str):
        super().__init__(id, name)
