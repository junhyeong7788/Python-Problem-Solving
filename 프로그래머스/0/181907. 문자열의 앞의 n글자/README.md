# [level 0] 문자열의 앞의 n글자 - 181907 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181907) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 19일 14:46:21

### 문제 설명

<p>문자열 <code>my_string</code>과 정수 <code>n</code>이 매개변수로 주어질 때, <code>my_string</code>의 앞의 <code>n</code>글자로 이루어진 문자열을 return 하는 solution 함수를 작성해 주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li><code>my_string</code>은 숫자와 알파벳으로 이루어져 있습니다.</li>
<li>1 ≤ <code>my_string</code>의 길이 ≤ 1,000</li>
<li>1 ≤ <code>n</code> ≤ <code>my_string</code>의 길이</li>
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
<td>"ProgrammerS123"</td>
<td>11</td>
<td>"ProgrammerS"</td>
</tr>
<tr>
<td>"He110W0r1d"</td>
<td>5</td>
<td>"He110"</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예</h5>

<p>입출력 예 #1</p>

<ul>
<li>예제 1번의 <code>my_string</code>에서 앞의 11글자는 "ProgrammerS"이므로 이 문자열을 return 합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>예제 2번의 <code>my_string</code>에서 앞의 5글자는 "He110"이므로 이 문자열을 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- string slicing

### 💻 접근법
인사이트 : 처음에는 for문으로 풀이하려고 하였으나 풀이중에 문자열 슬라이싱이 생각나서 아주 간단하게 풀이하였다.

### 📝 슈도코드
```
def solution(매개 변수로 문자열 my_string과 n을 받는다):
    return my_sting문자열의 처음부터 n까지의 문자열 슬라이싱
```
```python
# 풀이 코드
def solution(my_string, n):
    return my_string[:n]
```

### 👍 다른 정답 코드
1.
```python
def solution(my_string, n):
    answer = ''
    for i in range(n) :
        answer += my_string[i]
    return answer
```
- `answer += my_string[i]`: my_string에서 i번째 문자를 answer에 추가한다. 
