# 打包
a = 1, 2, 10
print(type(a))  # <class 'tuple'>
print(a)  # (1, 2, 10)
# 解包
x, y, z = a
print(f"{x = }, {y = }, {z = }")  # x = 1, y = 2, z = 10
i, *j = a
print(f"{i = }, {j = }")  # i = 1, j = [2, 10]，通过星号表达式，可以让一个变量接收多个值。在解包语法中，星号表达式只能出现一次。

a = 1
b = 2
print(f"{a = :}, {b = :}")  # a = 1, b = 2
a, b = b, a # 交换
print(f"{a = :}, {b = :}")  # a = 2, b = 1