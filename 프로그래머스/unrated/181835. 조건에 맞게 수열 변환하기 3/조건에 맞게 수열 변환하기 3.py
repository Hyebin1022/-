def solution(arr, k):
    answer = []
    if k % 2 ==1:
        for i in arr:
            answer.append(int(i)*k)
    else:
        for i in arr:
            answer.append(int(i)+k)
    return answer