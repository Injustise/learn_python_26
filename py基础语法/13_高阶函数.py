import functools
import operator

def calc(init_value, func, *args, **kwargs):
    nums = list(args) + list(kwargs.values())
    result = init_value
    for num in nums:
        result = func(result, num)
    return result

print(calc(0, operator.add, 1, 2, 3, 4, 5)) # 15
print(calc(1, operator.mul, 1, 2, 3, 4, 5)) # 120

def pow_2(x):
    return x ** 2
def is_even(x):
    return x % 2 == 0

nums = [1, 2, 3, 4, 5]
new_nums1 = list(map(pow_2, filter(is_even, nums))) # map 映射，filter 过滤
new_nums2 = list(map(lambda x: x ** 3, filter(lambda x: x % 2 == 1, nums))) # lambda 匿名函数
print(new_nums1) # [4, 16]
print(new_nums2) # [1, 27, 125]

fac = lambda x: functools.reduce(operator.mul, range(1, x + 1), 1) # reduce 累乘
print(fac(5)) # 120

is_prime = lambda x: all(x % i != 0 for i in range(2, int(x ** 0.5) + 1)) and x > 1 # 判断质数（all 函数：全真为真，否则为假）
print(is_prime(7)) # True
print(is_prime(1)) # False 

# functools.partial 固定一个函数的某些参数，返回一个新的函数
int2 = functools.partial(int, base = 2) # 偏函数，指定参数 base = 2
int8 = functools.partial(int, base = 8) # 偏函数，指定参数 base = 8
print(int('10010')) # int() 默认情况下将字符串视为十进制整数进行类型转换
print(int2('10010')) # int2() 将字符串视为二进制整数进行类型转换
print(int8('10010')) # int8() 将字符串视为八进制整数进行类型转换