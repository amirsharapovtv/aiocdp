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
from cdp.domains.dom_storage.types import (
    GetDOMStorageItemsReturnT,
    StorageId
)
if TYPE_CHECKING:
    from cdp.target.connection import (
        IResult
    )


@dataclass
class DOMStorage(BaseDomain):
    def clear(
            self,
            storage_id: StorageId
    ) -> IResult[None]:
        params = {
            'storageId': storage_id,
        }

        return self._send_command(
            'DOMStorage.clear',
            params,
            False
        )

    def disable(
            self
    ) -> IResult[None]:
        params = {}

        return self._send_command(
            'DOMStorage.disable',
            params,
            False
        )

    def enable(
            self
    ) -> IResult[None]:
        params = {}

        return self._send_command(
            'DOMStorage.enable',
            params,
            False
        )

    def get_dom_storage_items(
            self,
            storage_id: StorageId
    ) -> IResult['GetDOMStorageItemsReturnT']:
        params = {
            'storageId': storage_id,
        }

        return self._send_command(
            'DOMStorage.getDOMStorageItems',
            params,
            True
        )

    def remove_dom_storage_item(
            self,
            storage_id: StorageId,
            key: str
    ) -> IResult[None]:
        params = {
            'storageId': storage_id,
            'key': key,
        }

        return self._send_command(
            'DOMStorage.removeDOMStorageItem',
            params,
            False
        )

    def set_dom_storage_item(
            self,
            storage_id: StorageId,
            key: str,
            value: str
    ) -> IResult[None]:
        params = {
            'storageId': storage_id,
            'key': key,
            'value': value,
        }

        return self._send_command(
            'DOMStorage.setDOMStorageItem',
            params,
            False
        )
