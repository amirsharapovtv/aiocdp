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
from cdp.domains.dom.types import (
    BackendNodeId
)
from cdp.domains.page.types import (
    FrameId
)
from cdp.domains.autofill.types import (
    CreditCard
)
from cdp.utils import (
    is_defined,
    UNDEFINED
)


@dataclass
class Autofill(BaseDomain):
    def trigger(
        self,
        field_id: BackendNodeId,
        frame_id: FrameId,
        card: CreditCard = UNDEFINED
    ):
        params = {
            "fieldId": field_id,
            "card": card,
        }

        if is_defined(
            frame_id
        ):
            params["frameId"] = frame_id

        return self._send_command(
            "Autofill.trigger",
            params
        )

    def set_addresses(
        self,
        addresses: list
    ):
        params = {
            "addresses": addresses,
        }

        return self._send_command(
            "Autofill.setAddresses",
            params
        )

    def disable(
        self
    ):
        params = {}

        return self._send_command(
            "Autofill.disable",
            params
        )

    def enable(
        self
    ):
        params = {}

        return self._send_command(
            "Autofill.enable",
            params
        )

