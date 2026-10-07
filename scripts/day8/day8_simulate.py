from app.simulator import Simulator
from app.store import DeviceStore
from app.alert_store import AlertStore

store = DeviceStore("scripts/day8/simulated.json")
alert_store = AlertStore("scripts/day8/alerts.json")
sim = Simulator(store, alert_store, ["sensor-001", "sensor-002", "sensor-003"])
sim.register()
sim.run(9)

check = DeviceStore("scripts/day8/simulated.json")
check.load()
print(len(check.items))
