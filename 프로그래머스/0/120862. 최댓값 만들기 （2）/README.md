# [level 0] 최댓값 만들기 (2) - 120862 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120862?language=python3) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 10월 16일 22:44:53

### 문제 설명

<p>정수 배열 <code>numbers</code>가 매개변수로 주어집니다. <code>numbers</code>의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>-10,000 ≤ <code>numbers</code>의 원소 ≤ 10,000</li>
<li>2 ≤ <code>numbers</code> 의 길이 ≤ 100</li>
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
<td>[1, 2, -3, 4, -5]</td>
<td>15</td>
</tr>
<tr>
<td>[0, -31, 24, 10, 1, 9]</td>
<td>240</td>
</tr>
<tr>
<td>[10, 20, 30, 5, 5, 20, 5]</td>
<td>600</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>두 수의 곱중 최댓값은 -3 * -5 = 15 입니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>두 수의 곱중 최댓값은 10 * 24 = 240 입니다.</li>
</ul>

<p>입출력 예 #3</p>

<ul>
<li>두 수의 곱중 최댓값은 20 * 30 = 600 입니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- 조합 (combination) : 순서를 고려하지 않고, 주어진 요소들 중 일부를 선택하는 경우의 수

### 💻 접근법
인사이트 : 반복문으로 두 배열의 요소를 곱해 최대값을 반환

### 📝 슈도코드
```
def solution(정수 배열 numbers를 매개변수로 받는다):
    answer 변수 선언
    for numbers 리스트의 길이만큼 리스트를 만들고 요소 반복:
        for i+1 ~ numbers길이만큼의 리스트를 만들고 요소 반복:
            answer변수에 numbers[i] * numbers[j] 한 값을 저장
    return answer리스트의 최대값을 반환
```
```python
# 풀이 코드
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] * numbers[j])
    return max(answer)
```
```python
def solution(numbers):
    return max(numbers[i] * numbers[j] for i in range(len(numbers)) for j in range(i + 1, len(numbers)))
```
- 반복문을 사용하므로 시간복잡도는 $O(n²)$ 이다.

### 👍 다른 정답 코드
1.
```python
def solution(numbers):
    numbers.sort()
    return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2] )
```
- 리스트 정렬 후 가장 큰 값 두개와 가장 작은 값 두개를 곱해 두개 중에 최대값을 반환
    - 가장 작은 값 두개를 곱하는 이유는 리스트변수 중 - 값이 있기 때문이다.
- 시간 복잡도 : $O(n log n)$
    - sort()함수의 시간 복잡도 $O(n log n)$ 와 리스트 요소 곱 연산의 상수 시간 $O(1)$ 이므로 전체 시간복잡도는 $O(n log n)$ 이다.
2.
```python
from itertools  import combinations as comb

def solution(numbers):
    an_list=[]
    for i,j in comb(numbers,2):
        an_list.append(i*j)
    return max(an_list)
```
- 각 조합의 곱을 계산하여 최대값을 반환하는 함수
- `from itertools impoer combinations as comb`
    - `for i, j in comb(numbers, 2)`: numbers 리스트에서 길이가 2인 모든 조합을 생성한 요소를 i, j로 반복
- 시간 복잡도 : $O(n²)$
