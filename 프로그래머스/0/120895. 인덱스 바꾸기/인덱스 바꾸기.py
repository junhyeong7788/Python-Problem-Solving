def solution(my_string, num1, num2):
    answer = []
    for i, v in enumerate(my_string):
        if i == num2:
            answer.append(my_string[num1])
        elif i == num1:
            answer.append(my_string[num2])
        else:
            answer.append(v)
    return ''.join(answer)