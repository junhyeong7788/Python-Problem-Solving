def solution(my_string, alp):
    answer = []
    strList = list(my_string)
    for i, v in enumerate(strList):
        if v == alp:
            answer.append(v.upper())
        else:
            answer.append(v)
        
    return ''.join(answer)