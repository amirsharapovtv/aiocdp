# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.

from cdp.domains.runtime.types import (
    RemoteObjectId
)

StreamHandle = str


@dataclass
class ReadReturnT:
    base64_encoded: bool
    data: str
    eof: bool


@dataclass
class ResolveBlobReturnT:
    uuid: str
