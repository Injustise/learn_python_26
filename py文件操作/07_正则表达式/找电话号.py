import re

pattern = re.compile(r'(?<=\D)(1[38]\d{9}|14[57]\d{8}|15[0-35-9]\d{8}|17[678]\d{8})(?=\D)')
sentence = '''重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
不是15600998765，也不是110或119，张伟的手机号才是15600998765。'''

tels_list = re.findall(pattern, sentence)
for tel in tels_list:
    print(tel)

print('--------华丽的分隔线--------')

# 方法二：通过迭代器取出匹配对象并获得匹配的内容
for it in pattern.finditer(sentence):
    print(it.group())