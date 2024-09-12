def solution(hp):
    general = hp // 5
    soldier = (hp - (5*general)) // 3
    worker = (hp - (5*general)-(3*soldier)) // 1
    return general + soldier + worker