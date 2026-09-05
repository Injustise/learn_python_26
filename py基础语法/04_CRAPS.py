import random
import time

money = 1000
while money > 0:
    print(f"当前您的总资产为：{money} 元")
    while True:
        debt = int(input("请输入下注金额："))
        if debt > money:
            print("总资产不足，请重新输入！")
        elif debt <= 0:
            print("输入有误，请重新输入！")
        else:
            break
    print(f"玩家下注 {debt} 元")
    cnt = 1
    while True:
        time.sleep(1)
        if cnt == 1:
            print("--------- 第 1 回合 ---------")
            first_point = random.randrange(1, 7) + random.randrange(1, 7)
            print(f"玩家摇出点数：{first_point}")
            if first_point == 7 or first_point == 11:
                print("玩家胜！")
                flag = True
                break
            elif first_point == 2 or first_point == 3 or first_point == 12:
                print("庄家胜！")
                flag = False
                break
        else:
            print(f"--------- 第 {cnt} 回合 ---------")
            my_point = random.randrange(1, 7) + random.randrange(1, 7)
            print(f"玩家摇出点数：{my_point}")
            if my_point == first_point:
                print("玩家胜！")
                flag = True
                break
            elif my_point == 7:
                print("庄家胜！")
                flag = False
                break
        cnt += 1
    if(flag): money += debt
    else: money -= debt
print("您已破产，游戏结束！")