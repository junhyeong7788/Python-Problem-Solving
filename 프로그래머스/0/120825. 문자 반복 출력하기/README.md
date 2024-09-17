# [level 0] 문자 반복 출력하기 - 120825 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120825) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 17일 23:00:24

### 문제 설명

<p>문자열 <code>my_string</code>과 정수 <code>n</code>이 매개변수로 주어질 때, <code>my_string</code>에 들어있는 각 문자를 <code>n</code>만큼 반복한 문자열을 return 하도록 solution 함수를 완성해보세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>2 ≤ <code>my_string</code> 길이 ≤ 5</li>
<li>2 ≤ <code>n</code> ≤ 10</li>
<li>"my_string"은 영어 대소문자로 이루어져 있습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>my_string</th>
<th>n</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"hello"</td>
<td>3</td>
<td>"hhheeellllllooo"</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>"hello"의 각 문자를 세 번씩 반복한 "hhheeellllllooo"를 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- `.join()` : 여러 문자열을 빈 문자열('')을 기준으로 합쳐서 하나의 문자열로 만들어준다.

### 💻 접근법
인사이트 : 문자열 반복 파이썬이라는 키워드로 구글검색하여 .join매서드를 이용하여 풀이하게 되었다.

### 📝 슈도코드
```
def solution(매개변수로 my_string리스트와 n을 받는다):
    return 빈문자열을 기준으로 합쳐서 하나의 문자열로 만듬 [i를 n번 반복 , 각 문자를 하나씩 i에 할당하며 순회]
```
```python
# 풀이 코드
def solution(my_string, n):
    return ''.join([i * n for i in my_string])
```
```python
# 제너레이터 표현식으로 사용
def solution(my_string, n):
    return ''.join(i*n for i in my_string)
```
### 👍 다른 정답 코드
1.
```python
def solution(my_string, n):
    answer = ''
    for m in my_string:
        answer += (m * n)
    return answer
```
