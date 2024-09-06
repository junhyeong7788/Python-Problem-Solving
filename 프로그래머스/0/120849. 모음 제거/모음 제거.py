def solution(my_string):
    word = ("a,e,i,o,u")
    answer = ''
    for i in my_string:
        if i not in word:
            answer+=i
    return answer

