import json

devices = [
    {"name": "sensor1", "temperature": 20, "online": True},
    {"name": "sensor2", "temperature": 30, "online": False},
    {"name": "sensor3", "temperature": 25, "online": True},
]

with open("scripts/day5/devices.json", "w", encoding="utf-8") as f:

    json.dump(devices, f, ensure_ascii=False, indent=2)

with open("scripts/day5/devices.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(len(data))
print(data[0]["name"])

with open("scripts/day5/notes.txt", "w", encoding="utf-8") as f:
    f.write("这是一个测试文件\n")
    f.write("这是第二行\n")
    f.write("这是第三行\n")

with open("scripts/day5/notes.txt", "r", encoding="utf-8") as f:
    print(f.read())
