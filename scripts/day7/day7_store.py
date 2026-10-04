from app.device import Device
from app.store import DeviceStore

store = DeviceStore("scripts/day7/store.json")
store.add(Device("sensor-001", 36.5))
store.add(Device("sensor-002", 28.0, online=False))
store.add(Device("sensor-003", 41.2))
store.save()

store2 = DeviceStore("scripts/day7/store.json")
store2.load()
print(len(store2.devices))
print(store2.online_count())
print(store2.find("sensor-002").describe())
print(store2.find("不存在"))
