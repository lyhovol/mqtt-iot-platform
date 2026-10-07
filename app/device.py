from app.base import BaseModel


class Device(BaseModel):
    def __init__(self, name, temperature, online=True, timestamp=None):  # 构造
        self.name = name  # self指自己
        self.temperature = temperature
        self.online = online
        self.timestamp = timestamp

    def describe(self):
        return f"设备 {self.name} 温度为 {self.temperature}°C {'在线' if self.online else '离线'}"

    def level(self):  # 返回字符串
        if self.temperature < 0:
            return "冰冻警告"
        elif self.temperature < 30:
            return "温度正常"
        else:
            return "高温警告"
