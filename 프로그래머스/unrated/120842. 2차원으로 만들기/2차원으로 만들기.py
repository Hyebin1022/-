def solution(num_list, n):
    answer = []
    sub_list = []

    for num in num_list:
        sub_list.append(num)
        if len(sub_list) == n:
            answer.append(sub_list)
            sub_list = []

    return answer