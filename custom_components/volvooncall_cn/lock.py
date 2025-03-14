from __future__ import annotations
from homeassistant.components.lock import (
    LockEntity,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
    UpdateFailed,
)
import logging

from . import VolvoCoordinator, VolvoEntity
from . import metaMap
from .volvooncall_aaos import DOMAIN

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Configure sensors from a config entry created in the integrations UI."""
    coordinator: VolvoCoordinator = hass.data[DOMAIN][config_entry.entry_id]

    entities = []
    for idx, ent in enumerate(coordinator.data):
        entities.append(VolvoSensor(coordinator, idx, "car_lock"))
        entities.append(VolvoWindowSensor(coordinator, idx, "window_lock"))

    async_add_entities(entities)


class VolvoSensor(VolvoEntity, LockEntity):
    """An entity using CoordinatorEntity.

    The CoordinatorEntity class provides:
      should_poll
      async_update
      async_added_to_hass
      available
    """

    def __init__(self, coordinator, idx, metaMapKey):
        """Pass coordinator to CoordinatorEntity."""
        super().__init__(coordinator, idx, metaMapKey)

    @property
    def is_locked(self) -> bool | None:
        """Handle updated data from the coordinator."""
        data_map = self.coordinator.data[self.idx].toMap()
        # return data_map["car_locked"] and not data_map["remote_door_unlock"]
        return data_map["car_locked"]

    async def async_lock(self, **kwargs: Any) -> None:
        """Lock the car."""
        await self.coordinator.data[self.idx].lock()
        await self.coordinator.async_request_refresh()

    async def async_unlock(self, **kwargs: Any) -> None:
        """Unlock the car."""
        if not self.coordinator.data[self.idx].toMap()["car_locked"]:
            await self.coordinator.data[self.idx].unlock()

        await self.coordinator.async_request_refresh()


class VolvoWindowSensor(VolvoEntity, LockEntity):
    def __init__(self, coordinator, idx, metaMapKey):
        super().__init__(coordinator, idx, metaMapKey)

    @property
    def is_locked(self) -> bool | None:
        data_map = self.coordinator.data[self.idx].toMap()
        _LOGGER.debug(data_map)
        window_keys = ["front_left_window_open", "front_right_window_open",
                       "rear_right_window_open", "rear_left_window_open"]
        for window in window_keys:
            is_open = data_map[window]
            _LOGGER.debug("%s %s", window, is_open)
            if is_open:
                return False
        return True

    async def async_lock(self, **kwargs: Any) -> None:
        await self.coordinator.data[self.idx].lock_window()
        await self.coordinator.async_request_refresh()

    async def async_unlock(self, **kwargs: Any) -> None:
        await self.coordinator.data[self.idx].unlock_window()
        await self.coordinator.async_request_refresh()
