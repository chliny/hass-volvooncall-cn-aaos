import logging
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.components.button import ButtonEntity, ButtonEntityDescription

from . import VolvoCoordinator, VolvoEntity
from .volvooncall_aaos import DOMAIN

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up button."""
    coordinator: VolvoCoordinator = hass.data[DOMAIN][config_entry.entry_id]

    buttons = []
    for idx, _ in enumerate(coordinator.data):
        buttons.append(VolvoFlashButton(coordinator, idx, "flash_button"))
        buttons.append(VolvoHonkFlashButton(coordinator, idx, "honk_flash_button"))

    async_add_entities(buttons)


class VolvoFlashButton(VolvoEntity, ButtonEntity):
    """Representation of a Volvo Cars button."""

    def __init__(self, coordinator, idx, metaMapKey):
        super().__init__(coordinator, idx, metaMapKey)

    async def async_press(self) -> None:
        await self.coordinator.data[self.idx].flash()


class VolvoHonkFlashButton(VolvoEntity, ButtonEntity):
    """Representation of a Volvo Cars button."""

    def __init__(self, coordinator, idx, metaMapKey):
        super().__init__(coordinator, idx, metaMapKey)

    async def async_press(self) -> None:
        await self.coordinator.data[self.idx].honk_and_flash()
