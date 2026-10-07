import time, threading
from concurrent.futures import ThreadPoolExecutor

class Account():
    def __init__(self):
        self.balance = 0.0
        self.lock = threading.Lock()

    def deposit(self, money):
        with self.lock:
            new_balance = self.balance + money
            time.sleep(0.001) # 制造多线程问题，展示示例
            self.balance = new_balance

def main():
    account = Account()
    with ThreadPoolExecutor(max_workers = 10) as pool:
        futures = [pool.submit(account.deposit, 1) for _ in range(100)]
    for future in futures: # 捕获子线程的异常报错
        future.result()
    print(account.balance)


if __name__ == '__main__':
    main()