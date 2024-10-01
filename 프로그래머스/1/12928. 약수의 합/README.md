# [level 1] 약수의 합 - 12928 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12928) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.16 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 10월 02일 03:23:08

### 문제 설명

<p>정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.</p>

<h5>제한 사항</h5>

<ul>
<li><code>n</code>은 0 이상 3000이하인 정수입니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>n</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>12</td>
<td>28</td>
</tr>
<tr>
<td>5</td>
<td>6</td>
</tr>
</tbody>
      </table>
<h6>입출력 예 설명</h6>

<p>입출력 예 #1<br>
12의 약수는 1, 2, 3, 4, 6, 12입니다. 이를 모두 더하면 28입니다.</p>

<p>입출력 예 #2<br>
5의 약수는 1, 5입니다. 이를 모두 더하면 6입니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND

리스트 컴프리헨션 vs 제너레이터 표현식
- 리스트 컴프리헨션 : 대괄호 [] 로 감싸서 리스트를 즉시 생성, 메모리 상에서 리스트 전체를 생성한 후에 이를 처리
- 제너레이터 표현식 : 대괄호 대신 소괄호 ()를 사용하여 필요한 시점에 값을 하나씩 생성하는 방식, 메모리 효율이 더 좋고, 전체 리스트를 생성하지 않으므로 성능이 더 좋을 수 있다. 

### 💻 접근법
인사이트 : 정수 n을 배열의 요소로 나누었을때 나머지가 0인 것들은 정수 n의 약수이다.

### 🚫 문제해결 중 발생한 에러
- `ZeroDivisionError: integer division or modulo by zero`: 파이썬에서 0으로 나누는 연산을 시도할 때 발생하는 오류
    - `range(n+1)`로 생성된 배열에는 0부터 생성되었기 때문에 0을 나눌수 없어서 발생한 오류 -> `range(1, n+1)`

### 📝 슈도코드
```
def solution(정수 n을 매개변수로 받는다):
    return 1~n+1의 배열을 생성하고 배열의 요소를 i로 순회한다. n을 i로 나눴을때 나머지가 0인 것의 i를 리스트에 추가, 그 이후 리스트 요소의 합을 반환
```
```python
# 풀이 코드
def solution(n):
    return sum(i for i in range(1, n+1) if n % i == 0)
```
- 제러레이터 표현식으로 대괄호 없이 작성되어 값을 하나씩 생성하여 `sum()` 함수에 전달한다.

```python
# 풀이 코드 풀어 쓰기
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n % i == 0:
            answer += i
    return answer
```

