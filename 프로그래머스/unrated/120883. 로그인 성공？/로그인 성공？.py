def solution(id_pw, db):
    if id_pw in db:
        return "login"
    else:
        for element in db:
            if id_pw[0] == element[0]:
                return "wrong pw"
        return "fail"
