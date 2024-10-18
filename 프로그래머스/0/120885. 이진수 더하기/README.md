# [level 0] 이진수 더하기 - 120885 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120885) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 10월 18일 18:13:42

### 문제 설명

<p>이진수를 의미하는 두 개의 문자열 <code>bin1</code>과 <code>bin2</code>가 매개변수로 주어질 때, 두 이진수의 합을 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>return 값은 이진수를 의미하는 문자열입니다.</li>
<li>1 ≤ <code>bin1</code>, <code>bin2</code>의 길이 ≤ 10</li>
<li><code>bin1</code>과 <code>bin2</code>는 0과 1로만 이루어져 있습니다.</li>
<li><code>bin1</code>과 <code>bin2</code>는 "0"을 제외하고 0으로 시작하지 않습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>bin1</th>
<th>bin2</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"10"</td>
<td>"11"</td>
<td>"101"</td>
</tr>
<tr>
<td>"1001"</td>
<td>"1111"</td>
<td>"11000"</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>10 + 11 = 101 이므로 "101" 을 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>1001 + 1111 = 11000 이므로 "11000"을 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- `bin(answer)[2:]`: 문자열의 3번째 문자부터 끝까지의 부분을 반환
    - `bin()` : 정수를 이진수 문자열로 변환하는 함수

### 💻 접근법
인사이트 : 10진수 변환 -> 계산 후 -> 2진수 변환

### 📝 슈도코드
```
def solution(두개의 문재열 bin1과 bin2를 매개변수로 받는다):
    answer 변수 선언 = bin1 이진수 값
    return 
```
```python
# 풀이 코드
def solution(bin1, bin2):
    return bin(int(bin1, 2) + int(bin2, 2))[2:]
```
```
def solution(bin1, bin2):
    answer = int(bin1, 2) + int(bin2, 2)
    return bin(answer)[2:]
```
- `int(bin1, 2)와 int(bin2, 2)` : 이진수 문자열을 10진수로 변환하는 코드
- `bin(answer)[2:]`: 문자열의 3번째 문자부터 끝까지의 부분을 반환
    - `bin()` : 정수를 이진수 문자열로 변환하는 함수
