def solution(sides):
    max_num = max(sides)
    del_num = sides.remove(max_num)
    sum_list = sum(sides)
    if max_num < sum_list :
        return 1
    else :
        return 2
