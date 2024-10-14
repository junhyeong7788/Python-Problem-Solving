def solution(num, k):
    k_str = str(k)
    num_str = str(num)  
    index = num_str.find(k_str)
    return index + 1 if index != -1 else -1