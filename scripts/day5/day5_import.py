import requests
import random
from datetime import datetime


def mock_temperature():
    return round(random.uniform(20, 40), 1)


def now_stamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":
    print(requests.__version__)

    for i in range(3):
        print(f"[{now_stamp()}] 设备sensor-001 温度：{mock_temperature()}℃")
