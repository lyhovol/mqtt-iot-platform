from app.base import BaseModel


class Alert(BaseModel):
    def __init__(self, device_name, level, temperature, timestamp=None):
        self.device_name = device_name
        self.level = level
        self.temperature = temperature
        self.timestamp = timestamp

    def describe(self):
        return (
            f"[{self.timestamp}] {self.device_name} {self.level}：{self.temperature}°C"
        )
