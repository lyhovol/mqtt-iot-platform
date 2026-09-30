device = {"name": "sensor1", "temperature": 20, "online": True}  # 创建字典
print(device["name"], device["temperature"], device["online"])
device["temperature"] = 30
print(device["name"], device["temperature"], device["online"])
device["location"] = "room1"
print(device["name"], device["temperature"], device["online"], device["location"])
device_list = [
    {"name": "sensor1", "temperature": 20, "online": True},
    {"name": "sensor2", "temperature": 30, "online": False},
]  # 创建字典列表
for i in device_list:
    print("设备名字:", i["name"], "温度:", i["temperature"], "在线状态:", i["online"])
