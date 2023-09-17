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
from cdp.domains.mapper import (
    from_dict,
    to_dict
)
if TYPE_CHECKING:
    from cdp.target.connection import (
        IResponse
    )


@dataclass
class Media(BaseDomain):
    def enable(
            self
    ) -> IResponse[None]:
        params = {}

        return self._send_command(
            'Media.enable',
            params,
            False
        )

    def disable(
            self
    ) -> IResponse[None]:
        params = {}

        return self._send_command(
            'Media.disable',
            params,
            False
        )
