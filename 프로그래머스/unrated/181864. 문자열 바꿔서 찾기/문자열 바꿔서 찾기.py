def solution(myString, pat):
    answer = 0
    newString = ""
    
    for a in myString:
        if a == "A":
            newString += "B"
        else:
            newString += "A"
    
    if pat in newString:
        return 1
    else:
        return 0

