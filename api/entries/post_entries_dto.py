from dataclasses import dataclass
from typing import List
from typing import Union


'''
This class is designed to establish contract between client and the API endpoint.
With this, we can make the endpoint easy to change and also more safe.
'''


@dataclass(frozen=True, order=True)
class PostEntriesInputDTO:
    """docstring for PostEntriesInputDTO."""

    prices: List[float]
    amounts: List[int]
    product_names: List[str]
    tax_types: List[Union[int, None]]
    product_types: List[int]
    measurement_types: List[int]


@dataclass(frozen=True, order=True)
class PostEntriesOutputDTO:
    """docstring for PostEntriesOutputDTO."""

    prices: List[float]
    total_tax: float
    total_price: float
