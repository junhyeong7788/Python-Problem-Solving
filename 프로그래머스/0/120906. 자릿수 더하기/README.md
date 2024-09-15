# [level 0] 자릿수 더하기 - 120906 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120906) 

### 성능 요약

메모리: 10.3 MB, 시간: 0.02 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 15일 23:03:05

### 문제 설명

<p>정수 <code>n</code>이 매개변수로 주어질 때 <code>n</code>의 각 자리 숫자의 합을 return하도록 solution 함수를 완성해주세요</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>0 ≤ <code>n</code> ≤ 1,000,000</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>n</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>1234</td>
<td>10</td>
</tr>
<tr>
<td>930211</td>
<td>16</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>1 + 2 + 3 + 4 = 10을 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>9 + 3 + 0 + 2 + 1 + 1 = 16을 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- for loop에는 문자열, 리스트, 튜플과 같은 반복 가능한 객체에서만 사용할 수 있다.
- `sum()`

### 💻 접근법
인사이트 : for loop를 사용하여 문자열 n의 자릿수를 읽어 answer 변수에 더하려고 하였다.

### 🚫 문제해결 중 발생한 에러
1. `for i in n` : `TypeError: 'int' object is not iterable` 파이썬에서 반복 가능한 객체가 아닌 것을 반복하려고 할 때 발생하는 에러
2. `answer += i` : `TypeError: unsupported operand type(s) for +=: 'int' and 'str'` 숫자 (int)와 문자열 (str)을 더하려고 시도할 때 발생하는 에러

### 📝 슈도코드
```
def solution함수(매개변수 n):
    변수 answer를 0으로 초기화
    n을 문자열로 변환하여 str_n에 저장
    for str_n의 각 문자 i에 대해 반복:
        i를 정수로 변환한 값을 answer에 더한다.
    return answer를 반환
```
```python
# 풀이 코드
def solution(n):
    answer = 0
    str_n = str(n)
    for i in str_n:
        answer += int(i)
    return answer
```

### 👍 다른 정답 코드
1.
```python
def solution(n):
    return sum(int(i) for i in str(n))
```
- 내장함수 sum() 사용
- `int(i) for i in str(n)` : 리스트 컴프리헨션 방식, str(n)에서 각 문자를 정수로 변환한 리스트를 만듬
