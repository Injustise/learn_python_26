import time
import random

total = 0
for i in range(1, 101):
    total += i
print(total)
print(sum(range(1, 101)))

for _ in range(5):
    print("Hello World")
    time.sleep(1)

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j} * {i} = {i * j}", end = '\t') # 修改 print 末尾字符
    print() # 默认情况下 end = '\n'

ans = random.randrange(1, 101)
cnt = 0
while True:
    cnt += 1
    my_ans = int(input("请输入您的答案（0~100）："))
    if my_ans > ans:
        print("大了。")
    elif my_ans < ans:
        print("小了。")
    else:
        break
print(f"恭喜您成功猜出 {ans}，共计猜了 {cnt} 次。")