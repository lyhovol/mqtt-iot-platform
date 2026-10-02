def check_temperature(temp):
    if temp < -50 or temp > 100:
        return "数据异常"
    elif temp < 0:
        return "冰冻警告"
    elif temp >= 30:
        return "高温警告"
    else:
        return "温度正常"


if __name__ == "__main__":
    print(check_temperature(35))  # 自测用
