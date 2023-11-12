#def solution(myString):
#    return sorted(myString.split('x'))

def solution(myString):
    return sorted(filter(None, myString.split('x')))