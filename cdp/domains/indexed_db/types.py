from dataclasses import (
    dataclass
)
from cdp.domains.runtime.types import (
    RemoteObject
)
from cdp.domains.storage.types import (
    StorageBucket
)


@dataclass
class DatabaseWithObjectStores:
    name: str
    version: float
    object_stores: list


@dataclass
class ObjectStore:
    name: str
    key_path: "KeyPath"
    auto_increment: bool
    indexes: list


@dataclass
class ObjectStoreIndex:
    name: str
    key_path: "KeyPath"
    unique: bool
    multi_entry: bool


@dataclass
class Key:
    type: str
    number: float
    string: str
    date: float
    array: list


@dataclass
class KeyRange:
    lower: "Key"
    upper: "Key"
    lower_open: bool
    upper_open: bool


@dataclass
class DataEntry:
    key: "RemoteObject"
    primary_key: "RemoteObject"
    value: "RemoteObject"


@dataclass
class KeyPath:
    type: str
    string: str
    array: list


@dataclass
class RequestDataReturnT:
    object_store_data_entries: list
    has_more: bool


@dataclass
class GetMetadataReturnT:
    entries_count: float
    key_generator_value: float


@dataclass
class RequestDatabaseReturnT:
    database_with_object_stores: "DatabaseWithObjectStores"


@dataclass
class RequestDatabaseNamesReturnT:
    database_names: list