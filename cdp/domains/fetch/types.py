# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.

from dataclasses import (
    dataclass
)
from typing import (
    TYPE_CHECKING
)
from typing import (
    Literal
)
from typing import (
    Any
)
if TYPE_CHECKING:
    from cdp.domains.network.types import (
        ErrorReason,
        ResourceType
    )
    from cdp.domains.io.types import (
        StreamHandle
    )

RequestId = str

RequestStage = Literal[
    'Request',
    'Response'
]


@dataclass
class RequestPattern:
    url_pattern: str
    resource_type: 'ResourceType'
    request_stage: 'RequestStage'


@dataclass
class HeaderEntry:
    name: str
    value: str


@dataclass
class AuthChallenge:
    source: str
    origin: str
    scheme: str
    realm: str


@dataclass
class AuthChallengeResponse:
    response: str
    username: str
    password: str


@dataclass
class GetResponseBodyReturnT:
    body: str
    base64_encoded: bool


@dataclass
class TakeResponseBodyAsStreamReturnT:
    stream: 'StreamHandle'
