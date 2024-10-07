# [level 1] 정수 제곱근 판별 - 12934 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12934) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.02 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 10월 07일 15:59:59

### 문제 설명

<p>임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.<br>
n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.</p>

<h5>제한 사항</h5>

<ul>
<li>n은 1이상,  50000000000000 이하인 양의 정수입니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>n</th>
<th style="text-align: center">return</th>
</tr>
</thead>
        <tbody><tr>
<td>121</td>
<td style="text-align: center">144</td>
</tr>
<tr>
<td>3</td>
<td style="text-align: center">-1</td>
</tr>
</tbody>
      </table>
<h6>입출력 예 설명</h6>

<p><strong>입출력 예#1</strong><br>
121은 양의 정수 11의 제곱이므로, (11+1)를 제곱한 144를 리턴합니다.</p>

<p><strong>입출력 예#2</strong><br>
3은 양의 정수의 제곱이 아니므로, -1을 리턴합니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- n의 제곱근(루트) : `2**(1/2)`
- `sqrt_num = n**(1/2)` : n이 완전제곱수인지 검사를 할때 sqrt_num이 정수일 때만 유효한 조건이다.
    - `int(n**(1/2))`로 개선

### 💻 접근법
인사이트 : 제곱근 공식으로 풀이

### 📝 슈도코드
```
def solution(임의의 양의 정수 n을 매개변수로 받는다):
    sqrt_num의 변수를 선언 = n**(1/2)
    if 정수 n을 sqrt_num로 나누었을 때 나머지가 0일때:
        return sqrt_num에 1을 더한 값을 제곱
    else:
        return 
```
```python
# 풀이 코드
def solution(n):
    return ((n**(1/2))+1)**2 if n % (n**(1/2)) == 0 else -1
```
```python
def solution(n):
    sqrt_num = n**(1/2)
    if n % sqrt_num == 0:
        return (sqrt_num+1)**2
    else:
        return -1
```
### 👍 코드 로직 개선
```python
def solution(n):
    sqrt_num = int(n**(1/2))
    if sqrt_num * sqrt_num == n:
        return (sqrt_num + 1) ** 2
    else:
        return -1
```
- n이 완전제곱수인지 검사를 할때 sqrt_num이 정수일 때만 유효한 조건이다.
    - `int(n**(1/2))`로 개선
