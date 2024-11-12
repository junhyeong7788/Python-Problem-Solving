def solution(myString):
    split_strings = myString.split("x")
    result = [len(part) for part in split_strings]
    return result