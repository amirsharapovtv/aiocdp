from dataclasses import (
    dataclass
)
from typing import (
    Literal
)
from cdp.domains.network.types import (
    ClientSecurityState,
    CorsErrorStatus,
    IPAddressSpace,
    LoaderId,
    RequestId
)
from cdp.domains.page.types import (
    FrameId
)
from cdp.domains.runtime.types import (
    ScriptId
)
from cdp.domains.dom.types import (
    BackendNodeId
)

IssueId = str

CookieExclusionReason = Literal[
    "ExcludeSameSiteUnspecifiedTreatedAsLax",
    "ExcludeSameSiteNoneInsecure",
    "ExcludeSameSiteLax",
    "ExcludeSameSiteStrict",
    "ExcludeInvalidSameParty",
    "ExcludeSamePartyCrossPartyContext",
    "ExcludeDomainNonASCII",
    "ExcludeThirdPartyCookieBlockedInFirstPartySet",
    "ExcludeThirdPartyPhaseout"
]

CookieWarningReason = Literal[
    "WarnSameSiteUnspecifiedCrossSiteContext",
    "WarnSameSiteNoneInsecure",
    "WarnSameSiteUnspecifiedLaxAllowUnsafe",
    "WarnSameSiteStrictLaxDowngradeStrict",
    "WarnSameSiteStrictCrossDowngradeStrict",
    "WarnSameSiteStrictCrossDowngradeLax",
    "WarnSameSiteLaxCrossDowngradeStrict",
    "WarnSameSiteLaxCrossDowngradeLax",
    "WarnAttributeValueExceedsMaxSize",
    "WarnDomainNonASCII",
    "WarnThirdPartyPhaseout"
]

CookieOperation = Literal[
    "SetCookie",
    "ReadCookie"
]

MixedContentResolutionStatus = Literal[
    "MixedContentBlocked",
    "MixedContentAutomaticallyUpgraded",
    "MixedContentWarning"
]

MixedContentResourceType = Literal[
    "AttributionSrc",
    "Audio",
    "Beacon",
    "CSPReport",
    "Download",
    "EventSource",
    "Favicon",
    "Font",
    "Form",
    "Frame",
    "Image",
    "Import",
    "Manifest",
    "Ping",
    "PluginData",
    "PluginResource",
    "Prefetch",
    "Resource",
    "Script",
    "ServiceWorker",
    "SharedWorker",
    "Stylesheet",
    "Track",
    "Video",
    "Worker",
    "XMLHttpRequest",
    "XSLT"
]

BlockedByResponseReason = Literal[
    "CoepFrameResourceNeedsCoepHeader",
    "CoopSandboxedIFrameCannotNavigateToCoopPage",
    "CorpNotSameOrigin",
    "CorpNotSameOriginAfterDefaultedToSameOriginByCoep",
    "CorpNotSameSite"
]

HeavyAdResolutionStatus = Literal[
    "HeavyAdBlocked",
    "HeavyAdWarning"
]

HeavyAdReason = Literal[
    "NetworkTotalLimit",
    "CpuTotalLimit",
    "CpuPeakLimit"
]

ContentSecurityPolicyViolationType = Literal[
    "kInlineViolation",
    "kEvalViolation",
    "kURLViolation",
    "kTrustedTypesSinkViolation",
    "kTrustedTypesPolicyViolation",
    "kWasmEvalViolation"
]

SharedArrayBufferIssueType = Literal[
    "TransferIssue",
    "CreationIssue"
]

AttributionReportingIssueType = Literal[
    "PermissionPolicyDisabled",
    "UntrustworthyReportingOrigin",
    "InsecureContext",
    "InvalidHeader",
    "InvalidRegisterTriggerHeader",
    "SourceAndTriggerHeaders",
    "SourceIgnored",
    "TriggerIgnored",
    "OsSourceIgnored",
    "OsTriggerIgnored",
    "InvalidRegisterOsSourceHeader",
    "InvalidRegisterOsTriggerHeader",
    "WebAndOsHeaders",
    "NoWebOrOsSupport",
    "NavigationRegistrationWithoutTransientUserActivation"
]

