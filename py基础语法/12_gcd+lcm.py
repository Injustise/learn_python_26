def gcd(a: int, b: int) -> int: # : type -> type，类型注解：声明类型（增强可读性），但编译器不会强制检查
    return a if b == 0 else gcd(b, a % b)
def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)

