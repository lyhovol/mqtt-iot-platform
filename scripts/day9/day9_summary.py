from app.alert_store import AlertStore

store = AlertStore("scripts/day9/alerts.json")
store.load()

print("总告警条数:", store.count())
print("按设备统计:", store.count_by_device())

print("最近 3 条:")
for alert in store.alerts[-3:]:
    print(" ", alert.describe())
