# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: availability.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'availability.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x61vailability.proto\x12#services.vehiclestates.availability\"!\n\x12GetAvailabilityReq\x12\x0b\n\x03vin\x18\x02 \x01(\t\"<\n\x14\x41vailabilityDataHead\x12\x12\n\nupdateTime\x18\x01 \x01(\x03\x12\x10\n\x08unknown1\x18\x02 \x01(\x03\"\x96\x01\n\x10\x41vailabilityData\x12G\n\x04head\x18\x01 \x01(\x0b\x32\x39.services.vehiclestates.availability.AvailabilityDataHead\x12\x15\n\rengineRunning\x18\x03 \x01(\x05\x12\x10\n\x08unknown2\x18\x04 \x01(\x05\x12\x10\n\x08unknown3\x18\x05 \x01(\x05\"y\n\x13GetAvailabilityResp\x12\x0b\n\x03vin\x18\x02 \x01(\t\x12\x43\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x35.services.vehiclestates.availability.AvailabilityData\x12\x10\n\x08unknown4\x18\x06 \x01(\x05\x32\xa0\x01\n\x13\x41vailabilityService\x12\x88\x01\n\x0fGetAvailability\x12\x37.services.vehiclestates.availability.GetAvailabilityReq\x1a\x38.services.vehiclestates.availability.GetAvailabilityResp\"\x00\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'availability_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_GETAVAILABILITYREQ']._serialized_start=59
  _globals['_GETAVAILABILITYREQ']._serialized_end=92
  _globals['_AVAILABILITYDATAHEAD']._serialized_start=94
  _globals['_AVAILABILITYDATAHEAD']._serialized_end=154
  _globals['_AVAILABILITYDATA']._serialized_start=157
  _globals['_AVAILABILITYDATA']._serialized_end=307
  _globals['_GETAVAILABILITYRESP']._serialized_start=309
  _globals['_GETAVAILABILITYRESP']._serialized_end=430
  _globals['_AVAILABILITYSERVICE']._serialized_start=433
  _globals['_AVAILABILITYSERVICE']._serialized_end=593
# @@protoc_insertion_point(module_scope)
