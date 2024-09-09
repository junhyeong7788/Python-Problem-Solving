# [level 0] 짝수는 싫어요 - 120813 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120813) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 09일 11:01:55

### 문제 설명

<p>정수 <code>n</code>이 매개변수로 주어질 때, <code>n</code> 이하의 홀수가 오름차순으로 담긴 배열을 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>n</code> ≤ 100</li>
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
<td>10</td>
<td>[1, 3, 5, 7, 9]</td>
</tr>
<tr>
<td>15</td>
<td>[1, 3, 5, 7, 9, 11, 13, 15]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 #1</p>

<ul>
<li>10 이하의 홀수가 담긴 배열 [1, 3, 5, 7, 9]를 return합니다.</li>
</ul>

<p>입출력 #1</p>

<ul>
<li>15 이하의 홀수가 담긴 배열 [1, 3, 5, 7, 9, 11, 13, 15]를 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- for loop, if문, list comprehension

### 💻 접근법
인사이트 : 프로그래머스 18137. n의 배수
- 해당 문제는 정수 num과 n이 매개변수로 주어질 때, num이 n의 배수이면 1을 return n의 배수가 아니라면 0을 return하는 함수를 작성하는 것이다.
- 이 문제와 다르게 홀수만 찾아서 배열에 추가하면 되는 것이다.

### 📝 슈도코드
```
def solution함수이름 (n):
    answer배열 변수 = []
    for i in range( 변수 n + 1 ):
        if i를 2로 나눴을때 나머지가 1일때:
            answer배열에 i를 추가
    return answer배열 변수
```

```python
# 풀이 코드
def solution(n):
    answer = []
    for i in range(n+1):
        if i % 2 == 1:
            answer.append(i)
    return answer
```
- for루프와 조건문을 사용하여 의도를 명확하게 표현하여 이해하기 쉬운 코드 스타일

### 👍 다른 정답 코드
```python
def solution(n):
    return [x for x in range(n + 1) if x % 2]
### 슈도 코드
함수 정의 solution(n):
    return [ 3. x를 리스트로 추가 , 1. 0부터 n까지 각 숫자 x에 대해, 2. if x를 2로 나눈 나머지가 1이면]
###
```
- 리스트 컴프리헨션을 사용하여 짧고 간결하게 작성되었다.
- range(n+1)을 반복하면서 각 요소 x에 대해 if x % 2조건을 검사함
- 이 조건은 x가 홀수일 때 True(1)가 반환
