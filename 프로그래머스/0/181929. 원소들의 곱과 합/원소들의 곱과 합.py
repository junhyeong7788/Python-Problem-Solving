def solution(num_list):
    mul_num = 1
    sum_num = 0
    for i in num_list:
        mul_num *= i
        sum_num += i
    return 1 if mul_num < sum_num * sum_num else 0