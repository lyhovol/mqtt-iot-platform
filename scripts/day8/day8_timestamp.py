from app.store import DeviceStore

store = DeviceStore("scripts/day7/store.json")
store.load()
print(len(store.devices))
print(store.devices[0].timestamp)
