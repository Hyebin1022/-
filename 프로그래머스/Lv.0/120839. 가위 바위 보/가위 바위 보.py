#가위는 2 바위는 0 보는 5
def solution(rsp):
    result = {'2':'0','0':'5','5':'2'}
    answer = ''
    for i in rsp:
        answer += result.get(i)
    return answer