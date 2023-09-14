from dataclasses import (
    dataclass
)
from typing import (
    Literal
)
from cdp.domains.runtime.types import (
    ExecutionContextId,
    ScriptId,
    UniqueDebuggerId
)
from cdp.domains.network.types import (
    LoaderId,
    ResourceType,
    TimeSinceEpoch
)
from cdp.domains.dom.types import (
    Rect
)
from cdp.domains.io.types import (
    StreamHandle
)
from cdp.domains.emulation.types import (
    ScreenOrientation
)

FrameId = str

ScriptIdentifier = str

AdFrameType = Literal[
    "none",
    "child",
    "root"
]

AdFrameExplanation = Literal[
    "ParentIsAd",
    "CreatedByAdScript",
    "MatchedBlockingRule"
]

SecureContextType = Literal[
    "Secure",
    "SecureLocalhost",
    "InsecureScheme",
    "InsecureAncestor"
]

CrossOriginIsolatedContextType = Literal[
    "Isolated",
    "NotIsolated",
    "NotIsolatedFeatureDisabled"
]

GatedAPIFeatures = Literal[
    "SharedArrayBuffers",
    "SharedArrayBuffersTransferAllowed",
    "PerformanceMeasureMemory",
    "PerformanceProfile"
]

PermissionsPolicyFeature = Literal[
    "accelerometer",
    "ambient-light-sensor",
    "attribution-reporting",
    "autoplay",
    "bluetooth",
    "browsing-topics",
    "camera",
    "ch-dpr",
    "ch-device-memory",
    "ch-downlink",
    "ch-ect",
    "ch-prefers-color-scheme",
    "ch-prefers-reduced-motion",
    "ch-prefers-reduced-transparency",
    "ch-rtt",
    "ch-save-data",
    "ch-ua",
    "ch-ua-arch",
    "ch-ua-bitness",
    "ch-ua-platform",
    "ch-ua-model",
    "ch-ua-mobile",
    "ch-ua-form-factor",
    "ch-ua-full-version",
    "ch-ua-full-version-list",
    "ch-ua-platform-version",
    "ch-ua-wow64",
    "ch-viewport-height",
    "ch-viewport-width",
    "ch-width",
    "clipboard-read",
    "clipboard-write",
    "compute-pressure",
    "cross-origin-isolated",
    "direct-sockets",
    "display-capture",
    "document-domain",
    "encrypted-media",
    "execution-while-out-of-viewport",
    "execution-while-not-rendered",
    "focus-without-user-activation",
    "fullscreen",
    "frobulate",
    "gamepad",
    "geolocation",
    "gyroscope",
    "hid",
    "identity-credentials-get",
    "idle-detection",
    "interest-cohort",
    "join-ad-interest-group",
    "keyboard-map",
    "local-fonts",
    "magnetometer",
    "microphone",
    "midi",
    "otp-credentials",
    "payment",
    "picture-in-picture",
    "private-aggregation",
    "private-state-token-issuance",
    "private-state-token-redemption",
    "publickey-credentials-get",
    "run-ad-auction",
    "screen-wake-lock",
    "serial",
    "shared-autofill",
    "shared-storage",
    "shared-storage-select-url",
    "smart-card",
    "storage-access",
    "sync-xhr",
    "unload",
    "usb",
    "vertical-scroll",
    "web-share",
    "window-management",
    "window-placement",
    "xr-spatial-tracking"
]

PermissionsPolicyBlockReason = Literal[
    "Header",
    "IframeAttribute",
    "InFencedFrameTree",
    "InIsolatedApp"
]

OriginTrialTokenStatus = Literal[
    "Success",
    "NotSupported",
    "Insecure",
    "Expired",
    "WrongOrigin",
    "InvalidSignature",
    "Malformed",
    "WrongVersion",
    "FeatureDisabled",
    "TokenDisabled",
    "FeatureDisabledForUser",
    "UnknownTrial"
]

OriginTrialStatus = Literal[
    "Enabled",
    "ValidTokenNotProvided",
    "OSNotSupported",
    "TrialNotAllowed"
]

OriginTrialUsageRestriction = Literal[
    "None",
    "Subset"
]

