from concurrent.futures import ThreadPoolExecutor
from random import randint
from time import sleep

import threading

class Account():
    def __init__(self, balance = 0):
        self.balance = balance
        lock = threading.Lock()
        self.condition = threading.Condition(lock)
        '''
        Condition 可以理解为：一把锁 + 一个等待队列 + 唤醒机制
        '''

    # 取钱
    def withdraw(self, money):
        with self.condition:
            while(money > self.balance):
                self.condition.wait() # 只要不满足条件，就暂停自己（进入等待队列）
            new_balance = self.balance - money
            sleep(0.001)
            self.balance = new_balance

    # 存钱
    def deposit(self, money):
        with self.condition:
            new_balance = self.balance + money
            sleep(0.001)
            self.balance = new_balance
            self.condition.notify_all() # 唤醒等待队列中的所有线程
    
def add_money(account):
    while True:
        money = randint(5, 10)
        account.deposit(money)
        print(threading.current_thread().name, 
              ':', money, '====>', account.balance)
        sleep(0.5)


def sub_money(account):
    while True:
        money = randint(10, 30)
        account.withdraw(money)
        print(threading.current_thread().name, 
              ':', money, '<====', account.balance)
        sleep(1)

def main():
    account = Account()
    with ThreadPoolExecutor(max_workers = 15) as pool:
        for _ in range(5):
            pool.submit(add_money, account)
        for _ in range(10):
            pool.submit(sub_money, account)

if __name__ == '__main__':
    main()