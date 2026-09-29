device_name = "sensor-001"
temperature = 36.5
is_online = True  # 定义变量
print("Device Name:", device_name)
print("Temperature:", temperature)
print("Is Online:", is_online)  # 输出值
print("Device Name Type:", type(device_name))
print("Temperature Type:", type(temperature))
print("Is Online Type:", type(is_online))  # 输出类型
print(int(temperature))  # 将温度转换为整数
print(f"设备 {device_name} 温度 {temperature} 在线 {is_online}")  # 使用f-string输出
