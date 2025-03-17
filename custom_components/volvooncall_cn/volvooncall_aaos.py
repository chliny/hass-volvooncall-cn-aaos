import logging
import datetime
import os
import grpc
import asyncio
from .volvooncall_cn import VehicleAPI, Vehicle, gcj02towgs84
from .proto.exterior_pb2_grpc import ExteriorServiceStub
from .proto.exterior_pb2 import GetExteriorReq, GetExteriorResp, ExteriorData
from .proto.fuel_pb2_grpc import FuelServiceStub
from .proto.fuel_pb2 import GetFuelReq, GetFuelResp
from .proto.invocation_pb2_grpc import InvocationServiceStub
from .proto.invocation_pb2 import windowControlReq, windowControlResp, invocationHead
from .proto.invocation_pb2 import EngineStartReq, EngineStartResp, EngineStartType
from .proto.invocation_pb2 import HonkFlashReq, HonkFlashResp
from .proto.invocation_pb2 import LockReq, LockResp
from .proto.odometer_pb2_grpc import OdometerServiceStub
from .proto.odometer_pb2 import GetOdometerReq, GetOdometerResp
from .proto.availability_pb2_grpc import AvailabilityServiceStub
from .proto.availability_pb2 import GetAvailabilityReq, GetAvailabilityResp, AvailabilityBool
from .proto.dtlinternet_pb2_grpc import DtlInternetServiceStub
from .proto.dtlinternet_pb2 import StreamLastKnownLocationsReq, StreamLastKnownLocationsResp
from .proto.engineremotestart_pb2_grpc import EngineRemoteStartServiceStub
from .proto.engineremotestart_pb2 import GetEngineRemoteStartReq, GetEngineRemoteStartResp, EngineRemoteStartType


_LOGGER = logging.getLogger(__name__)

AAOS_DIGITALVOLVO_HOST = "cepmobtoken.prod.c3.volvocars.com.cn:443"
AAOS_LBS_VOLVO_HOST = "cepmobtoken.lbs.prod.c3.volvocars.com.cn:443"
USER_AGENT = "vca-android/5.51.1 grpc-java-okhttp/1.68.0"
MAX_RETRIES = 1
TIMEOUT = datetime.timedelta(seconds=10)
DOMAIN = "volvooncall_cn_aaos"


class AAOSWindowOpenType(object):
    Open = 1
    Close = 2
    OpenCrack = 3

    @staticmethod
    def isOpen(openType) -> bool:
        return openType in [AAOSWindowOpenType.Open, AAOSWindowOpenType.OpenCrack]

    @staticmethod
    def isClose(openType) -> bool:
        return openType == AAOSWindowOpenType.Close


