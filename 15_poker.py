from enum import Enum
import random

# 花色
class Suite(Enum): 
    SPADE, HEART, DIAMOND, CLUB = range(4) # 黑桃，红心，方块，梅花

# 牌
class Card:
    def __init__(self, suite, face):
        self.suite = suite
        self.face = face
    def __repr__(self):
        suites = "♠♥♦♣"
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f"{suites[self.suite.value]}{faces[self.face]}"
    def __lt__(self, other): # lt 是英文单词 less than 的缩写，这里重载 < 运算符
        if(self.face == other.face):
            return self.suite.value < other.suite.value
        return self.face < other.face

# 牌堆
class Poker:
    def __init__(self):
        self.cards = [
            Card(suite, face)
            for suite in Suite
            for face in range(1, 14)
        ]
        self.current = 0
    def shuffle(self): # 洗牌
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
    def get_one(self, card):
        self.cards.append(card)
    def arrange(self):
        self.cards.sort()
    
poker = Poker()
poker.shuffle()
players = [Player("东邪"), Player("西毒"), Player("南帝"), Player("北丐")]

for _ in range(1, 14):
    for player in players:
        player.get_one(poker.deal())

for player in players:
    player.arrange()
    print(f"{player.name}：", end = ' ')
    print(f"{player.cards}")
