def solution(num_list):
    answer = 1
    if len(num_list) <= 10:
        for i in num_list:
            
            answer *= i
        return answer
    else:
        return sum(num_list)
