from dataclasses import (
    dataclass
)
from typing import (
    Literal
)
from cdp.domains.target.types import (
    TargetID
)

BrowserContextID = str

WindowID = int

WindowState = Literal[
    "normal",
    "minimized",
    "maximized",
    "fullscreen"
]

PermissionType = Literal[
    "accessibilityEvents",
    "audioCapture",
    "backgroundSync",
    "backgroundFetch",
    "clipboardReadWrite",
    "clipboardSanitizedWrite",
    "displayCapture",
    "durableStorage",
    "flash",
    "geolocation",
    "idleDetection",
    "localFonts",
    "midi",
    "midiSysex",
    "nfc",
    "notifications",
    "paymentHandler",
    "periodicBackgroundSync",
    "protectedMediaIdentifier",
    "sensors",
    "storageAccess",
    "topLevelStorageAccess",
    "videoCapture",
    "videoCapturePanTiltZoom",
    "wakeLockScreen",
    "wakeLockSystem",
    "windowManagement"
]

PermissionSetting = Literal[
    "granted",
    "denied",
    "prompt"
]

BrowserCommandId = Literal[
    "openTabSearch",
    "closeTabSearch"
]


@dataclass
class Bounds:
    left: int
    top: int
    width: int
    height: int
    window_state: "WindowState"


@dataclass
class PermissionDescriptor:
    name: str
    sysex: bool
    user_visible_only: bool
    allow_without_sanitization: bool
    pan_tilt_zoom: bool


@dataclass
class Bucket:
    low: int
    high: int
    count: int


@dataclass
class Histogram:
    name: str
    sum: int
    count: int
    buckets: list


@dataclass
class GetVersionReturnT:
    protocol_version: str
    product: str
    revision: str
    user_agent: str
    js_version: str


@dataclass
class GetBrowserCommandLineReturnT:
    arguments: list


@dataclass
class GetHistogramsReturnT:
    histograms: list


@dataclass
class GetHistogramReturnT:
    histogram: "Histogram"


@dataclass
class GetWindowBoundsReturnT:
    bounds: "Bounds"


@dataclass
class GetWindowForTargetReturnT:
    window_id: "WindowID"
    bounds: "Bounds"