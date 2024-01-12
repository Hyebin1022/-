# 10인분을 먹으면 음료수 하나 서비스 양꼬치는 1인분에 12,000원, 음료수는 2,000원

def solution(n, k):    
    food = n * 12000		
    
    if n >= 10:					
        drink = (k - n // 10) * 2000 
    else :
        drink = k * 2000		
    
    answer = food + drink	
    return answer