GenericIssueErrorType = Literal[
    "CrossOriginPortalPostMessageError",
    "FormLabelForNameError",
    "FormDuplicateIdForInputError",
    "FormInputWithNoLabelError",
    "FormAutocompleteAttributeEmptyError",
    "FormEmptyIdAndNameAttributesForInputError",
    "FormAriaLabelledByToNonExistingId",
    "FormInputAssignedAutocompleteValueToIdOrNameAttributeError",
    "FormLabelHasNeitherForNorNestedInput",
    "FormLabelForMatchesNonExistingIdError",
    "FormInputHasWrongButWellIntendedAutocompleteValueError",
    "ResponseWasBlockedByORB"
]

ClientHintIssueReason = Literal[
    "MetaTagAllowListInvalidOrigin",
    "MetaTagModifiedHTML"
]

FederatedAuthRequestIssueReason = Literal[
    "ShouldEmbargo",
    "TooManyRequests",
    "WellKnownHttpNotFound",
    "WellKnownNoResponse",
    "WellKnownInvalidResponse",
    "WellKnownListEmpty",
    "WellKnownInvalidContentType",
    "ConfigNotInWellKnown",
    "WellKnownTooBig",
    "ConfigHttpNotFound",
    "ConfigNoResponse",
    "ConfigInvalidResponse",
    "ConfigInvalidContentType",
    "ClientMetadataHttpNotFound",
    "ClientMetadataNoResponse",
    "ClientMetadataInvalidResponse",
    "ClientMetadataInvalidContentType",
    "DisabledInSettings",
    "ErrorFetchingSignin",
    "InvalidSigninResponse",
    "AccountsHttpNotFound",
    "AccountsNoResponse",
    "AccountsInvalidResponse",
    "AccountsListEmpty",
    "AccountsInvalidContentType",
    "IdTokenHttpNotFound",
    "IdTokenNoResponse",
    "IdTokenInvalidResponse",
    "IdTokenInvalidRequest",
    "IdTokenInvalidContentType",
    "ErrorIdToken",
    "Canceled",
    "RpPageNotVisible",
    "SilentMediationFailure",
    "ThirdPartyCookiesBlocked"
]

FederatedAuthUserInfoRequestIssueReason = Literal[
    "NotSameOrigin",
    "NotIframe",
    "NotPotentiallyTrustworthy",
    "NoApiPermission",
    "NotSignedInWithIdp",
    "NoAccountSharingPermission",
    "InvalidConfigOrWellKnown",
    "InvalidAccountsResponse",
    "NoReturningUserFromFetchedAccounts"
]

StyleSheetLoadingIssueReason = Literal[
    "LateImportRule",
    "RequestFailed"
]

InspectorIssueCode = Literal[
    "CookieIssue",
    "MixedContentIssue",
    "BlockedByResponseIssue",
    "HeavyAdIssue",
    "ContentSecurityPolicyIssue",
    "SharedArrayBufferIssue",
    "LowTextContrastIssue",
    "CorsIssue",
    "AttributionReportingIssue",
    "QuirksModeIssue",
    "NavigatorUserAgentIssue",
    "GenericIssue",
    "DeprecationIssue",
    "ClientHintIssue",
    "FederatedAuthRequestIssue",
    "BounceTrackingIssue",
    "StylesheetLoadingIssue",
    "FederatedAuthUserInfoRequestIssue"
]


@dataclass
class AffectedCookie:
    name: str
    path: str
    domain: str


@dataclass
class AffectedRequest:
    request_id: "RequestId"
    url: str


@dataclass
class AffectedFrame:
    frame_id: "FrameId"


@dataclass
class CookieIssueDetails:
    cookie: "AffectedCookie"
    raw_cookie_line: str
    cookie_warning_reasons: list
    cookie_exclusion_reasons: list
    operation: "CookieOperation"
    site_for_cookies: str
    cookie_url: str
    request: "AffectedRequest"


@dataclass
class MixedContentIssueDetails:
    resource_type: "MixedContentResourceType"
    resolution_status: "MixedContentResolutionStatus"
    insecure_url: str
    main_resource_url: str
    request: "AffectedRequest"
    frame: "AffectedFrame"


@dataclass
class BlockedByResponseIssueDetails:
    request: "AffectedRequest"
    parent_frame: "AffectedFrame"
    blocked_frame: "AffectedFrame"
    reason: "BlockedByResponseReason"


@dataclass
class HeavyAdIssueDetails:
    resolution: "HeavyAdResolutionStatus"
    reason: "HeavyAdReason"
    frame: "AffectedFrame"


@dataclass
class SourceCodeLocation:
    script_id: "ScriptId"
    url: str
    line_number: int
    column_number: int


