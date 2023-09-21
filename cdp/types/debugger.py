# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.

from cdp.types import (
    runtime
)
from typing import (
    TypedDict
)

BreakpointId = str

CallFrameId = str


class Location(TypedDict):
    scriptId: 'runtime.ScriptId'
    lineNumber: int
    columnNumber: int


class ScriptPosition(TypedDict):
    lineNumber: int
    columnNumber: int


class CallFrame(TypedDict):
    callFrameId: 'CallFrameId'
    functionName: str
    location: 'Location'
    url: str
    scopeChain: list
    this: 'runtime.RemoteObject'
    functionLocation: 'Location'
    returnValue: 'runtime.RemoteObject'


class Scope(TypedDict):
    type: str
    object: 'runtime.RemoteObject'
    name: str
    startLocation: 'Location'
    endLocation: 'Location'


class SearchMatch(TypedDict):
    lineNumber: float
    lineContent: str


class BreakLocation(TypedDict):
    scriptId: 'runtime.ScriptId'
    lineNumber: int
    columnNumber: int
    type: str
