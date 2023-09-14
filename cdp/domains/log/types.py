from dataclasses import (
    dataclass
)
from cdp.domains.runtime.types import (
    StackTrace,
    Timestamp
)
from cdp.domains.network.types import (
    RequestId
)


@dataclass
class LogEntry:
    source: str
    level: str
    text: str
    category: str
    timestamp: "Timestamp"
    url: str
    line_number: int
    stack_trace: "StackTrace"
    network_request_id: "RequestId"
    worker_id: str
    args: list


@dataclass
class ViolationSetting:
    name: str
    threshold: float
