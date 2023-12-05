def solution(cipher, code):
    answer = ''
    for a,b in enumerate(cipher): # 0:d 1:f ..
        if (a+1)%code == 0 : answer += b
    return answer