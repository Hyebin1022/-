def solution(chicken):
    
    coupon = 0
    while True:
        service = chicken // 10
        chicken = chicken - (10*service) + service    
        coupon += service
        
        if chicken < 10:
            break
            
    return coupon