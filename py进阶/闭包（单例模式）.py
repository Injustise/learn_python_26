from functools import wraps

def singleton(cls): # 单例模式（Singleton Pattern）保证一个类在整个程序运行期间，只能有一个实例（对象）
    instances = {}
    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper
# 闭包以函数为主体（本质修饰器），通过返回内部函数来实现对外部变量的访问和修改。函数打包若干变量（专属，不共享的）
# 类比类，以对象为主体，打包若干函数和变量
# 两者都提供封装性

# lock 保证线程安全，避免多线程同时访问同一个资源导致数据不一致的问题。
from threading import RLock

def singleton_thread_safe(cls):
    instances = {}
    locker = RLock() # 创建一个可重入锁对象
    @wraps(cls)
    def wrapper(*ards, **kwargs):
        if cls not in instances: #  第一次检查（避免每次都要抢锁，提高性能）
            with locker: # 加锁
                if cls not in instances: # 第二次检查（防止多线程同时突破第一次检查）
                    instances[cls] = cls(*ards, **kwargs)
'''
with locker:
    ...
等价于
locker.acquire() # 尝试获取锁，如果锁已经被其他线程占用，则当前线程会阻塞，直到锁被释放。
...
locker.release() # 释放锁
'''