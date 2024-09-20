def solution(sides):
    max_num = max(sides)
    sides.remove(max_num)
    sum_list = sum(sides)
    return 1 if max_num < sum_list else 2