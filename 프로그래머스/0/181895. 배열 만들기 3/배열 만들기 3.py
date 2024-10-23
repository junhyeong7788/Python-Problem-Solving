def solution(arr, intervals):
    return [arr[i:j+1] for i, j in intervals][0] + [arr[i:j+1] for i, j in intervals][1]