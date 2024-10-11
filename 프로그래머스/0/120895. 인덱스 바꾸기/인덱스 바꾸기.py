def solution(my_string, num1, num2):
    strList = list(my_string)
    strList[num1], strList[num2] = strList[num2], strList[num1]
    return ''.join(strList)