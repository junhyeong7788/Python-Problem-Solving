# [level 0] 두 수의 차 - 120803 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120803?language=python3) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 02일 11:17:52

### 문제 설명

<p>정수 <code>num1</code>과 <code>num2</code>가 주어질 때, <code>num1</code>에서&nbsp;<code>num2</code>를 뺀 값을 return하도록 soltuion 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>-50000 ≤ <code>num1</code> ≤ 50000</li>
<li>-50000 ≤ <code>num2</code> ≤ 50000</li>
</ul>

<hr>

<h4>입출력 예</h4>
<table class="table">
        <thead><tr>
<th>num1</th>
<th>num2</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>2</td>
<td>3</td>
<td>-1</td>
</tr>
<tr>
<td>100</td>
<td>2</td>
<td>98</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li><code>num1</code>이 2이고 <code>num2</code>가 3이므로 2 - 3 = -1을 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li><code>num1</code>이 100이고 <code>num2</code>가 2이므로 100 - 2 = 98을 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 풀이 추가
```python
# 첫번째 풀이
def solution(num1, num2):
        answer = num1 - num2
        return answer
```
```python
# 두번째 풀이 (제한사항 추가)
def solution(num1, num2):
    def validate_input(x, lower, upper):
        if x >= lower and x <= upper:
            return True
        return False
    num_list = [num1, num2]
    assert all([validate_input(x, -50000, 50000) for x in num_list])
    answer = num1 - num2
    return answer
```
- 가정 설정문(assert) 사용
- all 함수는 리스트의 모든 요수가 True일 경우에만 True를 반환  
    - 만약 num1이나 num2 중 하나라도 범위를 벗어나면 False가 되어 AssertionError가 발생
- 입력값이 지정된 범위 내에 있는지 확인하기 위한 안전장치 역할을 한다고 생각하면 된다.
```python
# 추가 풀이
solution = lambda num1, num2 : num1 - num2
```
- [람다 표현식 TIL](https://github.com/junhyeong7788/TIL/blob/8678e0012d9a0abaf93d78b318540452772bf607/Python/lambda(%EB%9E%8C%EB%8B%A4).md)
