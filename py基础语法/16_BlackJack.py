from enum import Enum
import random

class Suite(Enum):
    SPADE, HEART, DIAMOND, CLUB = range(4)

class Card:
    def __init__(self, suite, face):
        self.suite = suite
        self.face = face
    def __repr__(self):
        suites = "♠♥♦♣"
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f"{suites[self.suite.value]}{faces[self.face]}"
    def __lt__(self, other):
        if self.face == other.face:
            return self.suite.value < other.suite.value
        return self.face < other.face

class Poker:
    def __init__(self):
        self.cards = [
            Card(suite, face)
            for suite in Suite
            for face in range(1, 14)
        ]
        self.current = 0
    def shuffle(self):
        self.current = 0
        random.shuffle(self.cards)
    def deal(self):
        card = self.cards[self.current]
        self.current += 1
        return card
    def empty(self):
        return self.current >= len(self.cards)

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.is_stand = False
    def __repr__(self):
        return f"{self.name}：{self.cards}"
    def Hit(self, card):
        self.cards.append(card)
    def Stand(self):
        self.is_stand = True

    @property
    def point(self):
        tatol = 0
        for card in reversed(self.cards):
            if card.face == 1:
                if tatol + 11 <= 21:
                    tatol += 11
                else:
                    tatol += 1
            elif card.face == 11 or card.face == 12 or card.face == 13:
                    tatol += 10
            else:
                tatol += card.face
        return tatol

class Banker(Player): 
    def __init__(self, name):
        super().__init__(name) # 继承
        self.dark_card = None # 多态

def is_BlackJack(player):
    return player.cards[0].face == 1 and (player.cards[1].face == 11 or player.cards[1].face == 12 or player.cards[1].face == 13)

def get_int(prompt):
    while True:
        try:
            val = int(input(prompt))
            return val
        except ValueError:
            print("请输入有效的数字！")

money = 1000
while money > 0:
    print(f"当前您的总资产为：{money} $")
    while True:
        debt = get_int("请输入下注金额（$）：")
        if debt > money:
            print("总资产不足，请重新输入！")
        elif debt <= 0:
            print("输入有误，请重新输入！")
        else:
            break
    print(f"您的下注金额为：{debt} $ （当前倍率：×1.0）")

    print("------- BLACK JACK START! -------")

    you = Player("您")
    banker= Banker("庄家")
    poker = Poker()
    poker.shuffle()

    you.Hit(poker.deal())
    you.Hit(poker.deal())
    you.cards.sort()
    banker.Hit(poker.deal())
    banker.dark_card = poker.deal()

    print("---------")
    print(you)
    print(banker)
    print("---------")


    if is_BlackJack(you):
        print("BLACK JACK! （当前倍率：×0.1 -> ×1.5）")
        print(f"庄家暗牌：{banker.dark_card}")
        if banker.cards[0].face == 1 and (banker.dark_card.face == 11 or banker.dark_card.face == 12 or banker.dark_card.face == 13):
            print("平局！")
            continue
        if (banker.cards[0].face == 11 or banker.cards[0].face == 12 or banker.cards[0].face == 13) and banker.dark_card.face == 1:
            print("平局！")
            continue
        print("恭喜您获胜！")
        money += debt
        continue
    
    while(not you.is_stand):
        print("您的回合（0：Stand  1：Hit）：")
        select = int(input())
        match(select):
            case 0:
                you.is_stand = True
            case 1:
                you.Hit(poker.deal())
                you.cards.sort()

        print("---------")
        print(you)
        print("---------")

        if(you.point > 21 ):
            print("庄家胜")
            money -= debt
            break

    if you.point <= 21:
        print("---------")
        print(you)
        print(banker)
        print(f"庄家暗牌：[{banker.dark_card}]")
        print("---------")

        banker.Hit(banker.dark_card)
        banker.cards.sort()

        print(f"{banker.point = }")
        if(banker.point == 21):
            print("BLACK JACK!")
            print("庄家胜")
            money -= debt
            continue

        while(banker.point < 17):
            banker.Hit(poker.deal())
            banker.cards.sort()

        if(banker.point > 21):
            print("恭喜您获胜！")
            money += debt
            continue

        if 21 - you.point < 21 - banker.point:
            print("恭喜您获胜！")
            money += debt
        elif 21 - you.point > 21 - banker.point:
            print("庄家胜")
            money -= debt
        else:
            print("平局！")
print("您已破产，游戏结束！")
