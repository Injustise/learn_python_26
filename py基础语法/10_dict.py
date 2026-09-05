person1 = dict(name = "John", age = 25, city = "New York")
person2 = {
    "name": "Jane",
    "age": 30,
    "city": "Los Angeles"
}

print(", ".join(f"{key}: {person1[key]}" for key in person1)) # 默认 person1.keys()
print(person1.keys()) # dict_keys(['name', 'age', 'city'])
print(person1.values()) # dict_values(['John', 25, 'New York'])
print(person1.items()) # dict_items([('name', 'John'), ('age', 25), ('city', 'New York')])
print(" | ".join(f"{key}: {value}" for key, value in person2.items()))

# 索引**读取**字典中的值时，如果指定的键没有在字典中，会导致 KeyError 报错。
print(person1.get("name")) # John
print(person1.get("gender")) # 默认返回 None
print(person1.get("gender", 0)) # 0

counter = {}
sentence = input("请输入一句话（English）：")
for ch in sentence:
    if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
        counter[ch] = counter.get(ch, 0) + 1 # 这里索引**写入（赋值）**字典中的值时，即使指定的键没有在字典中，也没问题。
sorted_key = sorted(counter, key = counter.get, reverse = True)
for key in sorted_key:
    print(f"字母 {key} 出现了 {counter[key]} 次")

      