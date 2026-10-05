import itertools # 返回的是一个迭代器，不能直接打印


# 产生ABCD的全排列
for it in itertools.permutations('ABCD'):
    print(it)

print('--------华丽的分隔线--------')

# 产生ABCDE的五选三的组合
for it in itertools.combinations('ABCDE', 3):
    print(it)

print('--------华丽的分隔线--------')

# 产生ABCD和123的笛卡尔积
for it in itertools.product('ABCD', '123'):
    print(it)

print('--------华丽的分隔线--------')

## 产生ABC的无限循环序列
itertools.cycle('ABC') # 因为是无限的，绝对不能直接转成 list()，否则会耗尽内存