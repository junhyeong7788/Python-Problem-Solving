# [level 0] 배열 만들기 2 - 181921 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181921?language=python3) 

### 성능 요약

메모리: 10.3 MB, 시간: 723.95 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 10월 12일 15:40:36

### 문제 설명

<p>정수 <code>l</code>과 <code>r</code>이 주어졌을 때, <code>l</code> 이상 <code>r</code>이하의 정수 중에서 숫자 "0"과 "5"로만 이루어진 모든 정수를 오름차순으로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.</p>

<p>만약 그러한 정수가 없다면, -1이 담긴 배열을 return 합니다.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>l</code> ≤ <code>r</code> ≤ 1,000,000</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>l</th>
<th>r</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>5</td>
<td>555</td>
<td>[5, 50, 55, 500, 505, 550, 555]</td>
</tr>
<tr>
<td>10</td>
<td>20</td>
<td>[-1]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>5 이상 555 이하의 0과 5로만 이루어진 정수는 작은 수부터 5, 50, 55, 500, 505, 550, 555가 있습니다. 따라서 [5, 50, 55, 500, 505, 550, 555]를 return 합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>10 이상 20 이하이면서 0과 5로만 이루어진 정수는 없습니다. 따라서 [-1]을 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 💻 접근법
인사이트 : 조건에 맞는 리스트 생성, 불리안 연산자로 해당 조건 값이 들어있는지 여부 판단

### 📝 슈도코드
```
def solution(정수 l과 r을 매개변수로 받는다):
    answer 변수 선언
    for l ~ r+1의 리스트 생성 후 요소 반복:
        if 숫자를 문자로 바꾼 후 '0'과 '5'에 속하는 경우에만 True를 반환
            answer리스트에 i를 추가
    if answer의 길이가 0이면
        answer.append(-1)
    return answer 리스트 반환
```
```python
# 풀이 코드
def solution(l, r):
    answer = []
    
    for i in range(l, r+1):
        if all(num in ['0', '5'] for num in str(i)):
            answer.append(i)
    
    if len(answer) == 0:
        answer.append(-1)
    return answer
```
- `all(num in ['0', '5'] for num in str(i)):`
    - `for i in str(i)`: 숫자를 문자열로 변환한 후, 각 문자를 순차적으로 검사
    - `num in ['0', '5']:`: 각 문자가 0 또는 5에 속하는지 확인
    - `all()` : 모든 문자가 '0' 또는 '5'에 속하는 경우에만 True를 반환
- 문제 조건에서 10이상이면서 20이하인 리스트 안에는 0과 5로만 이루어진 정수는 없다.
    - 이 조건은 `len(answer)==0` 으로 해결할 수 있다.

### 👍 다른 정답 코드
1.
```python
def solution(l, r):
    answer = []
    for num in range(l, r + 1):
        if not set(str(num)) - set(['0', '5']):
            answer.append(num)
    return answer if answer else [-1]
```
- `if not set(str(num)) - set(['0', '5']):`
    - `set(str(num))` : 문자열의 각 문자를 집합으로 변환, 집합은 중복되지 않는 값들로 이루어지기 때문에 num에 포함된 각 숫자를 유일하게 나타낸다.
    - `set(str(num)) - set(['0', '5']):` : num의 문자가 0과  5이외의 숫자를 포함하는지 확인하는 방법
    - `not set(str(num)) - set(['0', '5'])` : 차집합이 존재하지 않는 경우 (not)을 의미
