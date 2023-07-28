from datetime import timedelta
import logging

import async_timeout

from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.dispatcher import async_dispatcher_send
from homeassistant.helpers.entity import DeviceInfo

from homeassistant.components.sensor import SensorEntity
from homeassistant.core import callback
from homeassistant.exceptions import ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
    UpdateFailed,
)

from .volvooncall_cn import VehicleAPI, Vehicle

DOMAIN = "volvooncall_cn"

PLATFORMS = {
    "sensor": "sensor",
    "binary_sensor": "binary_sensor",
}

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass, entry):
    """Config entry example."""
    session = async_get_clientsession(hass)

    my_api = VehicleAPI(session=session, username=entry.data["username"], password=entry.data["password"])
    hass.data.setdefault(DOMAIN, {})
    coordinator = hass.data[DOMAIN][entry.entry_id] = MyCoordinator(hass, my_api)

    # Fetch initial data so we have data when entities subscribe
    #
    # If the refresh fails, async_config_entry_first_refresh will
    # raise ConfigEntryNotReady and setup will try again later
    #
    # If you do not want to retry setup on failure, use
    # coordinator.async_refresh() instead
    #
    await coordinator.async_config_entry_first_refresh()
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True

class MyCoordinator(DataUpdateCoordinator):
    """My custom coordinator."""

    def __init__(self, hass, my_api):
        """Initialize my coordinator."""
        super().__init__(
            hass,
            _LOGGER,
            # Name of the data. For logging purposes.
            name="Volvo On Call CN sensor",
            # Polling interval. Will only be polled if there are subscribers.
            update_interval=timedelta(seconds=30),
        )
        self.my_api = my_api

    async def _async_update_data(self):
        """Fetch data from API endpoint.

        This is the place to pre-process the data to lookup tables
        so entities can quickly look up their data.
        """
        try:
            # Note: asyncio.TimeoutError and aiohttp.ClientError are already
            # handled by the data update coordinator.
            async with async_timeout.timeout(10):
                # Grab active context variables to limit data required to be fetched from API
                # Note: using context is not required if there is no need or ability to limit
                # data retrieved from API.
                await self.my_api.login()
                await self.my_api.update_token()
                vins = await self.my_api.get_vehicles_vins()
                vehicles = []
                for vin in vins:
                    vehicle = Vehicle(vin, self.my_api)
                    await vehicle.update()
                    vehicles.append(vehicle)

                return vehicles
        except Exception as err:
            raise UpdateFailed(f"Error communicating with API: {err}")

metaMap = {
    "car_lock_open": {
        "name": "Car Lock",
        "device_class": "lock",
    },
    "distance_to_empty": {
        "name": "Distance To Empty",
        "device_class": "",
    },
    "tail_gate_open": {
        "name": "Tail Gate Open",
        "device_class": "",
    },
    "rear_right_door_open": {
        "name": "Rear Right Door Open",
        "device_class": "",
    },
    "rear_left_door_open": {
        "name": "Rear Left Door Open",
        "device_class": "",
    },
    "front_right_door_open": {
        "name": "Front Right Door Open",
        "device_class": "",
    },
    "front_left_door_open": {
        "name": "Front Left Door Open",
        "device_class": "",
    },
    "hood_open": {
        "name": "Hood Open",
        "device_class": "",
    },
    "engine_running": {
        "name": "Engine Running",
        "device_class": "",
    },
    "odo_meter": {
        "name": "Odo Meter",
        "device_class": "",
    }
}

class MyEntity(CoordinatorEntity, SensorEntity):
    """An entity using CoordinatorEntity.

    The CoordinatorEntity class provides:
      should_poll
      async_update
      async_added_to_hass
      available
    """

    def __init__(self, coordinator, idx, metaMapKey):
        """Pass coordinator to CoordinatorEntity."""
        super().__init__(coordinator, context=idx)
        self.idx = idx
        self.metaMapKey = metaMapKey

    @property
    def name(self):
        return f"{self.coordinator.data[self.idx].vin} {metaMap[self.metaMapKey]['name']}"

    @property
    def device_info(self) -> DeviceInfo:
        """Return a inique set of attributes for each vehicle."""
        return DeviceInfo(
            identifiers={(DOMAIN, self.coordinator.data[self.idx].vin)},
            name=self.coordinator.data[self.idx].series_name,
            model=self.coordinator.data[self.idx].model_name,
            manufacturer="Volvo",
        )

    @property
    def unique_id(self) -> str:
        """Return a unique ID."""
        return f"{self.coordinator.data[self.idx].vin}-{self.metaMapKey}"

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        self._attr_native_value = self.coordinator.data[self.idx].toMap()[self.metaMapKey]
        self.async_write_ha_state()
