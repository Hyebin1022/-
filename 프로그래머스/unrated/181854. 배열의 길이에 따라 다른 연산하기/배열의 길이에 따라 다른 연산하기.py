def solution(arr, n):
    answer = []
    for a, b in enumerate(arr):
        if len(arr) % 2 == 1:
            if a % 2 == 0:
                answer.append(b + n)
            else:
                answer.append(b)
        else:
            if a % 2 == 0:
                answer.append(b)
            else:
                answer.append(b + n)
    return answer
