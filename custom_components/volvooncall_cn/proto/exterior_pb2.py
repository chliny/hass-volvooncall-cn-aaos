# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: exterior.proto
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
    'exterior.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x65xterior.proto\x12\x1fservices.vehiclestates.exterior\"\x1d\n\x0eGetExteriorReq\x12\x0b\n\x03vin\x18\x02 \x01(\t\":\n\x12\x45xteriorDataHeader\x12\x12\n\nupdateTime\x18\x01 \x01(\x03\x12\x10\n\x08unknown1\x18\x02 \x01(\x03\"\xf6\x02\n\x0c\x45xteriorData\x12\x43\n\x06header\x18\x01 \x01(\x0b\x32\x33.services.vehiclestates.exterior.ExteriorDataHeader\x12\x0c\n\x04lock\x18\x02 \x01(\x05\x12\x15\n\rfrontLeftDoor\x18\x03 \x01(\x05\x12\x16\n\x0e\x66rontRightDoor\x18\x04 \x01(\x05\x12\x14\n\x0crearLeftDoor\x18\x05 \x01(\x05\x12\x15\n\rrearRightDoor\x18\x06 \x01(\x05\x12\x17\n\x0f\x66rontLeftWindow\x18\x07 \x01(\x05\x12\x18\n\x10\x66rontRightWindow\x18\x08 \x01(\x05\x12\x16\n\x0erearLeftWindow\x18\t \x01(\x05\x12\x17\n\x0frearRightWindow\x18\n \x01(\x05\x12\x0c\n\x04hood\x18\x0b \x01(\x05\x12\x10\n\x08tailGate\x18\x0c \x01(\x05\x12\x10\n\x08unknown3\x18\r \x01(\x05\x12\x0f\n\x07sunRoof\x18\x0e \x01(\x05\x12\x10\n\x08unknown4\x18\x0f \x01(\x05\"[\n\x0fGetExteriorResp\x12\x0b\n\x03vin\x18\x01 \x01(\t\x12;\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32-.services.vehiclestates.exterior.ExteriorData2\x87\x01\n\x0f\x45xteriorService\x12t\n\x0bGetExterior\x12/.services.vehiclestates.exterior.GetExteriorReq\x1a\x30.services.vehiclestates.exterior.GetExteriorResp\"\x00\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'exterior_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_GETEXTERIORREQ']._serialized_start=51
  _globals['_GETEXTERIORREQ']._serialized_end=80
  _globals['_EXTERIORDATAHEADER']._serialized_start=82
  _globals['_EXTERIORDATAHEADER']._serialized_end=140
  _globals['_EXTERIORDATA']._serialized_start=143
  _globals['_EXTERIORDATA']._serialized_end=517
  _globals['_GETEXTERIORRESP']._serialized_start=519
  _globals['_GETEXTERIORRESP']._serialized_end=610
  _globals['_EXTERIORSERVICE']._serialized_start=613
  _globals['_EXTERIORSERVICE']._serialized_end=748
# @@protoc_insertion_point(module_scope)
