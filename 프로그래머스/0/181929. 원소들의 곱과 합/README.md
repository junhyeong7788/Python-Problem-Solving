# [level 0] 원소들의 곱과 합 - 181929 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181929) 

### 성능 요약

메모리: 10.3 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 22일 00:07:20

### 문제 설명

<p>정수가 담긴 리스트 <code>num_list</code>가 주어질 때, 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>2 ≤ <code>num_list</code>의 길이 ≤ 10</li>
<li>1 ≤ <code>num_list</code>의 원소 ≤ 9</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>num_list</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[3, 4, 5, 2, 1]</td>
<td>1</td>
</tr>
<tr>
<td>[5, 7, 8, 3]</td>
<td>0</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>모든 원소의 곱은 120, 합의 제곱은 225이므로 1을 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>모든 원소의 곱은 840, 합의 제곱은 529이므로 0을 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- for loop
- `sum()`
- `reduce()` : funtools.reduce 함수는 주어진 반복 가능한 객체의 요소들을 순차적으로 누적적으로 처리하여 하나의 값으로 축소
    - reduce는 두 개의 인자를 받는 함수와 함께 사용됨, 첫 번째 인자는 누적값, 두 번째 인자는 현재값 (초기값을 제공할 수 도 있다.)
- `lambda` : 익명함수를 생성하는 데 사용, 간단한 함수를 한 줄로 정의할 수 있게 해준다.
    - 형식 : `lambda arguments: expression` / 입력 받은 arguments를 사용하여 experssion을 계산한 후 그 결과를 반환
- `math.prod()` : 입력으로 받은 반복 가능한(iterable) 객체의 모든 요소의 곱을 반환, 이 함수는 주로 숫자로 구성된 리스트나 튜플에서 모든 요소를 곱할 때 사용

### 💻 접근법
인사이트 : for loop를 사용하여 문제 풀이

### 📝 슈도코드
```
def solution(매개변수로 정수가 담긴 num_list를 받는다):
    리스트원소들의 곱을 저장할 변수 선언 = 1
    리스트원소들의 합을 저장할 변수 선언 = 0
    for i in num_list:
        리스트원소 곱 저장 변수 = 리스트원소 곱 저장 변수 + i (리스트원소순회)
        리스트원소 합 저장 변수 = 리스트원소 합 저장 변수 + i
    return 리스트원소 곱 < 리스트원소 합의 제곱일때 1을 반환, 아니면 0을 반환
```
```python
# 풀이 코드
def solution(num_list):
    mul_num = 1
    sum_num = 0
    for i in num_list:
        mul_num *= i
        sum_num += i
    return 1 if mul_num < sum_num * sum_num else 0
```

### 👍 다른 정답 코드
1.
```python
def solution(num_list):
    mul_num = 1
    square = sum(num_list) ** 2
    
    for i in num_list:
        mul_num *= i

    return 1 if mul_num < square else 0
```
- 원소들의 합의 제곱을 `sum()`을 이용하여 빠르게 구함
2.
```python
from functools import reduce

def solution(num_list):
    return 1 if (reduce(lambda x, y: x * y, num_list)) < (sum(num_list) ** 2) else 0
```
- Python의 functools.reduce함수와 lambda 표현식을 사용
- `reduce(lambda x, y: x * y, num_list)`: num_list리스트의 모든 요소를 순차적으로 곱한다.
 
3.
```python
import math
def solution(num_list):
    return 1 if math.prod(num_list) < (sum(num_list)**2) else 0
```
- math의 `prod()` 함수 사용 : 불필요한 반복문이나 다른 복잡한 구현 없이 간단하고 효율적으로 요소들의 곱을 계산할 수 있다.
