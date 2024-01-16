from collections import Counter

def solution(array):
    number_counts = Counter(array) # 숫자 : 횟수 
    most_common_numbers = number_counts.most_common(2) # 많이 등장한거 두개

    if len(most_common_numbers) > 1 and most_common_numbers[0][1] == most_common_numbers[1][1]:
        return -1
    else:
        return most_common_numbers[0][0]
