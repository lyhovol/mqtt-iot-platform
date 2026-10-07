from app.base_store import BaseStore
from app.device import Device


class DeviceStore(BaseStore):
    MODEL = Device

    def find(self, name):
        for device in self.items:
            if device.name == name:
                return device
        return None

    def online_count(self):
        return len([device for device in self.items if device.online])
