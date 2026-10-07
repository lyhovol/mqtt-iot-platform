def format_device(name, temperature, online=True):
    if online:
        status = "在线"
    else:
        status = "离线"
    return f"设备名称: {name}, 温度: {temperature}°C, 状态: {status}"


print(format_device("传感器A", 25, False))
print(format_device("传感器B", 30))
print(format_device("传感器C", -10))