TransitionType = Literal[
    "link",
    "typed",
    "address_bar",
    "auto_bookmark",
    "auto_subframe",
    "manual_subframe",
    "generated",
    "auto_toplevel",
    "form_submit",
    "reload",
    "keyword",
    "keyword_generated",
    "other"
]

DialogType = Literal[
    "alert",
    "confirm",
    "prompt",
    "beforeunload"
]

ClientNavigationReason = Literal[
    "formSubmissionGet",
    "formSubmissionPost",
    "httpHeaderRefresh",
    "scriptInitiated",
    "metaTagRefresh",
    "pageBlockInterstitial",
    "reload",
    "anchorClick"
]

ClientNavigationDisposition = Literal[
    "currentTab",
    "newTab",
    "newWindow",
    "download"
]

ReferrerPolicy = Literal[
    "noReferrer",
    "noReferrerWhenDowngrade",
    "origin",
    "originWhenCrossOrigin",
    "sameOrigin",
    "strictOrigin",
    "strictOriginWhenCrossOrigin",
    "unsafeUrl"
]

AutoResponseMode = Literal[
    "none",
    "autoAccept",
    "autoReject",
    "autoOptOut"
]

NavigationType = Literal[
    "Navigation",
    "BackForwardCacheRestore"
]

BackForwardCacheNotRestoredReason = Literal[
    "NotPrimaryMainFrame",
    "BackForwardCacheDisabled",
    "RelatedActiveContentsExist",
    "HTTPStatusNotOK",
    "SchemeNotHTTPOrHTTPS",
    "Loading",
    "WasGrantedMediaAccess",
    "DisableForRenderFrameHostCalled",
    "DomainNotAllowed",
    "HTTPMethodNotGET",
    "SubframeIsNavigating",
    "Timeout",
    "CacheLimit",
    "JavaScriptExecution",
    "RendererProcessKilled",
    "RendererProcessCrashed",
    "SchedulerTrackedFeatureUsed",
    "ConflictingBrowsingInstance",
    "CacheFlushed",
    "ServiceWorkerVersionActivation",
    "SessionRestored",
    "ServiceWorkerPostMessage",
    "EnteredBackForwardCacheBeforeServiceWorkerHostAdded",
    "RenderFrameHostReused_SameSite",
    "RenderFrameHostReused_CrossSite",
    "ServiceWorkerClaim",
    "IgnoreEventAndEvict",
    "HaveInnerContents",
    "TimeoutPuttingInCache",
    "BackForwardCacheDisabledByLowMemory",
    "BackForwardCacheDisabledByCommandLine",
    "NetworkRequestDatapipeDrainedAsBytesConsumer",
    "NetworkRequestRedirected",
    "NetworkRequestTimeout",
    "NetworkExceedsBufferLimit",
    "NavigationCancelledWhileRestoring",
    "NotMostRecentNavigationEntry",
    "BackForwardCacheDisabledForPrerender",
    "UserAgentOverrideDiffers",
    "ForegroundCacheLimit",
    "BrowsingInstanceNotSwapped",
    "BackForwardCacheDisabledForDelegate",
    "UnloadHandlerExistsInMainFrame",
    "UnloadHandlerExistsInSubFrame",
    "ServiceWorkerUnregistration",
    "CacheControlNoStore",
    "CacheControlNoStoreCookieModified",
    "CacheControlNoStoreHTTPOnlyCookieModified",
    "NoResponseHead",
    "Unknown",
    "ActivationNavigationsDisallowedForBug1234857",
    "ErrorDocument",
    "FencedFramesEmbedder",
    "CookieDisabled",
    "HTTPAuthRequired",
    "CookieFlushed",
    "WebSocket",
    "WebTransport",
    "WebRTC",
    "MainResourceHasCacheControlNoStore",
    "MainResourceHasCacheControlNoCache",
    "SubresourceHasCacheControlNoStore",
    "SubresourceHasCacheControlNoCache",
    "ContainsPlugins",
    "DocumentLoaded",
    "DedicatedWorkerOrWorklet",
    "OutstandingNetworkRequestOthers",
    "RequestedMIDIPermission",
    "RequestedAudioCapturePermission",
    "RequestedVideoCapturePermission",
    "RequestedBackForwardCacheBlockedSensors",
    "RequestedBackgroundWorkPermission",
    "BroadcastChannel",
    "WebXR",
    "SharedWorker",
    "WebLocks",
    "WebHID",
    "WebShare",
    "RequestedStorageAccessGrant",
    "WebNfc",
    "OutstandingNetworkRequestFetch",
    "OutstandingNetworkRequestXHR",
    "AppBanner",
    "Printing",
    "WebDatabase",
    "PictureInPicture",
    "Portal",
    "SpeechRecognizer",
    "IdleManager",
    "PaymentManager",
    "SpeechSynthesis",
    "KeyboardLock",
    "WebOTPService",
    "OutstandingNetworkRequestDirectSocket",
    "InjectedJavascript",
    "InjectedStyleSheet",
    "KeepaliveRequest",
    "IndexedDBEvent",
    "Dummy",
    "JsNetworkRequestReceivedCacheControlNoStoreResource",
    "WebRTCSticky",
    "WebTransportSticky",
    "WebSocketSticky",
    "ContentSecurityHandler",
    "ContentWebAuthenticationAPI",
    "ContentFileChooser",
    "ContentSerial",
    "ContentFileSystemAccess",
    "ContentMediaDevicesDispatcherHost",
    "ContentWebBluetooth",
    "ContentWebUSB",
    "ContentMediaSessionService",
    "ContentScreenReader",
    "EmbedderPopupBlockerTabHelper",
    "EmbedderSafeBrowsingTriggeredPopupBlocker",
    "EmbedderSafeBrowsingThreatDetails",
    "EmbedderAppBannerManager",
    "EmbedderDomDistillerViewerSource",
    "EmbedderDomDistillerSelfDeletingRequestDelegate",
    "EmbedderOomInterventionTabHelper",
    "EmbedderOfflinePage",
    "EmbedderChromePasswordManagerClientBindCredentialManager",
    "EmbedderPermissionRequestManager",
    "EmbedderModalDialog",
    "EmbedderExtensions",
    "EmbedderExtensionMessaging",
    "EmbedderExtensionMessagingForOpenPort",
    "EmbedderExtensionSentMessageToCachedFrame"
]