@dataclass
class ContentSecurityPolicyIssueDetails:
    blocked_url: str
    violated_directive: str
    is_report_only: bool
    content_security_policy_violation_type: "ContentSecurityPolicyViolationType"
    frame_ancestor: "AffectedFrame"
    source_code_location: "SourceCodeLocation"
    violating_node_id: "BackendNodeId"


@dataclass
class SharedArrayBufferIssueDetails:
    source_code_location: "SourceCodeLocation"
    is_warning: bool
    type: "SharedArrayBufferIssueType"


@dataclass
class LowTextContrastIssueDetails:
    violating_node_id: "BackendNodeId"
    violating_node_selector: str
    contrast_ratio: float
    threshold_aa: float
    threshold_aaa: float
    font_size: str
    font_weight: str


@dataclass
class CorsIssueDetails:
    cors_error_status: "CorsErrorStatus"
    is_warning: bool
    request: "AffectedRequest"
    location: "SourceCodeLocation"
    initiator_origin: str
    resource_ip_address_space: "IPAddressSpace"
    client_security_state: "ClientSecurityState"


@dataclass
class AttributionReportingIssueDetails:
    violation_type: "AttributionReportingIssueType"
    request: "AffectedRequest"
    violating_node_id: "BackendNodeId"
    invalid_parameter: str


@dataclass
class QuirksModeIssueDetails:
    is_limited_quirks_mode: bool
    document_node_id: "BackendNodeId"
    url: str
    frame_id: "FrameId"
    loader_id: "LoaderId"


@dataclass
class NavigatorUserAgentIssueDetails:
    url: str
    location: "SourceCodeLocation"


@dataclass
class GenericIssueDetails:
    error_type: "GenericIssueErrorType"
    frame_id: "FrameId"
    violating_node_id: "BackendNodeId"
    violating_node_attribute: str
    request: "AffectedRequest"


@dataclass
class DeprecationIssueDetails:
    affected_frame: "AffectedFrame"
    source_code_location: "SourceCodeLocation"
    type: str


@dataclass
class BounceTrackingIssueDetails:
    tracking_sites: list


@dataclass
class FederatedAuthRequestIssueDetails:
    federated_auth_request_issue_reason: "FederatedAuthRequestIssueReason"


@dataclass
class FederatedAuthUserInfoRequestIssueDetails:
    federated_auth_user_info_request_issue_reason: "FederatedAuthUserInfoRequestIssueReason"


@dataclass
class ClientHintIssueDetails:
    source_code_location: "SourceCodeLocation"
    client_hint_issue_reason: "ClientHintIssueReason"


@dataclass
class FailedRequestInfo:
    url: str
    failure_message: str
    request_id: "RequestId"


@dataclass
class StylesheetLoadingIssueDetails:
    source_code_location: "SourceCodeLocation"
    style_sheet_loading_issue_reason: "StyleSheetLoadingIssueReason"
    failed_request_info: "FailedRequestInfo"


@dataclass
class InspectorIssueDetails:
    cookie_issue_details: "CookieIssueDetails"
    mixed_content_issue_details: "MixedContentIssueDetails"
    blocked_by_response_issue_details: "BlockedByResponseIssueDetails"
    heavy_ad_issue_details: "HeavyAdIssueDetails"
    content_security_policy_issue_details: "ContentSecurityPolicyIssueDetails"
    shared_array_buffer_issue_details: "SharedArrayBufferIssueDetails"
    low_text_contrast_issue_details: "LowTextContrastIssueDetails"
    cors_issue_details: "CorsIssueDetails"
    attribution_reporting_issue_details: "AttributionReportingIssueDetails"
    quirks_mode_issue_details: "QuirksModeIssueDetails"
    navigator_user_agent_issue_details: "NavigatorUserAgentIssueDetails"
    generic_issue_details: "GenericIssueDetails"
    deprecation_issue_details: "DeprecationIssueDetails"
    client_hint_issue_details: "ClientHintIssueDetails"
    federated_auth_request_issue_details: "FederatedAuthRequestIssueDetails"
    bounce_tracking_issue_details: "BounceTrackingIssueDetails"
    stylesheet_loading_issue_details: "StylesheetLoadingIssueDetails"
    federated_auth_user_info_request_issue_details: "FederatedAuthUserInfoRequestIssueDetails"


@dataclass
class InspectorIssue:
    code: "InspectorIssueCode"
    details: "InspectorIssueDetails"
    issue_id: "IssueId"
