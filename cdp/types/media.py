# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.

from typing import (
    TypedDict
)

PlayerId = str

Timestamp = float


class PlayerMessage(TypedDict):
    level: str
    message: str


class PlayerProperty(TypedDict):
    name: str
    value: str


class PlayerEvent(TypedDict):
    timestamp: 'Timestamp'
    value: str


class PlayerErrorSourceLocation(TypedDict):
    file: str
    line: int


class PlayerError(TypedDict):
    errorType: str
    code: int
    stack: list
    cause: list
    data: dict
