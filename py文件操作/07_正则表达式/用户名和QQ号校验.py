import re

username = input('请输入用户名：')
qq = input('请输入QQ号：')
code = input('请输入密码（至少8位，必须包含数字以及大小写字母）：')

m1 = re.fullmatch(r'[0-9a-zA-z_]{1,20}', username)
m2 = re.fullmatch(r'[1-9]\d{4,11}', qq)
# 零宽断言
# (?=.*\d)：检查整个字符串里必须至少有一个数字。
# (?=.*[a-z])：if 检查整个字符串里必须至少有一个小写字母。
# (?=.*[A-Z])：if 检查整个字符串里必须至少有一个大写字母。
m3 = re.fullmatch(r'(?=.*\b)(?=.*[a-z])(?=.*[A-Z]).{8,}', code)

if not m1:
    print('请输入有效的用户名。')
if not m2:
    print('请输入有效的QQ号。')
if not m3:
    print('请输入有效的密码')
if m1 and m2 and m3:
    print('格式校验通过！')