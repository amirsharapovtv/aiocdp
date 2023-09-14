from dataclasses import (
    dataclass
)
from cdp.domains.network.types import (
    TimeSinceEpoch
)
from cdp.domains.dom.types import (
    BackendNodeId,
    Rect
)
from cdp.domains.page.types import (
    FrameId
)


@dataclass
class LargestContentfulPaint:
    render_time: "TimeSinceEpoch"
    load_time: "TimeSinceEpoch"
    size: float
    element_id: str
    url: str
    node_id: "BackendNodeId"


@dataclass
class LayoutShiftAttribution:
    previous_rect: "Rect"
    current_rect: "Rect"
    node_id: "BackendNodeId"


@dataclass
class LayoutShift:
    value: float
    had_recent_input: bool
    last_input_time: "TimeSinceEpoch"
    sources: list


@dataclass
class TimelineEvent:
    frame_id: "FrameId"
    type: str
    name: str
    time: "TimeSinceEpoch"
    duration: float
    lcp_details: "LargestContentfulPaint"
    layout_shift_details: "LayoutShift"