import csv
import random

# newline 用来规定换行符翻译机制：默认情况下，当写入 \n 时，Windows 变成 \r\n，Linux 变成 \n。
# 写入时，csv.writer 把换行符翻译成 \r\n，Python 再翻译一次变成 \r\r\n，导致多写一个空白行。
# 故处理 CSV 文件时，必须使用 newline=''，以避免字段内换行符被错误翻译。
with open('D://code_py//learn_9-1//py文件操作//02_CSV//scores.csv', 'w', newline = '',  encoding = 'utf-8-sig') as file: # 打开 csv 文件，规定路径，换行，解码
    writer = csv.writer(file) # 创建一个 csv 写入对象
    writer.writerow(['姓名', '语文', '数学', '英语']) # writerow 行写入
    names = ['东邪', '西毒', '南帝', '北丐'] 
    for name in names:
        scores = [random.randrange(60, 101) for _ in range(3)]
        scores.insert(0, name)
        writer.writerow(scores)


with open('D://code_py//learn_9-1//py文件操作//02_CSV//scores.csv', 'r', encoding = 'utf-8-sig') as file:
    reader = csv.reader(file)  # 创建一个读入对象
    for data_list in reader: # 行读入（遍历）
        print(reader.line_num, end = '\t') 
        for elem in data_list: # data_list 行列表
            print(elem, end = '\t')
        print()

