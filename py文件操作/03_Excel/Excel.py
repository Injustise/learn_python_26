# 读 Excel -------------------------
import datetime
import openpyxl

# 打开一个 excel 工作簿对象
wb = openpyxl.load_workbook('D://code_py//learn_9-1//py文件操作//03_Excel//2022年股票数据.xlsx')
# 获取所有工作表的名字
print(wb.sheetnames)
# 获取指定工作表（列表）
sheet = wb.worksheets[0]
# 获得该工作表的单元格的范围（dimension：尺寸；范围；维）
print(sheet.dimensions)
# 获得该工作表的行数和列数
print(sheet.max_row, sheet.max_column)

# 获取指定单元格的值（cell() 和 索引[]）
print(sheet.cell(3,3).value)
print(sheet['C3'].value)

# 获取多个单元格（嵌套元组）
print(sheet['A2:C5']) # 左上角：右下角

# 读取所有单元格的数据
for row in range(2, sheet.max_row + 1): # 第一行通常是标题
    for col in 'ABCDEF':
        value = sheet[f'{col}{row}'].value
        if type(value) == datetime.datetime: # 单元格格式为日期
            print(value.strftime('%Y年%m月%d日'), end = '\t')
        elif type(value) == int:
            print(f'{value:>10d}', end = '\t')
        elif type(value) == float:
            print(f'{value:.4f}', end = '\t')
        else:
            print(value, end = '\t')
    print()



# 写 Excel -------------------------
import random

# 第一步：创建工作簿（Workbook）
wb = openpyxl.Workbook()

# 第二步：添加工作表（Worksheet）
sheet = wb.active
sheet.title = '期末成绩'

titles = ('姓名', '语文', '数学', '英语')
for col, title in enumerate(titles): # enumerate 可以把可迭代对象变成一个“索引-值对”的迭代器
    sheet.cell(1, col + 1, title)
names = ('关羽', '张飞', '赵云', '马超', '黄忠')
for row, name in enumerate(names):
    sheet.cell(row + 2, 1, name)
    for col in range(2, 5):
        sheet.cell(row + 2, col, random.randrange(60, 101))

# 第四步：保存工作簿
wb.save('D://code_py//learn_9-1//py文件操作//03_Excel//蜀国考试成绩表.xlsx')



# Excel Style -------------------------
from openpyxl.styles import Font, Alignment, Border, Side
# Font：字体（字号、加粗、颜色、字体名称）
# Alignment：对齐方式（水平、垂直）
# Border 和 Side：边框（Side 定义线条样式，Border 组装成四边形）

alignment = Alignment(horizontal = 'center', vertical = 'center') # 水平居中，垂直居中
side = Side(color = 'ff7f50', style = 'mediumDashed') # 珊瑚色（橙红色），中等虚线

wb = openpyxl.load_workbook('D://code_py//learn_9-1//py文件操作//03_Excel//蜀国考试成绩表.xlsx')
sheet = wb.worksheets[0]

sheet.row_dimensions[1].height = 30
sheet.column_dimensions['E'].width = 120

sheet['E1'] = '平均分'
sheet.cell(1, 5).font = Font(size = 18, bold = True, color = 'ff1493', name = '华文楷体') # 18 号，加粗，深粉色，华文楷体
sheet.cell(1, 5).alignment = alignment
sheet.cell(1, 5).border = Border(left = side, top = side, right = side, bottom = side)

for row in range(2, 7):
    sheet[f'E{row}'] = f'=average(B{row}:D{row})' # 写入 Excel 公式
    sheet.cell(row, 5).font = Font(size = 12, color = '4169e1', italic = True)
    sheet.cell(row, 5).alignment = alignment

wb.save('D://code_py//learn_9-1//py文件操作//03_Excel//蜀国考试成绩表.xlsx')



# 创建图表 -------------------------
from openpyxl.chart import BarChart, Reference
from openpyxl.styles import Font, Alignment, Border, Side

wb = openpyxl.Workbook() # 当你开启仅写模式后，工作簿初始没有默认工作表，调用 wb.active 会直接报错
sheet = wb.active

rows = [
    ('类别', '销售A组', '销售B组'),
    ('手机', 40, 30),
    ('平板', 50, 60),
    ('笔记本', 80, 70),
    ('外围设备', 20, 10),
]

for row in rows:
    sheet.append(row)

chart = BarChart()

chart.type = 'col' # 纵向柱状图
chart.style = 10 # 内置的配色方案（10 号风格）

chart.title = '销售统计图'
chart.x_axis.title = '商品类别'
chart.y_axis.title = '销量'

# delete 控制图表坐标轴显示与隐藏
chart.x_axis.delete = False # 显示 x 轴
chart.y_axis.delete = False # 显示 y 轴

# Reference 创建一个指向 Excel 工作表中特定单元格区域的引用，作为后续创建图表时所需的数据源
data = Reference(sheet, min_col = 2, min_row = 1, max_row = 5, max_col = 3) # 数据：(1,2) -> (5,3)
cats = Reference(sheet, min_col=1, min_row=2, max_row=5, max_col = 1) # 类别：(1,2) -> (1,5)

chart.add_data(data, titles_from_data = True) # 添加数据，并指定第 1 行作为图例名称
chart.set_categories(cats)

chart.shape = 4 # 1 = 长方体，2 = 圆锥，3 = 金字塔，4 = 圆柱

sheet.add_chart(chart, 'A10')

wb.save('D://code_py//learn_9-1//py文件操作//03_Excel//销售统计图.xlsx')