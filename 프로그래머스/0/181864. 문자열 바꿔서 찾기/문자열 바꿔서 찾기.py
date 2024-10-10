def solution(myString, pat):
    answer = "".join("B" if i == "A" else "A" for i in myString)
    return int(pat in answer)

