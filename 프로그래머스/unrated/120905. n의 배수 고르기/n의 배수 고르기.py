def solution(n, numlist):
    answer = []
    for i in numlist:
        x = i % n
        if x==0 : answer.append(i)
    return answer