from dataclasses import (
    dataclass
)
from typing import (
    Literal
)
from cdp.domains.target.types import (
    TargetID
)

RegistrationID = str

ServiceWorkerVersionRunningStatus = Literal[
    "stopped",
    "starting",
    "running",
    "stopping"
]

ServiceWorkerVersionStatus = Literal[
    "new",
    "installing",
    "installed",
    "activating",
    "activated",
    "redundant"
]


@dataclass
class ServiceWorkerRegistration:
    registration_id: "RegistrationID"
    scope_url: str
    is_deleted: bool


@dataclass
class ServiceWorkerVersion:
    version_id: str
    registration_id: "RegistrationID"
    script_url: str
    running_status: "ServiceWorkerVersionRunningStatus"
    status: "ServiceWorkerVersionStatus"
    script_last_modified: float
    script_response_time: float
    controlled_clients: list
    target_id: "TargetID"


@dataclass
class ServiceWorkerErrorMessage:
    error_message: str
    registration_id: "RegistrationID"
    version_id: str
    source_url: str
    line_number: int
    column_number: int