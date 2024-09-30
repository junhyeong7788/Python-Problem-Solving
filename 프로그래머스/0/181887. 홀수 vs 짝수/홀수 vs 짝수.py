def solution(num_list):
    odd_list_sum = sum(num_list[0::2])
    even_list_sum = sum(num_list[1::2])
    return odd_list_sum if odd_list_sum > even_list_sum else even_list_sum