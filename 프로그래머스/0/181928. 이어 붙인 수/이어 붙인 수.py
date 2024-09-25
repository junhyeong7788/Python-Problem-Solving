def solution(num_list): 
    odd_num = []
    even_num = []

    for i in num_list:
        if i % 2 == 0:
            even_num.append(i)
        else :
            odd_num.append(i)

    return int(''.join(map(str, even_num))) + int(''.join(map(str, odd_num)))
            
            