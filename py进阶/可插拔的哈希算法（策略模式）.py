# 对大文件流式计算哈希值（避免一次性把大文件读入内存）
class StreamHasher:
    def __init__(self, alg = 'md5', size = 4096): # size 设定每次读取文件块的大小
        self.size = size
        alg = alg.lower()
        self.hasher = getattr(__import__('hashlib'), alg)() # 最后的 () 指启用这个工具（函数）
        '''
        hashlib 是 Python 的一个内置模块，里面有各种哈希算法
        __import__('hashlib')：动态地引入模块，等价于 import hashlib
        getattr(模块, 'md5')：get attribute（获取属性）。在 hashlib 模块中，找到名为 md5 的工具（函数）
        实现动态调用哈希算法
        '''

    def __call__(self, stream):
        return self.to_digest(stream)

    def to_digest(self, stream):
        for buf in iter(lambda: stream.read(self.size), b''):
            self.hasher.update(buf)
        return self.hasher.hexdigest()
        '''
        iter(函数, 结束标记)：iter 是生成迭代器的函数。重复调用前面的函数，直到返回值和第二个参数相等时，停止。
        b''：二进制里的空
        update：把刚才读出来的 4KB 数据，喂给 self.hasher
        hexdigest：所有数据都喂完了，输出十六进制字符串的哈希值
        '''

def main():
    """主函数"""
    hasher1 = StreamHasher()
    with open('Python-3.7.6.tgz', 'rb') as stream:
        print(hasher1.to_digest(stream))
    hasher2 = StreamHasher('sha1')
    with open('Python-3.7.6.tgz', 'rb') as stream:
        print(hasher2(stream))


if __name__ == '__main__':
    main()