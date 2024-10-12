def solution(my_string):
    lowStr = my_string.lower()
    strList = list(lowStr)
    return ''.join(sorted(strList))