from dataclasses import (
    dataclass
)
from typing import (
    Literal
)
from cdp.domains.network.types import (
    TimeSinceEpoch
)

CertificateId = int

MixedContentType = Literal[
    "blockable",
    "optionally-blockable",
    "none"
]

SecurityState = Literal[
    "unknown",
    "neutral",
    "insecure",
    "secure",
    "info",
    "insecure-broken"
]

SafetyTipStatus = Literal[
    "badReputation",
    "lookalike"
]

CertificateErrorAction = Literal[
    "continue",
    "cancel"
]


@dataclass
class CertificateSecurityState:
    protocol: str
    key_exchange: str
    key_exchange_group: str
    cipher: str
    mac: str
    certificate: list
    subject_name: str
    issuer: str
    valid_from: "TimeSinceEpoch"
    valid_to: "TimeSinceEpoch"
    certificate_network_error: str
    certificate_has_weak_signature: bool
    certificate_has_sha1_signature: bool
    modern_ssl: bool
    obsolete_ssl_protocol: bool
    obsolete_ssl_key_exchange: bool
    obsolete_ssl_cipher: bool
    obsolete_ssl_signature: bool


@dataclass
class SafetyTipInfo:
    safety_tip_status: "SafetyTipStatus"
    safe_url: str


@dataclass
class VisibleSecurityState:
    security_state: "SecurityState"
    certificate_security_state: "CertificateSecurityState"
    safety_tip_info: "SafetyTipInfo"
    security_state_issue_ids: list


@dataclass
class SecurityStateExplanation:
    security_state: "SecurityState"
    title: str
    summary: str
    description: str
    mixed_content_type: "MixedContentType"
    certificate: list
    recommendations: list


@dataclass
class InsecureContentStatus:
    ran_mixed_content: bool
    displayed_mixed_content: bool
    contained_mixed_form: bool
    ran_content_with_cert_errors: bool
    displayed_content_with_cert_errors: bool
    ran_insecure_content_style: "SecurityState"
    displayed_insecure_content_style: "SecurityState"