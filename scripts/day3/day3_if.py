temperature = float(input("现在的温度是: "))
if temperature > 100 or temperature < -50:
    print("温度异常,请检查温度传感器")
elif temperature < 0:
    print("冰冻警告")
elif temperature >= 30:
    print("高温警告")
else:
    print("温度正常")
