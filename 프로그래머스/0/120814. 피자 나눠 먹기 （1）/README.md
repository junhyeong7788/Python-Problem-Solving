# [level 0] 피자 나눠 먹기 (1) - 120814 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120814) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 11일 23:22:02

### 문제 설명

<p>머쓱이네 피자가게는 피자를 일곱 조각으로 잘라 줍니다. 피자를 나눠먹을 사람의 수 <code>n</code>이 주어질 때, 모든 사람이 피자를 한 조각 이상 먹기 위해 필요한 피자의 수를 return 하는 solution 함수를 완성해보세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>n</code> ≤ 100</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>n</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>7</td>
<td>1</td>
</tr>
<tr>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>15</td>
<td>3</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>7명이 최소 한 조각씩 먹기 위해서 최소 1판이 필요합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>1명은 최소 한 조각을 먹기 위해 1판이 필요합니다.</li>
</ul>

<p>입출력 예 #3</p>

<ul>
<li>15명이 최소 한 조각씩 먹기 위해서 최소 3판이 필요합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- math모듈 : `math.ceil()`

### 💻 접근법
인사이트 : 7의 배수
- 몫을 출력해야한다고 생각

### 📝 슈도코드
```
함수 solution 정의 (매개변수 n):
    if n을 7로 나눈 나머지가 0과 일치한다면:
        n // 7의 값을 반환
    else:
        n // 7 + 1 값을 반환
```

```python
# 풀이 코드
def solution(n):
    if n % 7 == 0:
        return n // 7
    else  :
        return n // 7 + 1
```

### 👍 다른 정답 코드
1.
```python
import math

def solution(n):
    return math.ceil(n/7)
```
- math 모듈 : 수학적 계산을 위한 다양한 함수와 상수를 제공
- `math.ceil()` : ()안의 있는 결과를 올림처리 한다.
    - `math.ceil( n / 7)` 일때 n이 15이면 15 / 7은 약 2.14가 되고, 올림 처리하여 값은 3이된다.
