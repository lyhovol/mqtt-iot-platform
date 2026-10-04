import json

from app.device import Device

devices = [
    Device("设备A", -5),
    Device("设备B", 20),
    Device("设备C", 35, online=False),
]

rows = []
for d in devices:
    rows.append(d.to_dict())

with open("scripts/day7/devices3.json", "w", encoding="utf-8") as f:
    json.dump(rows, f, ensure_ascii=False, indent=2)

with open("scripts/day7/devices3.json", "r", encoding="utf-8") as f:
    data = json.load(f)

restored = []
for d in data:
    restored.append(Device.from_dict(d))

for d in restored:
    print(f"{d.describe()}，{d.level()}")

restored[0].temperature = 99
print(f"{restored[0].describe()}，{restored[0].level()}")
