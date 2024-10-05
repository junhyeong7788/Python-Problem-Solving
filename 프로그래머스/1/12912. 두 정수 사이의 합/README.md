# [level 1] 두 정수 사이의 합 - 12912 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12912) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 10월 06일 03:53:17

### 문제 설명

<p>두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요. <br>
예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.</p>

<h5>제한 조건</h5>

<ul>
<li>a와 b가 같은 경우는 둘 중 아무 수나 리턴하세요.</li>
<li>a와 b는 -10,000,000 이상 10,000,000 이하인 정수입니다.</li>
<li>a와 b의 대소관계는 정해져있지 않습니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>a</th>
<th>b</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>3</td>
<td>5</td>
<td>12</td>
</tr>
<tr>
<td>3</td>
<td>3</td>
<td>3</td>
</tr>
<tr>
<td>5</td>
<td>3</td>
<td>12</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- `abs()` : 주어진 수의 절대값을 반환 / 정수, 실수, 복소수의 절대값을 계산하는 데 사용될 수 있으며, 매우 간단하고 직관적인 기능을 제공

### 💻 접근법
인사이트 : a와 b의 순서에 상관없이 a와 b를 포함한 사이에 속한 모든 정수의 합을 리턴해야한다.
- if문을 사용하여 리스트 생성 후 합을 구하는 방법으로 풀이
- 다른 정답 코드에서 `abs()`함수를 사용하면 시간이 0.00ms가 나온다.

### 📝 슈도코드
```
def solution(두 정수 a와 b를 매개변수로 받는다):
    if a가 b보다 크면
        return a~b+1의 리스트를 생성하여 리스트의 합을 반환
    else b가 a보다 크면
        return b~a+1의 리스트를 생성하여 리스트의 합을 반환
```
```python
# 풀이 코드
def solution(a, b):
    if a < b:
        return sum(range(a, b+1))
    else :
        return sum(range(b, a+1))
```

### 👍 다른 정답 코드
1.
```python
def solution(a, b):
    return sum(range(min(a, b), max(a, b)+1))
```
- min, max 함수를 사용하여 a와 b 사이의 모든 수를 생성
2.
```python
def solution(a, b):
    return (abs(a-b)+1)*(a+b)//2
```
- 등차수열의 합 공식을 사용 : $S = \frac{n}{2} \times (a_1 + a_n)$, n은 항의 수, a_1 과 a_n은 첫 항과 마지막 항
    - `abs(a-b)+1` : a와 b사이의 숫자 개수를 계산하고 (a+b)//2는 첫 항과 마지막 항의 평균을 구한다.
