def solution(arr):
    count = 0  # 2의 거듭제곱으로 만들기 위해 추가해야 하는 0의 개수를 세기 위한 변수
    length = len(arr)  # 주어진 리스트의 길이를 저장하는 변수

    while length > 1:
        length = length / 2  # 리스트의 길이를 2로 나누어가면서
        count += 1  # 2의 거듭제곱으로 만들기 위해 추가해야 하는 0의 개수를 증가시킴

    return arr + [0] * (2 ** count - len(arr))  # 0을 추가하여 리스트의 길이를 2의 거듭제곱으로 만듦