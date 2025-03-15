from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetAvailabilityReq(_message.Message):
    __slots__ = ("vin",)
    VIN_FIELD_NUMBER: _ClassVar[int]
    vin: str
    def __init__(self, vin: _Optional[str] = ...) -> None: ...

class AvailabilityDataHead(_message.Message):
    __slots__ = ("updateTime", "unknown1")
    UPDATETIME_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN1_FIELD_NUMBER: _ClassVar[int]
    updateTime: int
    unknown1: int
    def __init__(self, updateTime: _Optional[int] = ..., unknown1: _Optional[int] = ...) -> None: ...

class AvailabilityData(_message.Message):
    __slots__ = ("head", "engineRunning", "unknown2", "engineRemoteRunning")
    HEAD_FIELD_NUMBER: _ClassVar[int]
    ENGINERUNNING_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN2_FIELD_NUMBER: _ClassVar[int]
    ENGINEREMOTERUNNING_FIELD_NUMBER: _ClassVar[int]
    head: AvailabilityDataHead
    engineRunning: int
    unknown2: int
    engineRemoteRunning: int
    def __init__(self, head: _Optional[_Union[AvailabilityDataHead, _Mapping]] = ..., engineRunning: _Optional[int] = ..., unknown2: _Optional[int] = ..., engineRemoteRunning: _Optional[int] = ...) -> None: ...

class GetAvailabilityResp(_message.Message):
    __slots__ = ("vin", "data", "unknown4")
    VIN_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN4_FIELD_NUMBER: _ClassVar[int]
    vin: str
    data: AvailabilityData
    unknown4: int
    def __init__(self, vin: _Optional[str] = ..., data: _Optional[_Union[AvailabilityData, _Mapping]] = ..., unknown4: _Optional[int] = ...) -> None: ...
