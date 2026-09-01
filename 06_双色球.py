import random

red_balls = list(range(1, 34)) # 1.list 列表
my_balls = []
for _ in range(6):
    index = random.randrange(len(red_balls)) # 动态长度，动态索引
    my_balls.append(red_balls.pop(index)) 
my_balls.sort()
for ball in my_balls:
    print(f"\033[031m{ball:0>2d}\033[0m", end = ' ')
blue_ball = random.randrange(1, 17)
print(f"\033[034m{blue_ball:0>2d}\033[0m")

print()

# sample, choice
red_balls = [i for i in range(1, 34)] # 2.for 列表
blue_balls = [i for i in range(1, 17)]
my_balls = random.sample(red_balls, 6) # 无放回随机抽样
my_balls.sort()
for ball in my_balls:
    print(f"\033[031m{ball:0>2d}\033[0m", end = ' ')
blue_ball = random.choice(blue_balls) # 随机抽取一个元素
print(f"\033[034m{blue_ball:0>2d}\033[0m")

print()

"""
\033[0m
    m 前面的 0 表示终端的显示方式为默认值，0 可以省略，1 表示高亮，5 表示闪烁，7 表示反显等。
    在 0 和 m 的中间的数字代表颜色，比如 30 代表黑色，31 代表红色，32 代表绿色，33 代表黄色，34 代表蓝色等
:
    格式说明的起始符（后以此为 填充 -> 对齐 -> 宽度 -> 类型）
"""

# rich
from rich.console import Console
from rich.table import Table

console = Console()
table = Table(show_header = True) # 表格（设置表头）
for col_name in ["序号", "红球", "蓝球"]: 
    table.add_column(col_name, justify = "center") # 表头居中


n = int(input("请输入下注个数："))
for i in range(n):
    my_balls = random.sample(red_balls, 6)
    my_balls.sort()
    blue_ball = random.choice(blue_balls)
    table.add_row(
        str(i + 1),
        " ".join(f"[red]{ball:0>2d}[/red]" for ball in my_balls),
        f"[blue]{blue_ball:0>2d}[/blue]"
    )
console.print(table)
"""
" ".join(...)
    将列表中的元素以空格为分隔符连接成一个字符串
"""
