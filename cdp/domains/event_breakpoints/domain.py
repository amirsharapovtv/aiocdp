# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.

from cdp.domains.base import (
    BaseDomain
)
from dataclasses import (
    dataclass
)
from cdp.utils import (
    is_defined,
    UNDEFINED
)
from typing import (
    TYPE_CHECKING
)
if TYPE_CHECKING:
    from cdp.target.connection import (
        IResult
    )


@dataclass
class EventBreakpoints(BaseDomain):
    def set_instrumentation_breakpoint(
            self,
            event_name: str
    ) -> IResult[None]:
        params = {
            'eventName': event_name,
        }

        return self._send_command(
            'EventBreakpoints.setInstrumentationBreakpoint',
            params,
            False
        )

    def remove_instrumentation_breakpoint(
            self,
            event_name: str
    ) -> IResult[None]:
        params = {
            'eventName': event_name,
        }

        return self._send_command(
            'EventBreakpoints.removeInstrumentationBreakpoint',
            params,
            False
        )
