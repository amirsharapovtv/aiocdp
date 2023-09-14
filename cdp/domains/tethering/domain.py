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
class Tethering(BaseDomain):
    def bind(
        self,
        port: int
    ):
        params = {
            "port": port,
        }

        return self._send_command(
            "Tethering.bind",
            params
        )

    def unbind(
        self,
        port: int
    ):
        params = {
            "port": port,
        }

        return self._send_command(
            "Tethering.unbind",
            params
        )
