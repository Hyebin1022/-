def solution(num, k):
    str_num=str(num)
    for a, b in enumerate(str_num):
        if int(b) == k : return a+1
    return -1