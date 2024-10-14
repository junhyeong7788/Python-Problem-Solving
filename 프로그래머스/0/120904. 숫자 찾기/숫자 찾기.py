def solution(num, k):
    for i, v in enumerate(str(num)):
        if str(k) == v:
            return i + 1
    if str(num) not in str(k) :
        return -1