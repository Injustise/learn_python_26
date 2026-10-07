from concurrent.futures import ProcessPoolExecutor
import math

PRIMES = [
    1116281,
    1297337,
    104395303,
    472882027,
    533000389,
    817504243,
    982451653,
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419
] * 5

def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = math.isqrt(n) # isqrt() 开方并向下取整
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    with ProcessPoolExecutor() as pool:
        for number, prime in zip(PRIMES, pool.map(is_prime, PRIMES)): # zip 相互匹配，返回迭代器
            print(f'{number} is prime: {prime}')
        '''
        map 是 submit 的高级封装（等价于）：
            futures = [pool.submit(is_prime, prime) for prime in PRIMES]
            for future in futures:
                yield future.result() # 因为 map 还要返回迭代器，故需要 yield 返回 future.result()
        '''
if __name__ == '__main__':
    main()