def solution(arr, idx):
    answer = [i for i, a in enumerate(arr) if a == 1 and i >= idx]
    return min(answer) if answer != [] else -1