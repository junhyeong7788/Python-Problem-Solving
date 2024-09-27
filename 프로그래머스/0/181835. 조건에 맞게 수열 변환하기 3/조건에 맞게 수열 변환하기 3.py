def solution(arr, k):
    answer = []
    
    if k % 2 == 0:
        for val in arr:
            answer.append(k + val)
    else:
        for val in arr:
            answer.append(k * val)
    return answer
            