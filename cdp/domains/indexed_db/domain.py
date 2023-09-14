from cdp.domains.base import (
    BaseDomain
)
from dataclasses import (
    dataclass
)
from cdp.domains.storage.types import (
    StorageBucket
)
from cdp.domains.indexed_db.types import (
    DatabaseWithObjectStores,
    KeyRange
)
from cdp.utils import (
    is_defined,
    UNDEFINED
)


@dataclass
class IndexedDB(BaseDomain):
    def clear_object_store(
        self,
        security_origin: str,
        storage_key: str,
        storage_bucket: StorageBucket = UNDEFINED,
        database_name: str = UNDEFINED,
        object_store_name: str = UNDEFINED
    ):
        params = {
            "databaseName": database_name,
            "objectStoreName": object_store_name,
        }

        if is_defined(
            security_origin
        ):
            params["securityOrigin"] = security_origin

        if is_defined(
            storage_key
        ):
            params["storageKey"] = storage_key

        if is_defined(
            storage_bucket
        ):
            params["storageBucket"] = storage_bucket

        return self._send_command(
            "IndexedDB.clearObjectStore",
            params
        )

    def delete_database(
        self,
        security_origin: str,
        storage_key: str = UNDEFINED,
        storage_bucket: StorageBucket = UNDEFINED,
        database_name: str = UNDEFINED
    ):
        params = {
            "databaseName": database_name,
        }

        if is_defined(
            security_origin
        ):
            params["securityOrigin"] = security_origin

        if is_defined(
            storage_key
        ):
            params["storageKey"] = storage_key

        if is_defined(
            storage_bucket
        ):
            params["storageBucket"] = storage_bucket

        return self._send_command(
            "IndexedDB.deleteDatabase",
            params
        )

    def delete_object_store_entries(
        self,
        security_origin: str,
        storage_key: str,
        storage_bucket: StorageBucket,
        database_name: str = UNDEFINED,
        object_store_name: str = UNDEFINED,
        key_range: KeyRange = UNDEFINED
    ):
        params = {
            "databaseName": database_name,
            "objectStoreName": object_store_name,
            "keyRange": key_range,
        }

        if is_defined(
            security_origin
        ):
            params["securityOrigin"] = security_origin

        if is_defined(
            storage_key
        ):
            params["storageKey"] = storage_key

        if is_defined(
            storage_bucket
        ):
            params["storageBucket"] = storage_bucket

        return self._send_command(
            "IndexedDB.deleteObjectStoreEntries",
            params
        )

    def disable(
        self
    ):
        params = {}

        return self._send_command(
            "IndexedDB.disable",
            params
        )

    def enable(
        self
    ):
        params = {}

        return self._send_command(
            "IndexedDB.enable",
            params
        )

    def request_data(
        self,
        security_origin: str,
        storage_key: str,
        storage_bucket: StorageBucket,
        database_name: str,
        object_store_name: str,
        index_name: str = UNDEFINED,
        skip_count: int = UNDEFINED,
        page_size: int = UNDEFINED,
        key_range: KeyRange = UNDEFINED
    ):
        params = {
            "databaseName": database_name,
            "objectStoreName": object_store_name,
            "indexName": index_name,
            "skipCount": skip_count,
            "pageSize": page_size,
        }

        if is_defined(
            security_origin
        ):
            params["securityOrigin"] = security_origin

        if is_defined(
            storage_key
        ):
            params["storageKey"] = storage_key

        if is_defined(
            storage_bucket
        ):
            params["storageBucket"] = storage_bucket

        if is_defined(
            key_range
        ):
            params["keyRange"] = key_range

        return self._send_command(
            "IndexedDB.requestData",
            params
        )

    def get_metadata(
        self,
        security_origin: str,
        storage_key: str,
        storage_bucket: StorageBucket = UNDEFINED,
        database_name: str = UNDEFINED,
        object_store_name: str = UNDEFINED
    ):
        params = {
            "databaseName": database_name,
            "objectStoreName": object_store_name,
        }

        if is_defined(
            security_origin
        ):
            params["securityOrigin"] = security_origin

        if is_defined(
            storage_key
        ):
            params["storageKey"] = storage_key

        if is_defined(
            storage_bucket
        ):
            params["storageBucket"] = storage_bucket

        return self._send_command(
            "IndexedDB.getMetadata",
            params
        )

    def request_database(
        self,
        security_origin: str,
        storage_key: str = UNDEFINED,
        storage_bucket: StorageBucket = UNDEFINED,
        database_name: str = UNDEFINED
    ):
        params = {
            "databaseName": database_name,
        }

        if is_defined(
            security_origin
        ):
            params["securityOrigin"] = security_origin

        if is_defined(
            storage_key
        ):
            params["storageKey"] = storage_key

        if is_defined(
            storage_bucket
        ):
            params["storageBucket"] = storage_bucket

        return self._send_command(
            "IndexedDB.requestDatabase",
            params
        )

    def request_database_names(
        self,
        security_origin: str = UNDEFINED,
        storage_key: str = UNDEFINED,
        storage_bucket: StorageBucket = UNDEFINED
    ):
        params = {}

        if is_defined(
            security_origin
        ):
            params["securityOrigin"] = security_origin

        if is_defined(
            storage_key
        ):
            params["storageKey"] = storage_key

        if is_defined(
            storage_bucket
        ):
            params["storageBucket"] = storage_bucket

        return self._send_command(
            "IndexedDB.requestDatabaseNames",
            params
        )
