def solution(myString):
    num = []
    a = myString.split("x")
    for i in a:
        num.append(len(i))
    return num