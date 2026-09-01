set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {2, 4, 6, 8, 10}

print(set1 & set2) # {2, 4, 6} 交集
print(set1 | set2) # {1, 2, 3, 4, 5, 6, 7, 8, 10} 并集
print(set1 - set2) # {1, 3, 5, 7} 差集
print(set1 ^ set2) # {1, 3, 5, 7, 8, 10} 对称差集

set1 = {1, 3, 5}
set2 = {5, 4, 3, 2, 1}
set3 = {1, 2, 3, 4, 5}

print(set1 < set3) # True set1 是 set3 的真子集
print(set1 <= set3) # True set1 是 set3 的子集
print(set2 < set3) # False set2 不是 set3 的真子集
print(set2 <= set3) # True set2 是 set3 的子集