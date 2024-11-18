# [level 1] 없는 숫자 더하기 - 86051 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/86051) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 월간 코드 챌린지 시즌3

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 11월 19일 00:32:11

### 문제 설명

<p>0부터 9까지의 숫자 중 일부가 들어있는 정수 배열 <code>numbers</code>가 매개변수로 주어집니다. <code>numbers</code>에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>numbers</code>의 길이 ≤ 9

<ul>
<li>0 ≤ <code>numbers</code>의 모든 원소 ≤ 9</li>
<li><code>numbers</code>의 모든 원소는 서로 다릅니다.</li>
</ul></li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>numbers</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[1,2,3,4,6,7,8,0]</td>
<td>14</td>
</tr>
<tr>
<td>[5,8,4,0,6,7,9]</td>
<td>6</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p><strong>입출력 예 #1</strong></p>

<ul>
<li>5, 9가 <code>numbers</code>에 없으므로, 5 + 9 = 14를 return 해야 합니다.</li>
</ul>

<p><strong>입출력 예 #2</strong></p>

<ul>
<li>1, 2, 3이 <code>numbers</code>에 없으므로, 1 + 2 + 3 = 6을 return 해야 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- if문, 정수 시퀀스 생성, 람다함수

### 💻 접근법
인사이트 : 단순히 0~9까지의 배열 요소를 반복하면서 list안에 없는 요소들만 더해 합을 구하는 방법으로 풀이

### 📝 슈도코드
```
def solution(정수 리스트 numbers를 매개변수로 받는다):
    answer 변수를 0으로 초기화

    for 0부터 9까지의 정수 시퀀스를 생성 그 요소들을 반복:
        if i가 numbers리스트 안에 없으면:
            answer 변수에 i를 더한다.

    return answer 변수의 값을 반환
```
```python
# 풀이 코드
def solution(numbers):
    answer = 0
    
    for i in range(10):
        if i not in numbers:
            answer += i
    
    return answer
```

### 👍 다른 정답 코드
1.
```python
def solution(numbers):
    return sum(range(10)) - sum(numbers)
```
- range(10)의 합에서 numbers리스트의 합을 뺀 값을 반환
- `sum(range(10))` : 값은 항상 45 = 숫자 45로 대체 가능
2.
```python
solution = lambda x: sum(range(10)) - sum(x)
```
- 람다 함수 사용 : x는 함수의 입력 값이므로 여기서는 numbers 리스트를 입력으로 받는다.
