# 带有状态的执行上下文 or 状态机
def calc_avg():
    total, counter = 0, 0
    avg_value = None
    while(True):
        value = yield avg_value
        '''
        1.向外输出：返回 avg_value 的值并暂停（同普通生成器）
        2.向内接收：通过 gen.send(data) 发送数据时，函数被唤醒，data 会被赋值给等号左边的 value，然后继续往下执行。
        '''
        total += value
        counter += 1
        avg_value = total / counter

gen = calc_avg()
next(gen) # 预激。必须经过这一步，生成器才会停在 yield 处，准备好接收数据。
print(gen.send(10))
print(gen.send(20))
print(gen.send(30))
