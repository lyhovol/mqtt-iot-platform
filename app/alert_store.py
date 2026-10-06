import json
from app.alert import Alert


class AlertStore:
    def __init__(self, path):
        self.alerts = []
        self.path = path

    def add(self, alert):
        self.alerts.append(alert)

    def load(self):
        with open(self.path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.alerts = [Alert.from_dict(d) for d in data]

    def save(self):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(
                [alert.to_dict() for alert in self.alerts],
                f,
                ensure_ascii=False,
                indent=2,
            )

    def count(self):
        return len(self.alerts)

    def count_by_device(self):
        result = {}
        for alert in self.alerts:
            result[alert.device_name] = result.get(alert.device_name, 0) + 1
        return result
