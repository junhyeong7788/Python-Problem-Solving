def solution(n):
    sqrt_num = n**(1/2)
    if n % sqrt_num == 0:
        return (sqrt_num+1)**2
    else:
        return -1