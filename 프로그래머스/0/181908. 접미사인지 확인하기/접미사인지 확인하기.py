def solution(my_string, is_suffix):
    answer_list = []
    for i in range(len(my_string)):
        answer_list.append(my_string[i:])
    
    if is_suffix in answer_list:
        return 1
    else:
        return 0