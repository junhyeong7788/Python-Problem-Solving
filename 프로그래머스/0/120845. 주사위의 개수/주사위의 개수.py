from math import prod

def solution(box, n):
    return prod(int(i/n) for i in box)