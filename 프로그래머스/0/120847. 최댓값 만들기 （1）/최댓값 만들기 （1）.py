def solution(numbers):
    first_max_num = max(numbers)
    numbers.remove(first_max_num)
    second_max_num = max(numbers)
    return first_max_num * second_max_num