def solution(arr):
    answer = []
    previous = None  
    for i in arr:
        if i != previous:
            answer.append(i)
            previous = i
    return answer