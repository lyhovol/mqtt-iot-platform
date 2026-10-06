class Alert:
    def __init__(self, device_name, level, temperature, timestamp=None):
        self.device_name = device_name
        self.level = level
        self.temperature = temperature
        self.timestamp = timestamp

    def describe(self):
        return (
            f"[{self.timestamp}] {self.device_name} {self.level}：{self.temperature}°C"
        )

    def to_dict(self):
        return {
            "device_name": self.device_name,
            "level": self.level,
            "temperature": self.temperature,
            "timestamp": self.timestamp,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            device_name=data["device_name"],
            level=data["level"],
            temperature=data["temperature"],
            timestamp=data.get("timestamp"),
        )
