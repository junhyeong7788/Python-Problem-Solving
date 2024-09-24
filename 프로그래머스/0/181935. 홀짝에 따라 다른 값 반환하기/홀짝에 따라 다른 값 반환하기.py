def solution(n):
    odd_answer = [] 
    even_answer = []
    
    if n % 2 == 1:
        for i in range(n+1):
            if i % 2 == 1:
                odd_answer.append(i)
        return sum(odd_answer)
    else : 
        for i in range(n+1):
            if i % 2 == 0:
                even_answer.append(i**2)
        return sum(even_answer)