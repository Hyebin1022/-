import math
def solution(n):
    a = math.sqrt(n)
    if a.is_integer(): return 1
    else: return 2
