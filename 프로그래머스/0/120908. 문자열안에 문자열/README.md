# [level 0] 문자열안에 문자열 - 120908 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120908) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 10월 06일 03:33:50

### 문제 설명

<p>문자열 <code>str1</code>, <code>str2</code>가 매개변수로 주어집니다. <code>str1</code> 안에 <code>str2</code>가 있다면 1을 없다면 2를 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>str1</code>의 길이 ≤ 100</li>
<li>1 ≤ <code>str2</code>의 길이 ≤ 100</li>
<li>문자열은 알파벳 대문자, 소문자, 숫자로 구성되어 있습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>str1</th>
<th>str2</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"ab6CDE443fgh22iJKlmn1o"</td>
<td>"6CD"</td>
<td>1</td>
</tr>
<tr>
<td>"ppprrrogrammers"</td>
<td>"pppp"</td>
<td>2</td>
</tr>
<tr>
<td>"AbcAbcA"</td>
<td>"AAA"</td>
<td>2</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>"ab<code>6CD</code>E443fgh22iJKlmn1o" <code>str1</code>에 <code>str2</code>가 존재하므로 1을 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>"ppprrrogrammers" <code>str1</code>에 <code>str2</code>가 없으므로 2를 return합니다.</li>
</ul>

<p>입출력 예 #3</p>

<ul>
<li>"AbcAbcA" <code>str1</code>에 <code>str2</code>가 없으므로 2를 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- not in, in, int()

### 💻 접근법
인사이트 : 불리언 연산자를 사용하여 문제에 지정된 반환값 반환

### 📝 슈도코드
```
def solution(문자열 str1과 str2를 매개변수로 받는다):
    return str2가 str1안에 있다면 1을 반환 없으면 2를 반환
```
```python
# 풀이 코드
def solution(str1, str2):
    return 1 if str2 in str1 else 2
```
```python
def solution(str1, str2):
    if str2 in str1:
        return 1
    else:
        return 2
```
### 👍 다른 정답 코드
1.
```python
def solution(str1, str2):
    return 1 + int(str2 not in str1) 
```
