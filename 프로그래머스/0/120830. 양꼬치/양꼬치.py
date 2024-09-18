def solution(n, k):
    lambSkewers = 12000
    drink = 2000
    payment = (lambSkewers * n) + (drink * k)
    discount = (n//10) * 2000
    
    return payment-discount if n >= 10 else payment