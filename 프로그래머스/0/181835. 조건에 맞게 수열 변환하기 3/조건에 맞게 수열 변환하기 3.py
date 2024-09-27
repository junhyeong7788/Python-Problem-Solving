def solution(arr, k):
    return [k + val if k % 2 == 0 else k * val for val in arr]