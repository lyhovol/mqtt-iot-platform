def check_temperature(temp):
    if temp < -50 or temp > 100:
        return "数据异常"
    elif temp < 0:
        return "冰冻警告"
    elif temp >= 30:
        return "高温警告"
    else:
        return "温度正常"


try:
    temp = float(input("请输入温度值: "))
    print(check_temperature(temp))
except ValueError:
    print("输入的不是有效的数字!")
