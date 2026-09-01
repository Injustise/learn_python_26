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