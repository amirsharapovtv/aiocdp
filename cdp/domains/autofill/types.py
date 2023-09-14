from dataclasses import (
    dataclass
)
from typing import (
    Literal
)

FillingStrategy = Literal[
    "autocompleteAttribute",
    "autofillInferred"
]


@dataclass
class CreditCard:
    number: str
    name: str
    expiry_month: str
    expiry_year: str
    cvc: str


@dataclass
class AddressField:
    name: str
    value: str


@dataclass
class AddressFields:
    fields: list


@dataclass
class Address:
    fields: list


@dataclass
class AddressUI:
    address_fields: list


@dataclass
class FilledField:
    html_type: str
    id: str
    name: str
    value: str
    autofill_type: str
    filling_strategy: "FillingStrategy"
