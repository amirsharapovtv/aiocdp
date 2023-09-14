from dataclasses import (
    dataclass
)
from typing import (
    Literal
)

PressureLevel = Literal[
    "moderate",
    "critical"
]


@dataclass
class SamplingProfileNode:
    size: float
    total: float
    stack: list


@dataclass
class SamplingProfile:
    samples: list
    modules: list


@dataclass
class Module:
    name: str
    uuid: str
    base_address: str
    size: float


@dataclass
class GetDOMCountersReturnT:
    documents: int
    nodes: int
    js_event_listeners: int


@dataclass
class GetAllTimeSamplingProfileReturnT:
    profile: "SamplingProfile"


@dataclass
class GetBrowserSamplingProfileReturnT:
    profile: "SamplingProfile"


@dataclass
class GetSamplingProfileReturnT:
    profile: "SamplingProfile"