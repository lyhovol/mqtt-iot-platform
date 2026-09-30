def check_temperature(temp):
    if temp < -50 or temp > 100:
        return "数据异常"
    elif temp < 0:
        return "冰冻警告"
    elif temp >= 30:
        return "高温警告"
    else:
        return "温度正常"


print(check_temperature(-60))
print(check_temperature(150))
print(check_temperature(25))
print(check_temperature(35))
print(check_temperature(30))
