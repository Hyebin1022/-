def solution(my_string, num1, num2):
    string_list = list(my_string)
    a = string_list[num1] #a='e' 
    string_list[num1] = string_list[num2] #e를 ㅣ로
    string_list[num2] = a
    result_string = ''.join(string_list)
    return result_string