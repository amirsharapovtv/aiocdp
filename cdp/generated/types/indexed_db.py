# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.
from cdp.types import (
    runtime,
    storage
)
from typing import (
    TypedDict
)


class DatabaseWithObjectStores(TypedDict):
    name: str
    version: float
    object_stores: list


class ObjectStore(TypedDict):
    name: str
    key_path: 'KeyPath'
    auto_increment: bool
    indexes: list


class ObjectStoreIndex(TypedDict):
    name: str
    key_path: 'KeyPath'
    unique: bool
    multi_entry: bool


class Key(TypedDict):
    type: str
    number: float
    string: str
    date: float
    array: list


class KeyRange(TypedDict):
    lower_open: bool
    upper_open: bool
    lower: 'Key'
    upper: 'Key'


class DataEntry(TypedDict):
    key: 'runtime.RemoteObject'
    primary_key: 'runtime.RemoteObject'
    value: 'runtime.RemoteObject'


class KeyPath(TypedDict):
    type: str
    string: str
    array: list


class ClearObjectStoreParamsT(TypedDict):
    security_origin: str
    storage_key: str
    storage_bucket: 'storage.StorageBucket'
    database_name: str
    object_store_name: str


class DeleteDatabaseParamsT(TypedDict):
    security_origin: str
    storage_key: str
    storage_bucket: 'storage.StorageBucket'
    database_name: str


class DeleteObjectStoreEntriesParamsT(TypedDict):
    security_origin: str
    storage_key: str
    storage_bucket: 'storage.StorageBucket'
    database_name: str
    object_store_name: str
    key_range: 'KeyRange'


class RequestDataParamsT(TypedDict):
    security_origin: str
    storage_key: str
    storage_bucket: 'storage.StorageBucket'
    database_name: str
    object_store_name: str
    index_name: str
    skip_count: int
    page_size: int
    key_range: 'KeyRange'


class GetMetadataParamsT(TypedDict):
    security_origin: str
    storage_key: str
    storage_bucket: 'storage.StorageBucket'
    database_name: str
    object_store_name: str


class RequestDatabaseParamsT(TypedDict):
    security_origin: str
    storage_key: str
    storage_bucket: 'storage.StorageBucket'
    database_name: str


class RequestDatabaseNamesParamsT(TypedDict):
    security_origin: str
    storage_key: str
    storage_bucket: 'storage.StorageBucket'


class RequestDataReturnT(TypedDict):
    object_store_data_entries: list
    has_more: bool


class GetMetadataReturnT(TypedDict):
    entries_count: float
    key_generator_value: float


class RequestDatabaseReturnT(TypedDict):
    database_with_object_stores: 'DatabaseWithObjectStores'


class RequestDatabaseNamesReturnT(TypedDict):
    database_names: list