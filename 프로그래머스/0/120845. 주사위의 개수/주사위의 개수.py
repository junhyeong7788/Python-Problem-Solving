from math import prod

def solution(box, n):
    return prod((i//n) for i in box)