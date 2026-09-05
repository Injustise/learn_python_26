import time
import random
from functools import wraps


def record_time(func):
    @wraps(func) # @wraps 将原函数 func 复制给包装函数 wrapper
    def wrapper(*arg, **kwargs):
        start = time.time()
        result = func(*arg, **kwargs)
        end = time.time()
        print(f"函数 {func.__name__} 执行时间：{end - start:.6f} 秒")
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

@record_time
def updown(file_name):
    print(f"正在上传文件 {file_name} ...")
    time.sleep(random.random() * 6)
    print(f"文件 {file_name} 上传完毕！")

@times(5)
def print_hw():
    print("Hello World!")

updown.__wrapped__("test01.txt") # 调用原函数
updown("test02.txt")


print_hw()