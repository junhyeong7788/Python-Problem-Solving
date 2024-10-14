# [level 0] 순서쌍의 개수 - 120836 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120836?language=python3) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.14 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 10월 14일 15:46:00

### 문제 설명

<p>순서쌍이란 두 개의 숫자를 순서를 정하여 짝지어 나타낸 쌍으로 (a, b)로 표기합니다. 자연수 <code>n</code>이 매개변수로 주어질 때 두 숫자의 곱이 <code>n</code>인 자연수 순서쌍의 개수를 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ n ≤ 1,000,000</li>
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
<td>20</td>
<td>6</td>
</tr>
<tr>
<td>100</td>
<td>9</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li><code>n</code>이 20 이므로 곱이 20인 순서쌍은 (1, 20), (2, 10), (4, 5), (5, 4), (10, 2), (20, 1) 이므로 6을 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li><code>n</code>이 100 이므로 곱이 100인 순서쌍은 (1, 100), (2, 50), (4, 25), (5, 20), (10, 10), (20, 5), (25, 4), (50, 2), (100, 1) 이므로 9를 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- `filter(function, iterable)`: 주어진 함수 function이 참인 요소들만 모아서 새로운 이터레이터를 반환
- 제곱근 범위 반복 

### 💻 접근법
인사이트 : 
- `n % a == 0`: 정수 n의 약수
- `b = n // a` : b는 a에 대응하는 약수로, n을 a로 나눈 몫
- `(a, b)` : 약수의 순서쌍

### 📝 슈도코드
```
def solution(정수 n을 매개변수로 받는다):
    변수 a 선언
    pairs 리스트 선언
    for 1 ~ n+1의 리스트를 생성하고 a로 리스트 요소를 반복:
        if 정수 n을 a로 나누었을 때 나머지가 0과 같다면:
            변수 b = 정수 n을 a로 나눴을 때의 몫
            pairs리스트에 (a,b) 로 저장
    return pairs 리스트의 길이를 반환
```
```python
# 풀이 코드
def solution(n):
    a = 0
    pairs = []
    for a in range(1, n+1):
        if n % a == 0:
            b = n // a
            pairs.append((a, b))
    return len(pairs)
```

### 👍 다른 정답 코드
1.
```python
# ChatGPT 코드 개선
def solution(n):
    pairs_count = 0
    for a in range(1, int(n**0.5) + 1):
        if n % a == 0:
            pairs_count += 1  # a는 n % a == 0
            if a != n // a:  
                pairs_count += 1 # b는 n // a 
    return pairs_count
```
- 해당 코드로 진행 시 시간복잡도가 많이 낮아졌다.
- 제곱근 범위 반복 `for a in range(1, int(n**0.5) + 1)` :  a는 1부터 $\sqrt{n}$ 까지 반복, 약수를 찾는 데 필요한 횟수를 대폭 줄여, 최대 $\sqrt{n}$번의 반복으로 시간복잡도가 $O(\sqrt{n})$로 개선
    - ex: n = 36일 경우 a는 1,2,3,4,5,6까지 반복
- 대칭성 활용 : ` a \times b = n` 의 성질을 활용, $b$는 $n//a$로 계산되며, a와 b가 다를 경우에만 카운트한다. (= 중복된 쌍을 방지)
2.
```python
def solution(n):
    return len(list(filter(lambda v: n % (v+1) == 0, range(n))))
```
- `filter(function, iterable)`: 주어진 함수 function이 참인 요소들만 모아서 새로운 이터레이터를 반환
    - n의 약수들, 즉 n을 v+1로 나누었을 때 나누어떨어지는 숫자들만 추출
