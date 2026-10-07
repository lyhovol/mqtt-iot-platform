from app.store import DeviceStore

store = DeviceStore("scripts/day7/store.json")
store.load()
print(len(store.items))
print(store.items[0].timestamp)