BackForwardCacheNotRestoredReasonType = Literal[
    "SupportPending",
    "PageSupportNeeded",
    "Circumstantial"
]


@dataclass
class AdFrameStatus:
    ad_frame_type: "AdFrameType"
    explanations: list


@dataclass
class AdScriptId:
    script_id: "ScriptId"
    debugger_id: "UniqueDebuggerId"


@dataclass
class PermissionsPolicyBlockLocator:
    frame_id: "FrameId"
    block_reason: "PermissionsPolicyBlockReason"


@dataclass
class PermissionsPolicyFeatureState:
    feature: "PermissionsPolicyFeature"
    allowed: bool
    locator: "PermissionsPolicyBlockLocator"


@dataclass
class OriginTrialToken:
    origin: str
    match_sub_domains: bool
    trial_name: str
    expiry_time: "TimeSinceEpoch"
    is_third_party: bool
    usage_restriction: "OriginTrialUsageRestriction"


@dataclass
class OriginTrialTokenWithStatus:
    raw_token_text: str
    parsed_token: "OriginTrialToken"
    status: "OriginTrialTokenStatus"


@dataclass
class OriginTrial:
    trial_name: str
    status: "OriginTrialStatus"
    tokens_with_status: list


@dataclass
class Frame:
    id: "FrameId"
    parent_id: "FrameId"
    loader_id: "LoaderId"
    name: str
    url: str
    url_fragment: str
    domain_and_registry: str
    security_origin: str
    mime_type: str
    unreachable_url: str
    ad_frame_status: "AdFrameStatus"
    secure_context_type: "SecureContextType"
    cross_origin_isolated_context_type: "CrossOriginIsolatedContextType"
    gated_api_features: list


@dataclass
class FrameResource:
    url: str
    type: "ResourceType"
    mime_type: str
    last_modified: "TimeSinceEpoch"
    content_size: float
    failed: bool
    canceled: bool


