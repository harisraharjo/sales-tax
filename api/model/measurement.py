# from typing import Union, NamedTuple
from api.model.shared import BaseClass


class Measurement(BaseClass):
    def __init__(self, id: int, name: str):
        super().__init__(id, name)
