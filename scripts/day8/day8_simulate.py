from app.simulator import Simulator
from app.store import DeviceStore

store = DeviceStore("scripts/day8/simulated.json")
sim = Simulator(store, ["sensor-001", "sensor-002", "sensor-003"])
sim.register()
sim.run(9)

check = DeviceStore("scripts/day8/simulated.json")
check.load()
print(len(check.devices))