class AAOSVehicleAPI(VehicleAPI):
    def __init__(self, session, username, password):
        super(AAOSVehicleAPI, self).__init__(session, username, password)
        os.environ["GRPC_VERBOSITY"] = "debug"
        self.channel = None
        self.channel_token: str = ""
        self.lbs_channel = None
        self.lbs_channel_token: str = ""
        self.engine_duration = 5

    async def gen_channel(self, token, target):
        callCreds = grpc.access_token_call_credentials(token)
        sslCreds = grpc.ssl_channel_credentials()
        creds = grpc.composite_channel_credentials(sslCreds, callCreds)
        channel_options: tuple = (("grpc.primary_user_agent", USER_AGENT), ('grpc.accept_encoding', 'gzip'),)
        channel = grpc.secure_channel(target, creds, options=channel_options)
        _LOGGER.debug(channel.__dict__)
        return channel

    async def get_channel(self):
        if self.channel and self.channel_token == self._vocapi_access_token.strip():
            return
        self.channel_token = self._vocapi_access_token.strip()
        self.channel = await self.gen_channel(self.channel_token, AAOS_DIGITALVOLVO_HOST)

    async def get_lbs_channel(self):
        if self.lbs_channel and self.lbs_channel_token == self._vocapi_access_token.strip():
            return
        self.lbs_channel_token = self._vocapi_access_token.strip()
        self.lbs_channel = await self.gen_channel(self.lbs_channel_token, AAOS_LBS_VOLVO_HOST)

    async def get_fuel_status(self, vin) -> GetFuelResp:
        stub = FuelServiceStub(self.channel)
        req = GetFuelReq(vin=vin)
        metadata: list = [("vin", vin)]
        _LOGGER.debug(stub.__dict__)
        res = GetFuelResp()
        for res in stub.GetFuel(req, metadata=metadata, timeout=TIMEOUT.seconds):
            break
        return res

    async def get_exterior(self, vin) -> GetExteriorResp:
        stub = ExteriorServiceStub(self.channel)
        req = GetExteriorReq(vin=vin)
        metadata: list = [("vin", vin)]
        res = GetExteriorResp()
        for res in stub.GetExterior(req, metadata=metadata, timeout=TIMEOUT.seconds):
            break
        return res

    async def get_odometer(self, vin) -> GetOdometerResp:
        stub = OdometerServiceStub(self.channel)
        req = GetOdometerReq(vin=vin)
        metadata: list = [("vin", vin)]
        res = GetOdometerResp()
        for res in stub.GetOdometer(req, metadata=metadata, timeout=TIMEOUT.seconds):
            break
        return res

    async def get_availability(self, vin) -> GetAvailabilityResp:
        stub = AvailabilityServiceStub(self.channel)
        req = GetAvailabilityReq(vin=vin)
        metadata: list = [("vin", vin)]
        res = GetAvailabilityResp()
        for res in stub.GetAvailability(req, metadata=metadata, timeout=TIMEOUT.seconds):
            break
        return res

    async def window_control(self, vin, opentype) -> bool:
        stub = InvocationServiceStub(self.channel)
        req_header = invocationHead(vin=vin)
        req = windowControlReq(head=req_header, openType=opentype)
        metadata: list = [("vin", vin)]
        res: windowControlResp = windowControlResp()
        for res in stub.WindowControl(req, metadata=metadata, timeout=TIMEOUT.seconds):
            # TODO check res
            _LOGGER.debug(res)
            return True
        return False

    async def get_location(self, vin) -> StreamLastKnownLocationsResp:
        await self.get_lbs_channel()
        stub = DtlInternetServiceStub(self.lbs_channel)
        req = StreamLastKnownLocationsReq(vin=vin)
        metadata: list = [("vin", vin)]
        res: StreamLastKnownLocationsResp = StreamLastKnownLocationsResp()
        for res in stub.StreamLastKnownLocations(req, metadata=metadata, timeout=TIMEOUT.seconds):
            _LOGGER.debug(res)
            break
        return res

    async def engine_control(self, vin, startType) -> bool:
        stub = InvocationServiceStub(self.channel)
        req_header = invocationHead(vin=vin)
        req = EngineStartReq()
        if startType == EngineStartType.Start:
            duration = int(self.engine_duration)
            req = EngineStartReq(head=req_header, openType=startType, startDurationMin=duration)
        else:
            req = EngineStartReq(head=req_header, openType=startType)
        metadata: list = [("vin", vin)]
        res: EngineStartResp = EngineStartResp()
        for res in stub.EngineStart(req, metadata=metadata, timeout=TIMEOUT.seconds):
            _LOGGER.debug(res)
            return True
        return False

    async def honk_flash_control(self, vin, is_only_flash: bool) -> bool:
        stub = InvocationServiceStub(self.channel)
        req_header = invocationHead(vin=vin)
        req = HonkFlashReq(head=req_header)
        if is_only_flash:
            req.onlyFlash = 2
        metadata: list = [("vin", vin)]
        res: HonkFlashResp = HonkFlashResp()
        for res in stub.HonkFlash(req, metadata=metadata, timeout=TIMEOUT.seconds):
            _LOGGER.debug(res)
            return True
        return False

    async def door_lock(self, vin) -> bool:
        stub = InvocationServiceStub(self.channel)
        req_header = invocationHead(vin=vin)
        req = LockReq(head=req_header, lockType=1)
        metadata: list = [("vin", vin)]
        res: LockResp = LockResp()
        for res in stub.Lock(req, metadata=metadata, timeout=TIMEOUT.seconds):
            _LOGGER.debug(res)
            return True
        return False

    async def door_unlock(self, vin) -> bool:
        stub = InvocationServiceStub(self.channel)
        req_header = invocationHead(vin=vin)
        req = LockReq(head=req_header, lockType=2)
        metadata: list = [("vin", vin)]
        res: LockResp = LockResp()
        for res in stub.Unlock(req, metadata=metadata, timeout=TIMEOUT.seconds):
            _LOGGER.debug(res)
            return True
        return False

    async def get_engine_status(self, vin):
        stub = EngineRemoteStartServiceStub(self.channel)
        req = GetEngineRemoteStartReq(vin=vin)
        metadata: list = [("vin", vin)]
        res: GetEngineRemoteStartResp = GetEngineRemoteStartResp()
        for res in stub.GetEngineRemoteStart(req, metadata=metadata, timeout=TIMEOUT.seconds):
            _LOGGER.debug(res)
            break
        return res


