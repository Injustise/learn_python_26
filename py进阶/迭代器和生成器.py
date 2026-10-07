# 迭代器
class Fib:
    def __init__(self, num):
        self.num = num
        self.a, self.b = 0, 1
        self.idx = 0

    def __iter__(self): 
        return self
    '''
    使用 for 循环遍历对象时，Python 会首先调用 iter(对象)，这便触发了对象的 __iter__() 方法
    而该方法必须返回一个迭代器
    for 循环拿到这个迭代器后，不断调用 next(迭代器)（即触发 __next__() 方法），直到遇到 StopIteration 异常，停止
    '''

    def __next__(self):
        if(self.idx < self.num):
            self.a, self.b = self.b, self.a + self.b
            self.idx += 1
            return self.a
        raise StopIteration()

# 当函数体内出现了 yield 关键字，这个函数便不再是普通函数，调用它不会执行函数体，而是返回一个生成器对象
def fib(num):
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
        yield a # 返回 a 的值并暂停

# 使用迭代器类
for i in Fib(5):
    print(i, end = ' ')  # 输出 1 1 2 3 5

print()

# 使用生成器
for i in fib(5):
    print(i, end = ' ')  # 输出 1 1 2 3 5