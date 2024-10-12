# [level 0] 문자열 정렬하기 (2) - 120911 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120911) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.02 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 10월 12일 14:59:18

### 문제 설명

<p>영어 대소문자로 이루어진 문자열 <code>my_string</code>이 매개변수로 주어질 때, <code>my_string</code>을 모두 소문자로 바꾸고 알파벳 순서대로 정렬한 문자열을 return 하도록 solution 함수를 완성해보세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>0 &lt; <code>my_string</code> 길이 &lt; 100</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>my_string</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"Bcad"</td>
<td>"abcd"</td>
</tr>
<tr>
<td>"heLLo"</td>
<td>"ehllo"</td>
</tr>
<tr>
<td>"Python"</td>
<td>"hnopty"</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>"Bcad"를 모두 소문자로 바꾸면 "bcad"이고 이를 알파벳 순으로 정렬하면 "abcd"입니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>"heLLo"를 모두 소문자로 바꾸면 "hello"이고 이를 알파벳 순으로 정렬하면 "ehllo"입니다.</li>
</ul>

<p>입출력 예 #3</p>

<ul>
<li>"Python"를 모두 소문자로 바꾸면 "python"이고 이를 알파벳 순으로 정렬하면 "hnopty"입니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- 문자열 자체는 정렬이 불가능하다. 하지만 `sorted()`는 문자열을 리스트처럼 취급하여 각 문자를 정렬한 리스트로 반환한다.

### 💻 접근법
인사이트 : 변수 선언, `lower()`, `sorted()`, `''.join()`등을 이용하여 풀이

### 📝 슈도코드
```
def solution(문자열 my_string을 매개변수로 받는다):
    lowStr 변수 선언 = my_string문자열을 소문자로 바꾼다.
    strList 변수 선언 = lowStr문자열을 리스트로 만든다.
    return strList를 알파벳순서로 정렬한 후 문자열로 결합한 값을 반환
```
```python
# 풀이 코드
def solution(my_string):
    lowStr = my_string.lower()
    strList = list(lowStr)
    return ''.join(sorted(strList))
```

### 👍 다른 정답 코드
1.
```python
def solution(my_string):
    return ''.join(sorted(my_string.lower()))
```
- `sorted()` : 이터러블 객체를 입력으로 받아, 그 내부 요소를 정렬한 후 새로운 리스트로 반환
    - 문자열을 입력으로 받으면, 문자열을 리스트로 변환하여 각 문자를 개별적으로 정렬한 후 그 결과를 반환
