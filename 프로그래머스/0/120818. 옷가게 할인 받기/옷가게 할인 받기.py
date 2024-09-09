def solution(price):
    if price >= 500000:
        return int(price - (price*0.2))
    elif price >= 300000 and price < 500000:
        return int(price - (price*0.1))
    elif price >= 100000 and price < 300000:
        return int(price - (price*0.05))
    else : 
        return int(price)