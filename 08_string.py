# 大小写操作
s1 = "hello world!"
print(s1.capitalize()) # Hello world!
print(s1.title()) # Hello World!
s1 = s1.upper()
print(s1) # HELLO WORLD!
s1 = s1.lower()
print(s1) # hello world!

# 格式化操作
s2 = "hello world"
print(s2.center(20, "-")) # -------hello world-------
print(s2.ljust(20, "~")) # hello world~~~~~~~~
print(s2.rjust(20, "~")) # ~~~~~~~~~hello world
print("2".zfill(2)) # 02

# 修剪操作
s3 = s2.center(20, "-")
print(s3.strip()) # hello world
print(s3.lstrip("-")) # hello world-------
print(s3.rstrip("-")) # -------hello world

# 拆分与合并操作
s4 = "zhangjinghang@qq.com"
email = s4.split("@")
print(email) # ['zhangjinghang', 'qq.com']
print("@".join(email)) # zhangjinghang@qq.com

# 解码与编码
a = "张三"
b = a.encode("utf-8")
c = a.encode("gbk")
print(b) # b'\xe5\xbc\xa0\xe4\xb8\x89'  
print(c) # b'\xd5\xc5\xcb\xae'
print(b.decode("utf-8")) # 张三
print(c.decode("gbk")) # 张三
# 如果编码和解码的方式不一致，会导致乱码