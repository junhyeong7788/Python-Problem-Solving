def solution(str_list, ex):
    new_list = []
    for i in str_list:
        if ex not in i:
            new_list.append(i)
    return ''.join(new_list)


