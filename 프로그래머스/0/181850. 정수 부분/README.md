# [level 0] 정수 부분 - 181850 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181850) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 10월 10일 20:25:53

### 문제 설명

<p>실수 <code>flo</code>가 매개 변수로 주어질 때, <code>flo</code>의 정수 부분을 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>0 ≤ <code>flo</code> ≤ 100</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>flo</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>1.42</td>
<td>1</td>
</tr>
<tr>
<td>69.32</td>
<td>69</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>1.42의 정수 부분은 1입니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>69.32의 정수 부분은 69입니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- `int()`

### 💻 접근법
인사이트 : 형변환으로 간단하게 풀이

### 📝 슈도코드
```
def solution(실수 flo를 매개변수로 받는다):
    return flo를 int형으로 변환한 값을 반환
```
```python
# 풀이 코드
def solution(flo):
    return int(flo)
```

### 👍 다른 정답 코드
1.
```python
def solution(flo):
    return flo//1
```
- `//연산자` : 버림 나눗셈(floor division)
- flo를 1로 나눈 후, 결과를 소수점 아래를 버리고 가장 가까운 작거나 같은 정수를 반환
- 하지만 해당 코드의 결과는 float 타입이고 음수일 때 더 작은 정수로 내림(floor)을 한다.
    - `-3.7 // 1 = -4.0`
