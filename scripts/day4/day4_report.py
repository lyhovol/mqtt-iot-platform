devices = [
    {"name": "传感器A", "temperature": 25, "online": False},
    {"name": "传感器B", "temperature": 30, "online": True},
    {"name": "传感器C", "temperature": -10, "online": True},
    {"name": "传感器D", "temperature": 15, "online": False},
]


def describe_device(device):
    name = device["name"]
    temperature = device["temperature"]
    online = device["online"]
    if online:
        status = "在线"
    else:
        status = "离线"
    return f"设备名称: {name}, 温度: {temperature}°C, 状态: {status}"


def summarize_devices(devices):
    o = 0
    for device in devices:
        if device["online"]:
            o += 1
    return f"总设备数量: {len(devices)}, 在线设备数量: {o}"


try:
    for device in devices:
        print(describe_device(device))
    print(summarize_devices(devices))
except Exception as e:
    print(f"发生错误: {e}")
