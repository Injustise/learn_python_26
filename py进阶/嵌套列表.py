names = ['关羽', '张飞', '赵云', '马超', '黄忠']
courses = ['语文', '数学', '英语']


# scores = [None] * len(names) * len(courses)  # 错误
'''
列表乘法 * 永远执行的是浅拷贝（复制引用），而不是深拷贝（复制对象本身）。
[None] * 3 ：依旧对 None 对象引用复制 3 次，但由于 None 是不可变对象，进行赋值修改操作时会直接创建一个新的对象，然后再进行替换。
[x] * 5: 这里的 X 是 [None, None, None] 这个列表对象。而列表是可变对象，进行赋值修改操作时会直接影响到所有的引用对象。
'''
scores = [[None] * len(courses) for _ in range(len(names))]
for row, name in enumerate(names):
    for col, course in enumerate(courses):
        scores[row][col] = float(input(f'请输入{name}的{course}成绩：'))
        print(scores)