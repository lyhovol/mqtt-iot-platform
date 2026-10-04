from app.device import Device
import json


class DeviceStore:
    def __init__(self, path):
        self.path = path
        self.devices = []

    def add(self, device):
        self.devices.append(device)

    def load(self):
        with open(self.path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.devices = [Device.from_dict(d) for d in data]

    def save(self):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(
                [d.to_dict() for d in self.devices], f, ensure_ascii=False, indent=2
            )

    def find(self, name):
        for device in self.devices:
            if device.name == name:
                return device
        return None

    def online_count(self):
        return len([device for device in self.devices if device.online])
