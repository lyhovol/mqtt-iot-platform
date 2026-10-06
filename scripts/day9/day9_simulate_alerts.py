from app.alert_store import AlertStore
from app.simulator import Simulator
from app.store import DeviceStore

store = DeviceStore("scripts/day9/devices.json")
alert_store = AlertStore("scripts/day9/alerts.json")
sim = Simulator(store, alert_store, ["sensor-001", "sensor-002", "sensor-003"])
sim.register()
sim.run(9)

check = AlertStore("scripts/day9/alerts.json")
check.load()
print("告警条数:", check.count())
for a in check.alerts:
    print(a.describe())
