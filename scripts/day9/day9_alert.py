import json

from app.alert import Alert

a1 = Alert(
    device_name="sensor-001",
    level="高温警告",
    temperature=43.2,
    timestamp="2026-10-06 11:15:00",
)
a2 = Alert(
    device_name="sensor-002",
    level="冰冻警告",
    temperature=-3.5,
    timestamp="2026-10-06 11:16:00",
)

print(a1.describe())
print(a2.describe())

# 存
with open("scripts/day9/alerts_probe.json", "w", encoding="utf-8") as f:
    json.dump([a1.to_dict(), a2.to_dict()], f, ensure_ascii=False, indent=2)

# 读回来
with open("scripts/day9/alerts_probe.json", "r", encoding="utf-8") as f:
    data = json.load(f)

back = [Alert.from_dict(d) for d in data]
for a in back:
    print(a.describe())
