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
class Cast(BaseDomain):
    def enable(
            self,
            presentation_url: str = UNDEFINED
    ) -> IResult[None]:
        params = {}

        if is_defined(presentation_url):
            params['presentationUrl'] = presentation_url

        return self._send_command(
            'Cast.enable',
            params,
            False
        )

    def disable(
            self
    ) -> IResult[None]:
        params = {}

        return self._send_command(
            'Cast.disable',
            params,
            False
        )

    def set_sink_to_use(
            self,
            sink_name: str
    ) -> IResult[None]:
        params = {
            'sinkName': sink_name,
        }

        return self._send_command(
            'Cast.setSinkToUse',
            params,
            False
        )

    def start_desktop_mirroring(
            self,
            sink_name: str
    ) -> IResult[None]:
        params = {
            'sinkName': sink_name,
        }

        return self._send_command(
            'Cast.startDesktopMirroring',
            params,
            False
        )

    def start_tab_mirroring(
            self,
            sink_name: str
    ) -> IResult[None]:
        params = {
            'sinkName': sink_name,
        }

        return self._send_command(
            'Cast.startTabMirroring',
            params,
            False
        )

    def stop_casting(
            self,
            sink_name: str
    ) -> IResult[None]:
        params = {
            'sinkName': sink_name,
        }

        return self._send_command(
            'Cast.stopCasting',
            params,
            False
        )
