# [level 0] 공배수 - 181936 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181936) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 04일 23:44:58

### 문제 설명

<p>정수 <code>number</code>와 <code>n</code>, <code>m</code>이 주어집니다. <code>number</code>가 <code>n</code>의 배수이면서 <code>m</code>의 배수이면 1을 아니라면 0을 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>10 ≤ <code>number</code> ≤ 100</li>
<li>2 ≤ <code>n</code>, <code>m</code> &lt; 10</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>number</th>
<th>n</th>
<th>m</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>60</td>
<td>2</td>
<td>3</td>
<td>1</td>
</tr>
<tr>
<td>55</td>
<td>10</td>
<td>5</td>
<td>0</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>60은 2의 배수이면서 3의 배수이기 때문에 1을 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>55는 5의 배수이지만 10의 배수가 아니기 때문에 0을 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND

### 💻 접근법
인사이트 : 공배수

### 📝 슈도코드
```
def solution함수(정수number, n의 배수, m의 배수):
    정답 변수 = 0
    if ( 정수 number을 n으로 나눴을 때 값이 0과 동일하고 정수 number을 m으로 나눴을 때 값이 0과 동일하다면):
        answer 변수의 값은 1
    else:
        answer 변수의 값은 0
    answer 값을 반환
```
```python
# 풀이 코드
def solution(number, n, m):
    answer = 0
    if (number % n == 0 and number % m == 0):
        answer = 1
    else:
        answer = 0
    return answer
```

### 👍 다른 정답 코드
1.
```python
def solution(number, n, m):
    return int(number%n == 0 and number%m == 0)
```
2.
```python
def solution(number, n, m):
    return 1 if number%n==0 and number%m==0 else 0
```
