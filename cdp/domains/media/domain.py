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


@dataclass
class Media(BaseDomain):
    def enable(
        self
    ):
        params = {}

        return self._send_command(
            "Media.enable",
            params
        )

    def disable(
        self
    ):
        params = {}

        return self._send_command(
            "Media.disable",
            params
        )

