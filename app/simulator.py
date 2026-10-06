import random
from datetime import datetime
from app.device import Device
from app.alert import Alert
import time


class Simulator:
    def __init__(self, store, alert_store, device_names):
        self.store = store
        self.alert_store = alert_store
        self.device_names = device_names

    def register(self):
        for name in self.device_names:
            self.store.add(Device(name, 25.0))
        self.store.save()

    def report_once(self):
        device = random.choice(self.store.devices)
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        device.temperature = round(random.uniform(15, 45), 1)
        device.timestamp = ts

        print(f"[{ts}] {device.name} {device.temperature}°C {device.level()}")
        if device.level() != "温度正常":
            print(f"[告警] {device.name} {device.level()}：{device.temperature}°C")
            self.alert_store.add(
                Alert(
                    device_name=device.name,
                    level=device.level(),
                    temperature=device.temperature,
                    timestamp=ts,
                )
            )

    def run(self, rounds, interval=1, flush_every=3):
        try:
            for i in range(rounds):
                self.report_once()
                time.sleep(interval)
                if (i + 1) % flush_every == 0:
                    self.store.save()
        finally:
            self.store.save()
            self.alert_store.save()
