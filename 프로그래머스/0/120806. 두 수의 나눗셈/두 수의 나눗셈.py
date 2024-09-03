def solution(num1, num2):
    def validate_input(x, lower, upper):
        if lower > x and x <= upper :
            return Ture
        return False
    num_list = [num1, num2]
    assert all([validate_input(x, 0, 100)] for x in num_list)
    divide = num1 / num2 
    answer = int(divide * 1000) 
    return answer