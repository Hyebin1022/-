# 장군개미는 5의 공격력을, 병정개미는 3의 공격력을 일개미는 1
def solution(hp):
    general = hp // 5
    soldier = (hp-(5*general))//3
    work = (hp-(5*general)-(3*soldier))//1
    
    return general+soldier+work