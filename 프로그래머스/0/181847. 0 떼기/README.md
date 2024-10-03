# [level 0] 0 떼기 - 181847 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181847) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 10월 04일 02:43:23

### 문제 설명

<p>정수로 이루어진 문자열 <code>n_str</code>이 주어질 때, <code>n_str</code>의 가장 왼쪽에 처음으로 등장하는 0들을 뗀 문자열을 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>2 ≤ <code>n_str</code> ≤ 10</li>
<li><code>n_str</code>이 "0"으로만 이루어진 경우는 없습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>n_str</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"0010"</td>
<td>"10"</td>
</tr>
<tr>
<td>"854020"</td>
<td>"854020"</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>"0010"의 가장 왼쪽에 연속으로 등장하는 "0"을 모두 제거하면 "10"이 됩니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>"854020"는 가장 왼쪽에 0이 없으므로 "854020"을 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- strip메소드로 문자열 삭제
    -  `lstrip()` : 왼쪽 끝단의 불필요한 문자열을 삭제
    -  `strip()` : 양 끝단의 불필요한 문자열을 삭제
    -  `rstip()` : 오른쪽 끝단의 불필요한 문자열을 삭제

### 💻 접근법
인사이트 : `lstrip()` 함수 사용하여 풀이

### 📝 슈도코드
```
def solution(문자열 n_str를 매개변수로 받는다):
    return n_str 문자열의 왼쪽 0을 모두 제거한 값을 반환
```
```python
# 풀이 코드
def solution(n_str):
    return n_str.lstrip('0')
```

### 👍 다른 정답 코드
1.
```python
def solution(n_str):
    for i in range(len(n_str)):
        if n_str[i] != "0":
            return n_str[i:]
```
```
def solution(문자열 n_str를 매개변수로 받는다):
    for n_str의 문자열 길이 만큼 각 요소를 순회한다.
        if n_str 문자열의 [i]번쨰 인덱스에 0이 없으면 
            return 해당 인덱스부터 끝까지의 부분 문자열을 반환
```
