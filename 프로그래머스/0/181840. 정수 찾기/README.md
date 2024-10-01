# [level 0] 정수 찾기 - 181840 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181840) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 10월 02일 03:03:39

### 문제 설명

<p>정수 리스트 <code>num_list</code>와 찾으려는 정수 <code>n</code>이 주어질 때, <code>num_list</code>안에 <code>n</code>이 있으면 1을 없으면 0을 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>3 ≤ <code>num_list</code>의 길이 ≤ 100</li>
<li>1 ≤ <code>num_list</code>의 원소 ≤ 100</li>
<li>1 ≤ <code>n</code> ≤ 100</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>num_list</th>
<th>n</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[1, 2, 3, 4, 5]</td>
<td>3</td>
<td>1</td>
</tr>
<tr>
<td>[15, 98, 23, 2, 15]</td>
<td>20</td>
<td>0</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>[1, 2, 3, 4, 5] 안에 3이 있으므로 1을 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>[15, 98, 23, 2, 15] 안에 20이 없으므로 0을 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- 삼항연산자
- `int()` : 정수로 변환하는 함수로 불리언값을 1과 0으로 변환할 수 있다.

### 💻 접근법
인사이트 : if문을 사용, 정수리스트내에 정수n 포함 여부를 in연산자를 사용하여 풀이.

### 📝 슈도코드
```
def solution(정수리스트 num_list와 정수 n을 매개변수로 받는다):
    return num_list리스트 안에 정수 n이 있으면 1을 반환, 없으면 0을 반환
```
```python
# 풀이 코드
def solution(num_list, n):
    return 1 if n in num_list else 0
```

### 👍 다른 정답 코드
1.
```python
def solution(num_list, n):
    return int(n in num_list)
```
- `n in num_list`: 파이썬의 in연산자로, 리스트 num_list에 값 n이 포함되어 있는지 여부를 불리언 값으로 반환
- `int()` : True와 False는 파이썬에서 각각 1과 0으로 반환 될 수 있다. 따라서 int() 함수는 불리언 값을 정수 값으로 변환한다.
