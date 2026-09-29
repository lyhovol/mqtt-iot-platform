device = ["sensor1", "sensor2", "sensor3"]
print(len(device))
print(device[0], device[-1])
device.append("sensor4")
for i in device:
    print("设备上线", i)
print(len(device))
