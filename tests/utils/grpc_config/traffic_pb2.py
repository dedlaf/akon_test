# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: traffic.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC, 5, 28, 1, "", "traffic.proto"
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\rtraffic.proto\x12\x07traffic"Y\n\x0eTrafficRequest\x12\x15\n\rcustomer_name\x18\x01 \x01(\t\x12\x12\n\nstart_date\x18\x02 \x01(\t\x12\x10\n\x08\x65nd_date\x18\x03 \x01(\t\x12\n\n\x02ip\x18\x04 \x01(\t"6\n\x0fTrafficResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rtotal_traffic\x18\x02 \x01(\x02\x32S\n\x0eTrafficService\x12\x41\n\nGetTraffic\x12\x17.traffic.TrafficRequest\x1a\x18.traffic.TrafficResponse0\x01\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "traffic_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals["_TRAFFICREQUEST"]._serialized_start = 26
    _globals["_TRAFFICREQUEST"]._serialized_end = 115
    _globals["_TRAFFICRESPONSE"]._serialized_start = 117
    _globals["_TRAFFICRESPONSE"]._serialized_end = 171
    _globals["_TRAFFICSERVICE"]._serialized_start = 173
    _globals["_TRAFFICSERVICE"]._serialized_end = 256
# @@protoc_insertion_point(module_scope)
