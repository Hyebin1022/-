def solution(num, total):
    d=0
    for i in range(1, num): #1,2,3
        d += i #6
    start=(total-d)//num #6/6
    answer = [i for i in range(start, start+num)]
    return answer