@dataclass
class FrameResourceTree:
    frame: "Frame"
    child_frames: list
    resources: list


@dataclass
class FrameTree:
    frame: "Frame"
    child_frames: list


@dataclass
class NavigationEntry:
    id: int
    url: str
    user_typed_url: str
    title: str
    transition_type: "TransitionType"


@dataclass
class ScreencastFrameMetadata:
    offset_top: float
    page_scale_factor: float
    device_width: float
    device_height: float
    scroll_offset_x: float
    scroll_offset_y: float
    timestamp: "TimeSinceEpoch"


@dataclass
class AppManifestError:
    message: str
    critical: int
    line: int
    column: int


@dataclass
class AppManifestParsedProperties:
    scope: str


@dataclass
class LayoutViewport:
    page_x: int
    page_y: int
    client_width: int
    client_height: int


@dataclass
class VisualViewport:
    offset_x: float
    offset_y: float
    page_x: float
    page_y: float
    client_width: float
    client_height: float
    scale: float
    zoom: float


@dataclass
class Viewport:
    x: float
    y: float
    width: float
    height: float
    scale: float


@dataclass
class FontFamilies:
    standard: str
    fixed: str
    serif: str
    sans_serif: str
    cursive: str
    fantasy: str
    math: str


@dataclass
class ScriptFontFamilies:
    script: str
    font_families: "FontFamilies"


@dataclass
class FontSizes:
    standard: int
    fixed: int


@dataclass
class InstallabilityErrorArgument:
    name: str
    value: str


@dataclass
class InstallabilityError:
    error_id: str
    error_arguments: list


@dataclass
class CompilationCacheParams:
    url: str
    eager: bool


@dataclass
class BackForwardCacheNotRestoredExplanation:
    type: "BackForwardCacheNotRestoredReasonType"
    reason: "BackForwardCacheNotRestoredReason"
    context: str


@dataclass
class BackForwardCacheNotRestoredExplanationTree:
    url: str
    explanations: list
    children: list


@dataclass
class AddScriptToEvaluateOnLoadReturnT:
    identifier: "ScriptIdentifier"


@dataclass
class AddScriptToEvaluateOnNewDocumentReturnT:
    identifier: "ScriptIdentifier"


@dataclass
class CaptureScreenshotReturnT:
    data: str


@dataclass
class CaptureSnapshotReturnT:
    data: str


@dataclass
class CreateIsolatedWorldReturnT:
    execution_context_id: "ExecutionContextId"


@dataclass
class GetAppManifestReturnT:
    url: str
    errors: list
    data: str
    parsed: "AppManifestParsedProperties"


@dataclass
class GetInstallabilityErrorsReturnT:
    installability_errors: list


@dataclass
class GetManifestIconsReturnT:
    primary_icon: str


@dataclass
class GetAppIdReturnT:
    app_id: str
    recommended_id: str


@dataclass
class GetAdScriptIdReturnT:
    ad_script_id: "AdScriptId"


@dataclass
class GetCookiesReturnT:
    cookies: list


@dataclass
class GetFrameTreeReturnT:
    frame_tree: "FrameTree"


@dataclass
class GetLayoutMetricsReturnT:
    layout_viewport: "LayoutViewport"
    visual_viewport: "VisualViewport"
    content_size: "Rect"
    css_layout_viewport: "LayoutViewport"
    css_visual_viewport: "VisualViewport"
    css_content_size: "Rect"


@dataclass
class GetNavigationHistoryReturnT:
    current_index: int
    entries: list


@dataclass
class GetResourceContentReturnT:
    content: str
    base64_encoded: bool


@dataclass
class GetResourceTreeReturnT:
    frame_tree: "FrameResourceTree"


@dataclass
class NavigateReturnT:
    frame_id: "FrameId"
    loader_id: "LoaderId"
    error_text: str


@dataclass
class PrintToPDFReturnT:
    data: str
    stream: "StreamHandle"


@dataclass
class SearchInResourceReturnT:
    result: list


@dataclass
class GetPermissionsPolicyStateReturnT:
    states: list


@dataclass
class GetOriginTrialsReturnT:
    origin_trials: list