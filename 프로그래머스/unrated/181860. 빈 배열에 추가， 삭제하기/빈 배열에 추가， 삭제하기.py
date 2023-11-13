def solution(arr, flag):
    answer = []
    for pro, num in enumerate(arr):
        for i in range(num):
            if flag[pro]:
                answer.extend([num] * 2)
            else:
                answer.pop()
    return answer