def solution(array):
    answer = [0,0]
    for a,b in enumerate(array):
        if b == max(array):
            answer[0]=b
            answer[1]=a
    return answer