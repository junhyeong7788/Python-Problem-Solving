def solution(s):
    p_count = s.lower().count('p')
    s_count = s.lower().count('y')
    print(p_count, s_count)
    if p_count != s_count:
        return False
    else:
        return True
