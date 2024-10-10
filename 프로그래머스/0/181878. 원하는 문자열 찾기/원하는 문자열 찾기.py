def solution(myString, pat):
    upStr = pat.upper()
    up_myStr = myString.upper()
    return int(upStr in up_myStr)

