import math

c = float(input("请输入摄氏温度："))
f = c * 1.8 + 32
print(f"{c:.1f} 摄氏度 = {f:.1f} 华氏度\n")

f = float(input("请输入华氏温度："))
c = (f - 32) / 1.8
print("%.1f 华氏度 = %.1f 摄氏度\n" % (f, c))

r = float(input("请输入圆的半径："))
L = 2 * math.pi * r
S = math.pi * r ** 2
print("圆的周长：%.2f" % L)
print("圆的面积：%.2f\n" % S)

height = float(input("请输入您的身高（cm）："))
weight = float(input("请输入您的体重（kg）："))
BMI = weight / (height / 100) ** 2
print(f"{BMI = :.2f}")