def solution(A, B):
    B = B*2 #ohellohell
    if A in B: return B.find(A)
    else: return -1
    