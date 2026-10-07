from app.base_store import BaseStore
from app.alert import Alert


class AlertStore(BaseStore):
    MODEL = Alert

    def count_by_device(self):
        result = {}
        for alert in self.items:
            result[alert.device_name] = result.get(alert.device_name, 0) + 1
        return result
