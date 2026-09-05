import random
counters = [0] * 6
for _ in range(60000):
    face = random.randrange(0, 6)
    counters[face] += 1
for face in range(1, 7):
    print(f"点数 {face} 共计出现 {counters[face - 1]} 次")

languages = ["C++", "Python"]

languages.append("Java")
print(languages) # ['C++', 'Python', 'Java']

languages.insert(2, "Java") 
print(languages) # ['C++', 'Python', 'Java', 'Java']

if "Java" in languages: 
    languages.remove("Java") # 删除一个元素
    print(languages) # ['C++', 'Python', 'Java']
temp = languages.pop(1) # pop() 删除并返回值
languages.append(temp)
print(languages) # ['C++', 'Java', 'Python']

del languages[1]
print(languages) # ['C++', 'Python']

index = languages.index("C++")
print(f"{index = :}") # 0

count = languages.count("C++")
print(f"{count = :}") # 1

languages.reverse()
print(languages) # ['Python', 'C++']

languages.sort()
print(languages) # ['C++', 'Python']

