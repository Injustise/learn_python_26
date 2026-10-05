import time
import random
from functools import wraps

# 装饰器就是 用一个函数（record_time）装饰另外一个函数（func）并为其提供额外的能力 的语法
def record_time(func):
    @wraps(func) # wraps 也是一个修饰器（添加__wrapped__属性，实现修饰器的开关）
    def wrapper(*arg, **kwargs): # *arg, **kwargs 保证参数传入
        start = time.time()
        result = func(*arg, **kwargs) # 调用原函数 func
        end = time.time()
        print(f"函数 {func.__name__} 执行时间：{end - start:.6f} 秒")
        return result 
    return wrapper

# 类式
class Record_time:
    def __init__(self, output):
        self.output = output

    def __call__(self, func): # __call__ 方法使类的实例可以像函数一样被调用，从而支持语法糖 @Record_time(print) （这里的()是初始化output，区别带参修饰器）
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            self.output(func.__name__, end - start)
            return result
        return wrapper

# 带参数的装饰器（三层结构）
def times(num):
    def decorator(func):
        @wraps(func)
        def wrapper(*arg, **kwargs):
            for i in range(num):
                result = func(*arg, **kwargs)
            return result
        return wrapper
    return decorator

# @Record_time(print) # 添加装饰器
@record_time # 添加装饰器
def updown(file_name):
    print(f"正在上传文件 {file_name} ...")
    time.sleep(random.random() * 6)
    print(f"文件 {file_name} 上传完毕！")

@times(5)
def print_hw():
    print("Hello World!")

updown.__wrapped__("test01.txt") # 关闭修饰器
updown("test02.txt") # 打开修饰器


print_hw()