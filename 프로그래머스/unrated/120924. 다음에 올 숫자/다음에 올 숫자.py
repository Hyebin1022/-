def solution(common):
    answer = 0
    if common[2]-common[1] == common[1]-common[0]: #등차수열
        answer = common[0] + len(common)*(common[1]-common[0])
    else: #등비수열 ar^(n-1)
        answer = common[0]*((common[2]/common[1])**len(common))
    return answer