from dataclasses import (
    dataclass
)
from cdp.domains.runtime.types import (
    CallArgument,
    ExceptionDetails,
    RemoteObject,
    RemoteObjectId,
    ScriptId,
    StackTrace,
    StackTraceId,
    TimeDelta,
    UniqueDebuggerId
)

BreakpointId = str

CallFrameId = str


@dataclass
class Location:
    script_id: "ScriptId"
    line_number: int
    column_number: int


@dataclass
class ScriptPosition:
    line_number: int
    column_number: int


@dataclass
class CallFrame:
    call_frame_id: "CallFrameId"
    function_name: str
    function_location: "Location"
    location: "Location"
    url: str
    scope_chain: list
    this: "RemoteObject"
    return_value: "RemoteObject"


@dataclass
class Scope:
    type: str
    object: "RemoteObject"
    name: str
    start_location: "Location"
    end_location: "Location"


@dataclass
class SearchMatch:
    line_number: float
    line_content: str


@dataclass
class BreakLocation:
    script_id: "ScriptId"
    line_number: int
    column_number: int
    type: str


@dataclass
class EnableReturnT:
    debugger_id: "UniqueDebuggerId"


@dataclass
class EvaluateOnCallFrameReturnT:
    result: "RemoteObject"
    exception_details: "ExceptionDetails"


@dataclass
class GetPossibleBreakpointsReturnT:
    locations: list


@dataclass
class GetScriptSourceReturnT:
    script_source: str


@dataclass
class GetStackTraceReturnT:
    stack_trace: "StackTrace"


@dataclass
class RestartFrameReturnT:
    call_frames: list
    async_stack_trace: "StackTrace"
    async_stack_trace_id: "StackTraceId"


@dataclass
class SearchInContentReturnT:
    result: list


@dataclass
class SetBreakpointReturnT:
    breakpoint_id: "BreakpointId"
    actual_location: "Location"


@dataclass
class SetInstrumentationBreakpointReturnT:
    breakpoint_id: "BreakpointId"


@dataclass
class SetBreakpointByUrlReturnT:
    breakpoint_id: "BreakpointId"
    locations: list


@dataclass
class SetBreakpointOnFunctionCallReturnT:
    breakpoint_id: "BreakpointId"


@dataclass
class SetScriptSourceReturnT:
    call_frames: list
    stack_changed: bool
    async_stack_trace: "StackTrace"
    async_stack_trace_id: "StackTraceId"
    exception_details: "ExceptionDetails"