import math

def solution(n):
    print((n * 6))
    print(math.gcd(n, 6))
    return (n * 6) // math.gcd(n, 6) // 6
