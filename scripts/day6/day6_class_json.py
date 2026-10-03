from day6_class import Device
import json

devices = [Device("设备A", -5), Device("设备B", 20), Device("设备C", 35, online=False)]
rows = []
for d in devices:
    rows.append(d.to_dict())

with open("devices2.json", "w", encoding="utf-8") as f:
    json.dump(rows, f, ensure_ascii=False, indent=2)
with open("devices2.json", "r", encoding="utf-8") as f:
    data = json.load(f)
print(data[0])
print(type(data[0]))
print(data[0].level())
