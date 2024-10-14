def solution(n):
    pairs_count = 0
    for a in range(1, int(n**0.5) + 1):
        if n % a == 0:
            pairs_count += 1  
            if a != n // a:  
                pairs_count += 1  
    return pairs_count