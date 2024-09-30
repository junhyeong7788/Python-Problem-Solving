# [level 0] 특정 문자 제거하기 - 120826 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120826) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 30일 21:27:26

### 문제 설명

<p>문자열 <code>my_string</code>과 문자 <code>letter</code>이 매개변수로 주어집니다. <code>my_string</code>에서 <code>letter</code>를 제거한 문자열을 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>my_string</code>의 길이 ≤ 100</li>
<li><code>letter</code>은 길이가 1인 영문자입니다.</li>
<li><code>my_string</code>과 <code>letter</code>은 알파벳 대소문자로 이루어져 있습니다.</li>
<li>대문자와 소문자를 구분합니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>my_string</th>
<th>letter</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"abcdef"</td>
<td>"f"</td>
<td>"abcde"</td>
</tr>
<tr>
<td>"BCBdbe"</td>
<td>"B"</td>
<td>"Cdbe"</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>"abcdef" 에서 "f"를 제거한 "abcde"를 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>"BCBdbe" 에서 "B"를 모두 제거한 "Cdbe"를 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- `string.replace(old, new, count)` : 파이썬 문자열 메서드로 특정 문자열을 다른 문자열로 바꿀 때 사용
    - old : 기존 문자열 / new : 대체할 문자열 (새로운 문자열) / count : 바꿀 횟수 지정

### 💻 접근법
인사이트 : 문자열 대체로 특정 문자 제거

### 📝 슈도코드
```
def solution(문자열 my_string과 문자 letter을 매개변수로 받는다):
    return 문자열 my_string에 letter문자를 "" 공백으로 대체한(삭제) 값을 반환
```
```python
# 풀이 코드
def solution(my_string, letter):
    return my_string.replace(letter, "")
```
