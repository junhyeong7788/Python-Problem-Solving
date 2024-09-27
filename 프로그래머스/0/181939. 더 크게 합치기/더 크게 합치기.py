def solution(a, b):
    str1 = str(a) + str(b) 
    str2 = str(b) + str(a)
    if str1 > str2 :
        return int(str1)
    elif str1 < str2:
        return int(str2)
    else :
        return int(str1)
