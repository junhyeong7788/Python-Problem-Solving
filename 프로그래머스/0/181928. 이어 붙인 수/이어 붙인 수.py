def solution(num_list): 
    odd_num = [i for i in num_list if i%2 == 1]
    even_num = [i for i in num_list if i%2 == 0]
    return int(''.join(map(str, even_num))) + int(''.join(map(str, odd_num)))


    
            