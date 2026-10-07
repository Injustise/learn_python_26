class Thing:
    def __init__(self, name, price, weight): # 本质构造函数。用于初始化
        self.name = name
        self.price = price
        self.weight = weight

    @property # property 装饰器把 value 方法变成属性
    def value(self):
        return self.price / self.weight

def input_thing():
    name_str, price_str, weight_str = input().split()
    return name_str, int(price_str), int(weight_str) # 打包返回一个元组

def main():
    max_weight, num_of_things = map(int, input().split())
    all_things = []
    for _ in range(num_of_things):
        all_things.append(Thing(*input_thing())) # * 解包，元组拆成三个参数，分别传入 name, price, weight
    all_things.sort(key = lambda x: x.value, reverse = True)
    total_weight = 0
    total_price = 0
    for thing in all_things:
        if total_weight + thing.weight <= max_weight:
            print(f'小偷拿走了{thing.name}')
            total_weight += thing.weight
            total_price += thing.price
    print(f'总价值: {total_price}美元')

if __name__ == '__main__':
    main()