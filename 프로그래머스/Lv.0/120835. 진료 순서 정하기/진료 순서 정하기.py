def solution(emergency):
    answer = []
    aa = sorted (emergency , reverse = True)
    for i in emergency: ## 이 부분 다시 공부
        answer.append(aa.index(i)+1)
    return answer