# n!/ (n-m)!*m!
from math import factorial as fac

def solution(balls, share):
    n = fac(balls)
    m = fac(share)
    mi = fac(balls-share)
    
    answer = n/(mi*m)
    
    return answer
