from dataclasses import (
    dataclass
)
from cdp.domains.base import (
    BaseDomain
)
from cdp.utils import (
    is_defined,
    MaybeUndefined,
    UNDEFINED
)
from cdp.domains.storage.types import (
    StorageType,
    SharedStorageAccessType,
    SharedStorageAccessParams,
    StorageBucketInfo,
    AttributionReportingSourceRegistrationResult,
    InterestGroupAccessType,
    SignedInt64AsBase10,
    StorageBucketsDurability,
    AttributionReportingSourceType,
    AttributionReportingEventReportWindows,
    UnsignedInt64AsBase10,
    StorageBucket,
    InterestGroupDetails,
    SerializedStorageKey,
    AttributionReportingSourceRegistration,
    UnsignedInt128AsBase16,
    SharedStorageMetadata
)
from cdp.domains.network.types import (
    TimeSinceEpoch
)
from cdp.domains.page.types import (
    FrameId
)
from cdp.domains.browser.types import (
    BrowserContextID
)


@dataclass
class Storage(BaseDomain):
    def get_storage_key_for_frame(
        self,
        frame_id: FrameId
    ):
        params = {
            "frameId": frame_id,
        }

        return self._send_command(
            "Storage.getStorageKeyForFrame",
            params
        )

    def clear_data_for_origin(
        self,
        origin: str,
        storage_types: str
    ):
        params = {
            "origin": origin,
            "storageTypes": storage_types,
        }

        return self._send_command(
            "Storage.clearDataForOrigin",
            params
        )

    def clear_data_for_storage_key(
        self,
        storage_key: str,
        storage_types: str
    ):
        params = {
            "storageKey": storage_key,
            "storageTypes": storage_types,
        }

        return self._send_command(
            "Storage.clearDataForStorageKey",
            params
        )

    def get_cookies(
        self,
        browser_context_id: MaybeUndefined[]
    ):
        params = {}

        if is_defined(
            browser_context_id
        ):
            params[] = browser_context_id

        return self._send_command(
            "Storage.getCookies",
            params
        )

    def set_cookies(
        self,
        cookies: list,
        browser_context_id: MaybeUndefined[]
    ):
        params = {
            "cookies": cookies,
        }

        if is_defined(
            browser_context_id
        ):
            params[] = browser_context_id

        return self._send_command(
            "Storage.setCookies",
            params
        )

    def clear_cookies(
        self,
        browser_context_id: MaybeUndefined[]
    ):
        params = {}

        if is_defined(
            browser_context_id
        ):
            params[] = browser_context_id

        return self._send_command(
            "Storage.clearCookies",
            params
        )

    def get_usage_and_quota(
        self,
        origin: str
    ):
        params = {
            "origin": origin,
        }

        return self._send_command(
            "Storage.getUsageAndQuota",
            params
        )

    def override_quota_for_origin(
        self,
        origin: str,
        quota_size: MaybeUndefined[]
    ):
        params = {
            "origin": origin,
        }

        if is_defined(
            quota_size
        ):
            params[] = quota_size

        return self._send_command(
            "Storage.overrideQuotaForOrigin",
            params
        )

    def track_cache_storage_for_origin(
        self,
        origin: str
    ):
        params = {
            "origin": origin,
        }

        return self._send_command(
            "Storage.trackCacheStorageForOrigin",
            params
        )

    def track_cache_storage_for_storage_key(
        self,
        storage_key: str
    ):
        params = {
            "storageKey": storage_key,
        }

        return self._send_command(
            "Storage.trackCacheStorageForStorageKey",
            params
        )

    def track_indexed_db_for_origin(
        self,
        origin: str
    ):
        params = {
            "origin": origin,
        }

        return self._send_command(
            "Storage.trackIndexedDBForOrigin",
            params
        )

    def track_indexed_db_for_storage_key(
        self,
        storage_key: str
    ):
        params = {
            "storageKey": storage_key,
        }

        return self._send_command(
            "Storage.trackIndexedDBForStorageKey",
            params
        )

    def untrack_cache_storage_for_origin(
        self,
        origin: str
    ):
        params = {
            "origin": origin,
        }

        return self._send_command(
            "Storage.untrackCacheStorageForOrigin",
            params
        )

    def untrack_cache_storage_for_storage_key(
        self,
        storage_key: str
    ):
        params = {
            "storageKey": storage_key,
        }

        return self._send_command(
            "Storage.untrackCacheStorageForStorageKey",
            params
        )

    def untrack_indexed_db_for_origin(
        self,
        origin: str
    ):
        params = {
            "origin": origin,
        }

        return self._send_command(
            "Storage.untrackIndexedDBForOrigin",
            params
        )

    def untrack_indexed_db_for_storage_key(
        self,
        storage_key: str
    ):
        params = {
            "storageKey": storage_key,
        }

        return self._send_command(
            "Storage.untrackIndexedDBForStorageKey",
            params
        )

    def get_trust_tokens(
        self
    ):
        params = {}

        return self._send_command(
            "Storage.getTrustTokens",
            params
        )

    def clear_trust_tokens(
        self,
        issuer_origin: str
    ):
        params = {
            "issuerOrigin": issuer_origin,
        }

        return self._send_command(
            "Storage.clearTrustTokens",
            params
        )

    def get_interest_group_details(
        self,
        owner_origin: str,
        name: str
    ):
        params = {
            "ownerOrigin": owner_origin,
            "name": name,
        }

        return self._send_command(
            "Storage.getInterestGroupDetails",
            params
        )

    def set_interest_group_tracking(
        self,
        enable: bool
    ):
        params = {
            "enable": enable,
        }

        return self._send_command(
            "Storage.setInterestGroupTracking",
            params
        )

    def get_shared_storage_metadata(
        self,
        owner_origin: str
    ):
        params = {
            "ownerOrigin": owner_origin,
        }

        return self._send_command(
            "Storage.getSharedStorageMetadata",
            params
        )

    def get_shared_storage_entries(
        self,
        owner_origin: str
    ):
        params = {
            "ownerOrigin": owner_origin,
        }

        return self._send_command(
            "Storage.getSharedStorageEntries",
            params
        )

    def set_shared_storage_entry(
        self,
        owner_origin: str,
        key: str,
        value: str,
        ignore_if_present: MaybeUndefined[]
    ):
        params = {
            "ownerOrigin": owner_origin,
            "key": key,
            "value": value,
        }

        if is_defined(
            ignore_if_present
        ):
            params[] = ignore_if_present

        return self._send_command(
            "Storage.setSharedStorageEntry",
            params
        )

    def delete_shared_storage_entry(
        self,
        owner_origin: str,
        key: str
    ):
        params = {
            "ownerOrigin": owner_origin,
            "key": key,
        }

        return self._send_command(
            "Storage.deleteSharedStorageEntry",
            params
        )

    def clear_shared_storage_entries(
        self,
        owner_origin: str
    ):
        params = {
            "ownerOrigin": owner_origin,
        }

        return self._send_command(
            "Storage.clearSharedStorageEntries",
            params
        )

    def reset_shared_storage_budget(
        self,
        owner_origin: str
    ):
        params = {
            "ownerOrigin": owner_origin,
        }

        return self._send_command(
            "Storage.resetSharedStorageBudget",
            params
        )

    def set_shared_storage_tracking(
        self,
        enable: bool
    ):
        params = {
            "enable": enable,
        }

        return self._send_command(
            "Storage.setSharedStorageTracking",
            params
        )

    def set_storage_bucket_tracking(
        self,
        storage_key: str,
        enable: bool
    ):
        params = {
            "storageKey": storage_key,
            "enable": enable,
        }

        return self._send_command(
            "Storage.setStorageBucketTracking",
            params
        )

    def delete_storage_bucket(
        self,
        bucket: StorageBucket
    ):
        params = {
            "bucket": bucket,
        }

        return self._send_command(
            "Storage.deleteStorageBucket",
            params
        )

    def run_bounce_tracking_mitigations(
        self
    ):
        params = {}

        return self._send_command(
            "Storage.runBounceTrackingMitigations",
            params
        )

    def set_attribution_reporting_local_testing_mode(
        self,
        enabled: bool
    ):
        params = {
            "enabled": enabled,
        }

        return self._send_command(
            "Storage.setAttributionReportingLocalTestingMode",
            params
        )

    def set_attribution_reporting_tracking(
        self,
        enable: bool
    ):
        params = {
            "enable": enable,
        }

        return self._send_command(
            "Storage.setAttributionReportingTracking",
            params
        )

