from app.device import Device

d1 = Device("设备A", -5)
d2 = Device("设备B", 20)
d3 = Device("设备C", 35, online=False)
for d in (d1, d2, d3):
    print(f"{d.describe()}，{d.level()}")