class AAOSVehicle(Vehicle):
    def __init__(self, vin, api):
        super(AAOSVehicle, self).__init__(vin, api)

    async def _parse_exterior(self):
        try:
            exterior_resp: GetExteriorResp = await self._api.get_exterior(self.vin)
            exterior_data: ExteriorData = exterior_resp.data
            _LOGGER.debug(exterior_data)
        except Exception as err:
            _LOGGER.error(err)
            return
        self.car_locked = AAOSWindowOpenType.isClose(exterior_data.lock)
        self.front_left_door_open = AAOSWindowOpenType.isOpen(exterior_data.frontLeftDoor)
        self.front_right_door_open = AAOSWindowOpenType.isOpen(exterior_data.frontRightDoor)
        self.rear_left_door_open = AAOSWindowOpenType.isOpen(exterior_data.rearLeftDoor)
        self.rear_right_door_open = AAOSWindowOpenType.isOpen(exterior_data.rearRightDoor)
        self.front_left_window_open = AAOSWindowOpenType.isOpen(exterior_data.frontLeftWindow)
        self.front_right_window_open = AAOSWindowOpenType.isOpen(exterior_data.frontRightWindow)
        self.rear_left_window_open = AAOSWindowOpenType.isOpen(exterior_data.rearLeftWindow)
        self.rear_right_window_open = AAOSWindowOpenType.isOpen(exterior_data.rearRightWindow)
        self.sunroof_open = AAOSWindowOpenType.isOpen(exterior_data.sunRoof)
        self.tail_gate_open = exterior_data.tailGate == AAOSWindowOpenType.Open
        self.hood_open = AAOSWindowOpenType.isOpen(exterior_data.hood)

    async def _parse_fuel(self):
        try:
            fuel_resp: GetFuelResp = await self._api.get_fuel_status(self.vin)
            fuel_data = fuel_resp.data
            _LOGGER.debug(fuel_data)
        except Exception as err:
            _LOGGER.error(err)
            return
        self.fuel_amount = round(fuel_data.fuelAmount, 2)
        self.distance_to_empty = fuel_data.distanceToEmpty
        # self.fuel_amount_level = fuel_data.fluelHalfLevel / 5

    async def _parse_odometer(self):
        try:
            odometer_resp: GetOdometerResp = await self._api.get_odometer(self.vin)
            odometer_data = odometer_resp.data
            _LOGGER.debug(odometer_data)
        except Exception as err:
            _LOGGER.error(err)
            return
        self.odo_meter = odometer_data.totalDistance / 1000

    async def _parse_availability(self):
        try:
            availability_resp: GetAvailabilityResp = await self._api.get_availability(self.vin)
            availability_data = availability_resp.data
            _LOGGER.debug(availability_data)
        except Exception as err:
            _LOGGER.error(err)
            return
        self.engine_running = availability_data.engineLocalRunning == AvailabilityBool.Yes

    async def _parse_location(self):
        try:
            location_resp: StreamLastKnownLocationsResp = await self._api.get_location(self.vin)
        except Exception as err:
            _LOGGER.error(err)
            return
        self.position = {
            "latitude": location_resp.latitude,
            "longitude": location_resp.longitude,
        }
        wgs84_data = gcj02towgs84(self.position["longitude"], self.position["latitude"])
        if len(wgs84_data) >= 2:
            self.position_wgs84 = {
                "longitude": wgs84_data[0],
                "latitude": wgs84_data[1],
            }

    async def _parse_engine_status(self):
        try:
            engine_resp: GetEngineRemoteStartResp = await self._api.get_engine_status(self.vin)
            engine_data = engine_resp.data
        except Exception as err:
            _LOGGER.error(err)
            return
        if engine_data.engineStarting == EngineRemoteStartType.Yes or \
                engine_data.engineStarted in [EngineRemoteStartType.Yes, EngineRemoteStartType.Starting]:
            self.engine_remote_running = True
        else:
            self.engine_remote_running = False

    async def update(self):
        if not self.series_name:
            vehicles = await self._api.get_vehicles()
            for vehicle in vehicles:
                if vehicle["vinCode"] == self.vin:
                    self.series_name = vehicle["seriesName"]
                    self.model_name = vehicle["modelName"]

        tasks = []
        await self._api.get_channel()
        async with asyncio.TaskGroup() as tg:
            funcs = [self._parse_exterior, self._parse_odometer,
                     self._parse_fuel, self._parse_availability, self._parse_location, self._parse_engine_status]
            for runf in funcs:
                task = tg.create_task(runf())
                tasks.append(task)
        for task in tasks:
            _LOGGER.debug(task.result())

    async def lock_window(self):
        await self._api.window_control(self.vin, AAOSWindowOpenType.Close)

    async def unlock_window(self):
        await self._api.window_control(self.vin, AAOSWindowOpenType.Open)

    async def lock_vehicle(self):
        await self._api.door_lock(self.vin)

    async def unlock_vehicle(self):
        await self._api.door_unlock(self.vin)

    async def flash(self):
        await self._api.honk_flash_control(self.vin, True)

    async def honk_and_flash(self):
        await self._api.honk_flash_control(self.vin, False)

    async def engine_start(self):
        await self._api.engine_control(self.vin, EngineStartType.Start)

    async def engine_stop(self):
        await self._api.engine_control(self.vin, EngineStartType.Stop)

    async def set_engine_duration(self, durationMin):
        self._api.engine_duration = durationMin

    def get_engine_duration(self) -> float:
        return self._api.engine_duration
