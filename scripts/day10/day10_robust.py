from app.alert_store import AlertStore
from app.store import DeviceStore
import json
import os

# 场景 1：文件不存在 —— 应该不崩，items 为空
fresh = DeviceStore("scripts/day10/本来就不存在.json")
fresh.load()
print("场景1 条数:", len(fresh.items))

# 场景 2：文件坏了 —— 应该炸出 JSONDecodeError
with open("scripts/day10/broken.json", "w", encoding="utf-8") as f:
    f.write('[{"name": "x",')  # 故意只写半截

bad = AlertStore("scripts/day10/broken.json")
try:
    bad.load()
    print("场景2 没报错（不对，应该报错）")
except Exception as e:
    print("场景2 报错类型:", type(e).__name__)
    print("场景2 报错内容:", e)
