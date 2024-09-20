# [level 0] 최댓값 만들기 (1) - 120847 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120847) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 20일 23:56:09

### 문제 설명

<p>정수 배열 <code>numbers</code>가 매개변수로 주어집니다. <code>numbers</code>의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>0 ≤ <code>numbers</code>의 원소 ≤ 10,000</li>
<li>2 ≤ <code>numbers</code>의 길이 ≤ 100</li>
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
<td>[1, 2, 3, 4, 5]</td>
<td>20</td>
</tr>
<tr>
<td>[0, 31, 24, 10, 1, 9]</td>
<td>744</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>두 수의 곱중 최댓값은 4 * 5 = 20 입니다.</li>
</ul>

<p>입출력 예 #1</p>

<ul>
<li>두 수의 곱중 최댓값은 31 * 24 = 744 입니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🤔 REMIND
- `max(), remove()`
- `sort()` : 리스트를 원본 리스트에 영향을 미치는 (in-place)함수, 정렬이 완료된 후, 리스트는 정렬된 상태로 유지
- `sorted()` : 리스트는 새로운 리스트로 반환하는 함수, 원본 리스트는 변경되지 않는다.

### 💻 접근법
인사이트 : list method

### 📝 슈도코드
```
def solution(매개변수로 numbers 정수배열을 받는다):
    첫번째 최대값 변수 생성 = numbers 배열에서의 최대값
    첫번쨰 최대값을 numbers배열에서 제거
    두번쨰 최대값 변수 생성 = numbers 배열에서 두번째 최대값
    return 첫번째 최대값과 두번째 최대값을 곱하여 반환
```
```python
# 풀이 코드
def solution(numbers):
    first_max_num = max(numbers)
    numbers.remove(first_max_num)
    second_max_num = max(numbers)
    return first_max_num * second_max_num
```

### 👍 다른 정답 코드
1.
```python
def solution(numbers):
    numbers.sort()
    return numbers[-2] * numbers[-1]
```
- `sort()`: 리스트 자체를 정렬, 리스트를 직접 수정하여 정렬된 상태로 바꿈
    - 이후 리스트에서 두번째로 큰값과 가장 큰 값을 가져와 곱한다.

2.
```python
def solution(numbers):
    return sorted(numbers)[-1] * sorted(numbers)[-2]
```
- `sorted(numbers)`: 새로운 정렬된 리스트를 반환, 원본리스트는 변경되지 않는다.
    - 정렬된 새로운 리스트에서 가장 큰 값 * 정렬된 새로운 리스트에서 두번째로 큰 값을 반환
