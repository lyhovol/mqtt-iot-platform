class Device:
    def __init__(self, name, temperature, online=True):  # 构造
        self.name = name  # self指自己
        self.temperature = temperature
        self.online = online

    def describe(self):
        return f"设备 {self.name} 温度为 {self.temperature}°C {'在线' if self.online else '离线'}"

    def level(self):  # 返回字符串
        if self.temperature < 0:
            return "冰冻警告"
        elif self.temperature < 30:
            return "温度正常"
        else:
            return "高温警告"

    def to_dict(self):
        return {
            "name": self.name,
            "temperature": self.temperature,
            "online": self.online,
        }


if __name__ == "__main__":
    device1 = Device("设备A", -5)
    device2 = Device("设备B", 20)
    device3 = Device("设备C", 35, online=False)
    print(f"{device1.describe()}，{device1.level()}")
    print(f"{device2.describe()}，{device2.level()}")
    print(f"{device3.describe()}，{device3.level()}")
    device1.temperature = 15
    print(f"{device1.describe()}，{device1.level()}")
