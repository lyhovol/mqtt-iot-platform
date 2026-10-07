import json
import os


class BaseStore:
    MODEL = None

    def __init__(self, path):
        self.path = path
        self.items = []

    def add(self, obj):
        self.items.append(obj)

    def load(self):
        if not os.path.exists(self.path):
            self.items = []
            return
        with open(self.path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.items = [self.MODEL.from_dict(d) for d in data]

    def save(self):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(
                [obj.to_dict() for obj in self.items],
                f,
                ensure_ascii=False,
                indent=2,
            )

    def count(self):
        return len(self.items)
