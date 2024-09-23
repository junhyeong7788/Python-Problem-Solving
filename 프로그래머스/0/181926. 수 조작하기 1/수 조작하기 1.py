def solution(n, control):
    for x in control:
        if x == "w":
            n += 1
        elif x == "a":
            n -= 10
        elif x == "s":
            n -= 1
        else:
            n += 10
    return n