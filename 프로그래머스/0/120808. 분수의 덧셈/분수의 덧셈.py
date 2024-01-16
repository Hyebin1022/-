# 내가 생각한 과정 GPT에 쳐서 만든 코드

def gcd(a, b):  #최대공약수 구하기
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):  #최소 공배수 구하기
    return a * b // gcd(a, b) 

def solution(numer1, denom1, numer2, denom2):
    common_denom = lcm(denom1, denom2) #분모 최소공배수

    # 분자변환
    new_numer1 = numer1 * (common_denom // denom1)
    new_numer2 = numer2 * (common_denom // denom2)

    # 분자 값 더하기
    result_numer = new_numer1 + new_numer2

    # 최종적으로 최대공약수로 나누기
    common_factor = gcd(result_numer, common_denom)

    return [result_numer // common_factor, common_denom // common_factor]

#def solution(denum1, num1, denum2, num2):
#    a = num1 * num2
#    b = denum1 * num2 + denum2 * num1
#    
#    start = max(a, b)
#    gcd_value = 1
#    
#    for num in range(start, 0, -1):
#        if a % num == 0 and b % num == 0:
#            gcd_value = num
#            break

    answer = [b / gcd_value, a / gcd_value]
    return answer


